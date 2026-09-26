#!/usr/bin/env python3
"""Can harness/conformance.py tell a good harness from a bad one?

    python scripts/test_conformance.py

The conformance test is what a model's self-built harness must pass before it is left running.
A test nobody has seen fail is a claim, so this runs it against scripts/reference_agent.py,
where every check must hold, and then against copies of it with exactly one property broken,
where it must report at least one check broken. A broken property the test does not notice is
a hole in the test, and fails this.
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFERENCE = ROOT / "scripts" / "reference_agent.py"
CONFORMANCE = ROOT / "harness" / "conformance.py"

# (the property broken, the text replaced, what replaces it)
BROKEN = [
    ("a conversation that grows every step instead of a fresh context",
     '"messages": [{"role": "system", "content": RULES},\n'
     '                                        {"role": "user", "content": prompt}]}).encode()',
     '"messages": self.__dict__.setdefault("convo", [{"role": "system", "content": RULES}])\n'
     '                                    + [{"role": "user", "content": p} for p in self.__dict__.setdefault("said", []) + [prompt]]}).encode()\n'
     '        self.said.append(prompt)'),
    ("no budget on recent actions",
     "            if tokens(\"\\n\".join(recent + [item])) > left:\n                break\n", ""),
    ("files written anywhere",
     "        path = (self.work / name).resolve()\n"
     "        if path != self.work and self.work not in path.parents:\n"
     "            raise PermissionError(f\"{name} is outside the project\")\n"
     "        return path",
     "        return self.work / name"),
    ("the model can write the person's file",
     "            if parts and parts[0] in KEPT:", "            if False:"),
    ("commands run somewhere other than the project",
     "shell=True, cwd=self.work,", "shell=True, cwd=None,"),
    ("a choice that waits for the person",
     '            return f"recorded as C{n}; carry on"',
     '            input("waiting for the person: ")\n            return f"recorded as C{n}; carry on"'),
    ("no checkpoints", "            self.checkpoint(f\"step {self.step}: {action['tool']}\")", "            pass"),
    ("STATE.md not read back", 'state = path.read_text(encoding="utf-8") if path.exists() else "(empty)"',
     'state = "(empty)"'),
    ("the person's overrides not shown", 'overridden = "\\n".join(self.overrides()) or "(nothing)"',
     'overridden = "(nothing)"'),
    ("STOP ignored", '            if (self.home / "STOP").exists():', "            if False:"),
    ("remote endpoints allowed by default", "        if not self.local and not self.a.allow_remote:", "        if False:"),
    ("the full skill always loaded", "        if tokens(RULES + full) <= self.budget() // 2:", "        if True:"),
]


def conform(harness: Path, where: Path) -> tuple[int, str]:
    # Run from a scratch directory: a broken harness that ignores --workdir writes to its
    # current directory, and that must not be the repository.
    done = subprocess.run([sys.executable, str(CONFORMANCE), "--harness", f"{sys.executable} {harness}",
                           "--timeout", "60"], capture_output=True, text=True, cwd=where)
    return done.returncode, done.stdout + done.stderr


def main() -> int:
    problems = []
    scratch = tempfile.mkdtemp()
    code, output = conform(REFERENCE, Path(scratch))
    if code != 0:
        problems.append(f"the reference fails the conformance test:\n{output}")
    source = REFERENCE.read_text(encoding="utf-8")
    with tempfile.TemporaryDirectory() as tmp:
        for number, (name, old, new) in enumerate(BROKEN):
            if old not in source:
                problems.append(f"{name}: the text to break is not in reference_agent.py any more")
                continue
            broken = Path(tmp) / f"broken_{number}.py"
            broken.write_text(source.replace(old, new, 1), encoding="utf-8")
            code, output = conform(broken, Path(scratch))
            if code == 0 or "broken" not in output:
                problems.append(f"{name}: the conformance test passed a harness with it\n{output[-500:]}")
    total = len(BROKEN) + 1
    if problems:
        print(f"{len(problems)} of {total} broken:")
        for problem in problems:
            print(f"  - {problem}")
        return 1
    print(f"conformance.py: passes the reference, and catches all {len(BROKEN)} broken harnesses.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
