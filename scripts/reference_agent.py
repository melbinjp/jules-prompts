#!/usr/bin/env python3
"""A reference implementation of the harness contract, kept only to prove the conformance test.

jules-prompts does not give a model a harness: a model with only a chat endpoint builds its own
from the specification in the `run-autonomously` skill, and `harness/conformance.py` decides
whether what it built is good enough. A test nobody has seen pass and fail is a claim, so this
file exists for one reason: `scripts/test_conformance.py` runs the conformance test against it,
where it must pass, and against copies of it with one property broken, where it must fail. It is
not published on the site or offered as a tool.

The properties it demonstrates, which the skill specifies:
    - a fresh, bounded context every step, rebuilt from files: rules, task, skill (the short
      form when the full one would not fit), STATE.md, the person's overrides, recent actions;
    - actions as one JSON object per reply; commands through a shell, in the project;
    - files only inside the project; CHOICES.md and .agent/ kept by the harness and the person;
    - choices recorded and never waited on; the person overrides them in CHOICES.md;
    - a git checkpoint after every step that changed the project;
    - .agent/STOP, a step limit, and a refusal to send prompts off the local network unless
      --allow-remote says so.
"""
from __future__ import annotations

import argparse
import datetime
import ipaddress
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

RULES = """You are an agent working on a project. Reply with exactly one JSON object and nothing else. The actions:
{"tool": "read", "path": "<file>", "start": 1, "lines": 80}
{"tool": "write", "path": "<file>", "content": "<the whole new file>"}
{"tool": "run", "cmd": "<shell command, run in the project>"}
{"tool": "choose", "question": "<what was open>", "choice": "<what you chose>", "reason": "<why>", "reversible": true}
{"tool": "state", "content": "<where the work is, what was decided and why, what is next; under 40 lines>"}
{"tool": "done", "summary": "<what was done, and the checks that passed>"}
Rules:
- You see only this message. Keep STATE current: it is your only memory.
- Every fact you use comes from a file you read, a command you ran, or the person. Check before you rely on anything.
- Decide for yourself where the briefing is silent: look it up, test it, choose, and record the choice. Never wait.
- Nothing is done until its checks pass. Run them."""

KEPT = ("CHOICES.md", ".agent")
CHOICES_HEAD = "# Choices the agent made\n\nWrite after \"Override:\" to change one. The agent applies it at its next step.\n"
RESULT_CHARS = 2000


def tokens(text):
    return len(text) // 3 + 1


def cut(text, chars):
    if len(text) <= chars:
        return text
    half = max(chars // 2 - 40, 0)
    return f"{text[:half]}\n[... {len(text) - 2 * half} characters cut ...]\n{text[-half:]}"


class Agent:
    def __init__(self, a):
        self.a = a
        self.work = Path(a.workdir).resolve()
        self.home = self.work / ".agent"
        (self.home / "out").mkdir(parents=True, exist_ok=True)
        self.task = Path(a.task).read_text(encoding="utf-8") if Path(a.task).is_file() else a.task
        self.skill = self.pick_skill()
        self.history, self.step = [], 0
        host = urllib.parse.urlparse(a.endpoint).hostname or ""
        self.local = host == "localhost" or self.private(host)
        self.opener = urllib.request.build_opener(*([urllib.request.ProxyHandler({})] if self.local else []))

    @staticmethod
    def private(host):
        try:
            address = ipaddress.ip_address(host)
        except ValueError:
            return False
        return address.is_loopback or address.is_private

    def budget(self):
        return self.a.context_tokens - self.a.reply_tokens

    def pick_skill(self):
        full = Path(self.a.skill).read_text(encoding="utf-8") if self.a.skill else ""
        if tokens(RULES + full) <= self.budget() // 2:
            return full
        short = Path(self.a.skill_short).read_text(encoding="utf-8") if self.a.skill_short else ""
        if short and tokens(RULES + short) <= self.budget() // 2:
            return short
        raise SystemExit("the skill does not fit in half the window, even in short form")

    def overrides(self):
        path = self.work / "CHOICES.md"
        if not path.exists():
            return []
        found = []
        for block in path.read_text(encoding="utf-8").split("\n## C")[1:]:
            lines = block.splitlines()
            fields = {k.strip().lower(): v.strip() for k, _, v in (line.partition(":") for line in lines[1:])}
            if fields.get("override"):
                found.append(f"C{lines[0].strip()}: {fields.get('question', '')} -> {fields['override']}")
        return found

    def prompt(self):
        room = self.budget() - tokens(RULES)
        path = self.work / "STATE.md"
        state = path.read_text(encoding="utf-8") if path.exists() else "(empty)"
        overridden = "\n".join(self.overrides()) or "(nothing)"
        head = (f"TASK\n{self.task.strip()}\n\nSKILL\n{self.skill.strip()}\n\n"
                f"STATE.md\n{cut(state, room * 3 // 5).strip()}\n\n"
                f"THE PERSON OVERRODE\n{cut(overridden, room * 3 // 10)}\n")
        tail = f"\nSTEP {self.step} of {self.a.max_steps}. Reply with one JSON object."
        left = room - tokens(head + tail)
        if left < 0:
            raise SystemExit("the task, skill and STATE.md no longer fit the window")
        recent = []
        for item in reversed(self.history[-8:]):
            if tokens("\n".join(recent + [item])) > left:
                break
            recent.insert(0, item)
        return head + "\nRECENT ACTIONS\n" + ("\n".join(recent) or "(none)") + tail

    def ask(self, prompt):
        body = json.dumps({"model": self.a.model, "max_tokens": self.a.reply_tokens, "temperature": 0.2,
                           "messages": [{"role": "system", "content": RULES},
                                        {"role": "user", "content": prompt}]}).encode()
        headers = {"Content-Type": "application/json"}
        if os.environ.get("AGENT_API_KEY"):
            headers["Authorization"] = "Bearer " + os.environ["AGENT_API_KEY"]
        last = None
        for attempt in range(3):
            try:
                url = self.a.endpoint.rstrip("/") + "/chat/completions"
                with self.opener.open(urllib.request.Request(url, data=body, headers=headers), timeout=600) as reply:
                    return json.load(reply)["choices"][0]["message"]["content"]
            except (urllib.error.URLError, OSError, KeyError, IndexError, ValueError) as error:
                last = error
                time.sleep(2 ** attempt)
        raise SystemExit(f"the model endpoint failed three times ({last})")

    def inside(self, name):
        path = (self.work / name).resolve()
        if path != self.work and self.work not in path.parents:
            raise PermissionError(f"{name} is outside the project")
        return path

    def act(self, action):
        tool = action.get("tool")
        if tool == "read":
            lines = self.inside(action["path"]).read_text(encoding="utf-8", errors="replace").splitlines()
            start, count = max(int(action.get("start", 1)), 1), int(action.get("lines", 80))
            shown = "\n".join(lines[start - 1:start - 1 + count])
            return f"{action['path']} from line {start} of {len(lines)}\n{shown}"
        if tool == "write":
            path = self.inside(action["path"])
            parts = path.relative_to(self.work).parts
            if parts and parts[0] in KEPT:
                raise PermissionError(f"{action['path']} is kept by the harness and the person")
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(action["content"], encoding="utf-8")
            return f"wrote {action['path']}"
        if tool == "run":
            try:
                done = subprocess.run(action["cmd"], shell=True, cwd=self.work, capture_output=True,
                                      text=True, timeout=self.a.command_timeout)
            except subprocess.TimeoutExpired:
                return f"stopped after {self.a.command_timeout} s"
            output = (done.stdout + done.stderr).strip()
            (self.home / "out" / f"step-{self.step}.txt").write_text(output, encoding="utf-8")
            return f"exit {done.returncode}; full output .agent/out/step-{self.step}.txt\n{cut(output, RESULT_CHARS)}"
        if tool == "choose":
            path = self.work / "CHOICES.md"
            text = path.read_text(encoding="utf-8") if path.exists() else CHOICES_HEAD
            n = text.count("\n## C") + 1
            clean = {k: " ".join(str(action.get(k, "")).split()) for k in ("question", "choice", "reason")}
            text += (f"\n## C{n}\nQuestion: {clean['question']}\nChoice: {clean['choice']}\n"
                     f"Reason: {clean['reason']}\nReversible: {'yes' if action.get('reversible', True) else 'no'}\n"
                     "Override:\n")
            path.write_text(text, encoding="utf-8")
            return f"recorded as C{n}; carry on"
        if tool == "state":
            (self.work / "STATE.md").write_text(action["content"], encoding="utf-8")
            return "STATE.md replaced"
        raise ValueError(f"unknown tool {tool!r}")

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.work), *args], capture_output=True, text=True)

    def checkpoint(self, label):
        if self.git("rev-parse", "--git-dir").returncode != 0:
            self.git("init", "-q")
            (self.work / ".git" / "info").mkdir(parents=True, exist_ok=True)
            with (self.work / ".git" / "info" / "exclude").open("a") as handle:
                handle.write("\n.agent/\n")
        self.git("add", "-A")
        if self.git("diff", "--cached", "--quiet").returncode == 0:
            return
        who = [] if self.git("config", "user.email").stdout.strip() else [
            "-c", "user.name=agent", "-c", "user.email=agent@localhost"]
        subprocess.run(["git", "-C", str(self.work), *who, "commit", "-q", "-m", label], capture_output=True)

    def log(self, entry):
        entry["time"] = datetime.datetime.now().isoformat(timespec="seconds")
        with (self.home / "log.jsonl").open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(entry) + "\n")

    def loop(self):
        print(f"endpoint {self.a.endpoint} ({'local' if self.local else 'REMOTE'})", flush=True)
        if not self.local and not self.a.allow_remote:
            print("refusing a remote endpoint without --allow-remote", file=sys.stderr)
            return 1
        self.checkpoint("checkpoint before the run")
        while self.step < self.a.max_steps:
            if (self.home / "STOP").exists():
                return 3
            self.step += 1
            prompt = self.prompt()
            reply = self.ask(prompt)
            start, end = reply.find("{"), reply.rfind("}")
            try:
                action = json.loads(reply[start:end + 1]) if start != -1 and end > start else None
                if not isinstance(action, dict) or "tool" not in action:
                    raise ValueError("no JSON object with a tool")
            except ValueError as error:
                self.history.append(f"[step {self.step}] unreadable reply ({error}); reply with one JSON object")
                continue
            if action["tool"] == "done":
                self.log({"step": self.step, "action": action})
                print(f"done: {action.get('summary', '')}")
                return 0
            try:
                result = self.act(action)
            except (OSError, ValueError, KeyError) as error:
                result = f"refused or failed: {error}"
            shown = {k: cut(v, 300) if isinstance(v, str) else v for k, v in action.items()}
            self.history.append(f"[step {self.step}] {json.dumps(shown)} -> {cut(result, RESULT_CHARS)}")
            self.log({"step": self.step, "prompt_tokens": tokens(prompt), "action": shown, "result": cut(result, 500)})
            self.checkpoint(f"step {self.step}: {action['tool']}")
        return 2


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--workdir", required=True)
    p.add_argument("--task", required=True)
    p.add_argument("--skill", default="")
    p.add_argument("--skill-short", default="")
    p.add_argument("--endpoint", default=os.environ.get("AGENT_ENDPOINT", "http://127.0.0.1:8080/v1"))
    p.add_argument("--model", default=os.environ.get("AGENT_MODEL", "local"))
    p.add_argument("--allow-remote", action="store_true")
    p.add_argument("--context-tokens", type=int, default=8192)
    p.add_argument("--reply-tokens", type=int, default=1024)
    p.add_argument("--max-steps", type=int, default=50)
    p.add_argument("--command-timeout", type=int, default=600)
    return Agent(p.parse_args(argv)).loop()


if __name__ == "__main__":
    sys.exit(main())
