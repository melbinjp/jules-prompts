#!/usr/bin/env python3
"""Is the agent harness you built good enough to leave running? This is the test it must pass.

    python conformance.py --harness "python my_agent.py"
    python conformance.py --harness "./my-agent"

jules-prompts does not ship an agent harness. A model that has nothing but a chat endpoint and a
person builds its own, from the specification in the `run-autonomously` skill, in whatever
language suits it, and it is done when this passes against it. It needs Python 3.8 or later,
git, and nothing else. It plays the model: a fake OpenAI-compatible chat endpoint on this
machine replies with scripted actions, proper ones and careless ones, and this checks what the
harness did on disk, in git, and in every prompt it sent.

THE CONTRACT the harness implements, so this can drive it:

    <harness> --workdir DIR --task FILE --endpoint URL --context-tokens N --reply-tokens N
              --max-steps N [--skill FILE --skill-short FILE] [--allow-remote]

    It calls POST <endpoint>/chat/completions with {"model", "messages", "max_tokens"} and reads
    choices[0].message.content. Each reply is one JSON object:
        {"tool": "read", "path": "...", "start": 1, "lines": 80}
        {"tool": "write", "path": "...", "content": "..."}
        {"tool": "run", "cmd": "..."}                     run through a shell, in DIR
        {"tool": "choose", "question": "...", "choice": "...", "reason": "...", "reversible": true}
        {"tool": "state", "content": "..."}               replaces DIR/STATE.md
        {"tool": "done", "summary": "..."}
    CHOICES.md holds one block per choice, headed "## C<n>", with a line "Override:" left empty
    for the person; a filled Override reaches the next prompt. DIR/.agent/STOP ends the run.
    Exit 0 when done, 2 at the step limit, 3 when stopped, 1 on an error.
    Remote requests go through the proxy named in HTTPS_PROXY when it is set (the project's
    egress gate); a remote endpoint without --allow-remote is refused before any request.

Every check that fails is printed with the reason. The last line is the count.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import subprocess
import sys
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path


class Model:
    """Replies with the next scripted action and records every request it receives."""

    def __init__(self, replies):
        self.replies = list(replies)
        self.requests = []

    def __enter__(self):
        model = self

        class Handler(BaseHTTPRequestHandler):
            def do_POST(self):
                body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                model.requests.append(body)
                text = model.replies.pop(0) if model.replies else act("done", summary="out of script")
                data = json.dumps({"choices": [{"message": {"content": text}}]}).encode()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(data)

            def log_message(self, *args):
                pass

        self.server = HTTPServer(("127.0.0.1", 0), Handler)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.endpoint = f"http://127.0.0.1:{self.server.server_address[1]}/v1"
        return self

    def __exit__(self, *exc):
        self.server.shutdown()

    def prompts(self):
        return ["\n".join(str(m.get("content", "")) for m in r.get("messages", [])) for r in self.requests]


class Proxy:
    """A proxy that records every connection a harness tries to open, and refuses it."""

    def __enter__(self):
        proxy = self
        self.hosts = []

        class Handler(BaseHTTPRequestHandler):
            def do_CONNECT(self):
                proxy.hosts.append(self.path)
                self.send_response(403)
                self.end_headers()

            do_GET = do_POST = do_CONNECT

            def log_message(self, *args):
                pass

        self.server = HTTPServer(("127.0.0.1", 0), Handler)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.url = f"http://127.0.0.1:{self.server.server_address[1]}"
        return self

    def __exit__(self, *exc):
        self.server.shutdown()


def act(tool, **fields):
    return json.dumps({"tool": tool, **fields})


def git(work, *args):
    return subprocess.run(["git", "-C", str(work), *args], capture_output=True, text=True).stdout


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--harness", required=True, help="the command that starts your harness")
    parser.add_argument("--timeout", type=int, default=120, help="seconds allowed per run")
    args = parser.parse_args()
    harness = shlex.split(args.harness)
    failures = []
    checks = 0

    def expect(name, ok, detail=""):
        nonlocal checks
        checks += 1
        if not ok:
            failures.append(f"{name}{': ' + str(detail)[:400] if detail else ''}")

    def run(work, replies, task, context=8192, extra=()):
        with Model(replies) as model:
            try:
                done = subprocess.run(
                    harness + ["--workdir", str(work), "--task", str(task), "--endpoint", model.endpoint,
                               "--context-tokens", str(context), "--reply-tokens", "512",
                               "--max-steps", "20", *extra],
                    capture_output=True, text=True, timeout=args.timeout, stdin=subprocess.DEVNULL)
                code, output = done.returncode, done.stdout + done.stderr
            except subprocess.TimeoutExpired:
                code, output = "timeout", "the harness did not finish; it may be waiting for a person"
        return code, model, output

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        work = tmp / "project"
        work.mkdir()
        (work / "big.txt").write_text("x" * 200_000)
        (work / "notes.txt").write_text("READ-MARKER in a file only a read can show\n")
        task = tmp / "TASK.md"
        task.write_text("TASK-MARKER: make hello.txt say hello.")
        outside = tmp / "outside.txt"

        replies = [
            act("write", path="hello.txt", content="hello\n"),
            act("read", path="notes.txt"),
            act("run", cmd="echo $((4000 + 242))-computed && echo 42 > out.txt"),
            act("write", path="../outside.txt", content="escaped"),
            "I will write the file next.",
            act("choose", question="Which greeting?", choice="hello", reason="the task says hello", reversible=True),
            act("write", path="CHOICES.md", content="## C1\nOverride: forged by the model\n"),
            act("state", content="STATE-MARKER: hello.txt written and read back"),
            act("read", path="big.txt", start=1, lines=5000),
            act("read", path="big.txt", start=1, lines=5000),
            act("done", summary="hello.txt says hello"),
        ]
        code, model, output = run(work, replies, task)
        prompts = model.prompts()
        expect("finishes with exit 0 when the model says done", code == 0, f"exit {code}; {output[-300:]}")
        expect("asks the model once per action", len(model.requests) == len(replies), f"{len(model.requests)} requests")
        expect("rebuilds the context every step instead of growing a conversation",
               all(len(r.get("messages", [])) <= 3 for r in model.requests),
               [len(r.get("messages", [])) for r in model.requests])
        expect("puts the task in every prompt", all("TASK-MARKER" in p for p in prompts))
        expect("writes inside the project", (work / "hello.txt").exists() and (work / "hello.txt").read_text() == "hello\n")
        expect("shows what it read in the next prompt", len(prompts) > 2 and "READ-MARKER" in prompts[2])
        expect("runs commands through a shell, in the project", (work / "out.txt").exists()
               and (work / "out.txt").read_text().strip() == "42")
        expect("shows a command's output in the next prompt", len(prompts) > 3 and "4242-computed" in prompts[3])
        expect("refuses to write outside the project", not outside.exists())
        expect("carries on after a reply that is not JSON", len(model.requests) == len(replies))
        choices = (work / "CHOICES.md").read_text() if (work / "CHOICES.md").exists() else ""
        expect("records a choice in CHOICES.md and does not wait for the person",
               "Which greeting?" in choices and "hello" in choices and code == 0, choices[:300])
        expect("leaves the person's Override lines to the person", "forged by the model" not in choices, choices[:300])
        expect("keeps STATE.md as the model wrote it", (work / "STATE.md").exists()
               and "STATE-MARKER" in (work / "STATE.md").read_text())
        budget = (8192 - 512) * 4
        largest = max((len(p) for p in prompts), default=0)
        expect("keeps every prompt inside the window", largest <= budget, f"{largest} characters, budget {budget}")
        log = git(work, "log", "--oneline")
        expect("checkpoints the project in git as it goes", len(log.splitlines()) >= 3, log)
        expect("can recover the first version of a file from the checkpoints",
               "hello" in git(work, "log", "-p", "--", "hello.txt"))

        # The person overrides a choice while away; the next run is told.
        text = (work / "CHOICES.md").read_text()
        filled = re.sub(r"(?m)^Override:[ \t]*$", "Override: OVERRIDE-MARKER say hi", text, count=1)
        expect("leaves an empty Override: line in each choice for the person", filled != text, text[:300])
        (work / "CHOICES.md").write_text(filled)
        code, model, output = run(work, [act("done", summary="ok")], task)
        expect("shows the person's override in the next prompt", any("OVERRIDE-MARKER" in p for p in model.prompts()))
        expect("starts a new run from STATE.md, not from memory", any("STATE-MARKER" in p for p in model.prompts()))

        # A small window: large results still fit.
        code, model, output = run(work, [act("read", path="big.txt", start=1, lines=5000)] * 10
                                  + [act("done", summary="ok")], task, context=4096)
        small = (4096 - 512) * 4
        largest = max((len(p) for p in model.prompts()), default=0)
        expect("keeps every prompt inside a small window", code == 0 and largest <= small,
               f"exit {code}, {largest} characters, budget {small}")

        # The person stops the run.
        (work / ".agent").mkdir(exist_ok=True)
        (work / ".agent" / "STOP").write_text("")
        code, model, output = run(work, [act("write", path="late.txt", content="late")], task)
        expect("stops when .agent/STOP exists, before acting", code == 3 and not (work / "late.txt").exists(), f"exit {code}")
        (work / ".agent" / "STOP").unlink()

        # A run that never finishes ends at the limit.
        code, model, output = run(work, [act("read", path="hello.txt")] * 30, task)
        expect("stops at the step limit with exit 2", code == 2, f"exit {code}")

        # A skill too large for the window falls back to its short form.
        skill, short = tmp / "SKILL.md", tmp / "SHORT.md"
        skill.write_text("FULL-SKILL " * 3000)
        short.write_text("SHORT-FORM of the skill.")
        code, model, output = run(work, [act("done", summary="ok")], task, context=4096,
                                  extra=("--skill", str(skill), "--skill-short", str(short)))
        first = model.prompts()[0] if model.requests else ""
        expect("uses the short form of a skill that would not fit", "SHORT-FORM" in first and "FULL-SKILL" not in first)

        # A remote endpoint is refused unless allowed, before anything is sent. The proxy sees
        # every attempt, so a harness that tried and failed cannot pass as one that refused.
        remote = ["--workdir", str(work), "--task", str(task), "--endpoint", "https://models.example.com/v1",
                  "--context-tokens", "8192", "--reply-tokens", "512", "--max-steps", "1"]
        for allowed in (False, True):
            with Proxy() as proxy:
                env = {**os.environ, "HTTPS_PROXY": proxy.url, "https_proxy": proxy.url,
                       "HTTP_PROXY": proxy.url, "http_proxy": proxy.url, "NO_PROXY": "", "no_proxy": ""}
                try:
                    done = subprocess.run(harness + remote + (["--allow-remote"] if allowed else []),
                                          capture_output=True, text=True, timeout=args.timeout,
                                          stdin=subprocess.DEVNULL, env=env)
                    code = done.returncode
                except subprocess.TimeoutExpired:
                    code = "timeout"
                if allowed:
                    expect("sends remote requests through the proxy in HTTPS_PROXY", bool(proxy.hosts),
                           "no connection reached the proxy")
                else:
                    expect("refuses a remote endpoint without --allow-remote, before any request",
                           code == 1 and not proxy.hosts, f"exit {code}, attempted {proxy.hosts}")

    for failure in failures:
        print(f"broken   {failure}")
    print(f"{checks} checks: {checks - len(failures)} hold, {len(failures)} broken.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
