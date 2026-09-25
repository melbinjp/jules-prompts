#!/usr/bin/env python3
"""Can harness/check_trace.py fail? Each rule, broken once on purpose.

    python scripts/test_check_trace.py

The worked example in harness/ledger-example/ must pass. Then each case below copies it,
breaks exactly one thing, and requires the checker to exit 1 and name that thing. A rule
with no case here is a rule nobody has seen fail, which this library does not count as a
rule. The last case builds a small git history and checks the commit trailers.
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECK = ROOT / "harness" / "check_trace.py"
EXAMPLE = ROOT / "harness" / "ledger-example"
D1 = "decisions/D0001-store-bookings-in-sqlite.md"
D2 = "decisions/D0002-host-on-the-shop-pi.md"


def run(root: Path, *extra: str) -> tuple[int, str]:
    done = subprocess.run([sys.executable, str(CHECK), "--root", str(root), *extra],
                          capture_output=True, text=True)
    return done.returncode, done.stdout + done.stderr


def edit(root: Path, name: str, old: str, new: str) -> None:
    path = root / name
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise SystemExit(f"test setup: {old!r} is not in {name}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def drop_lines(root: Path, name: str, pattern: str) -> None:
    path = root / name
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    kept = [line for line in lines if not re.search(pattern, line)]
    if len(kept) == len(lines):
        raise SystemExit(f"test setup: nothing in {name} matches {pattern!r}")
    path.write_text("".join(kept), encoding="utf-8")


# (what is broken, how to break it, what the checker must say)
CASES = [
    ("no ledger", lambda r: (r / "PROJECT.md").unlink(), "PROJECT.md: missing"),
    ("no goal", lambda r: drop_lines(r, "PROJECT.md", r"^\| G1 "), "no G row"),
    ("no course change", lambda r: drop_lines(r, "PROJECT.md", r"^\| K\d "), "no K row"),
    ("no milestone", lambda r: drop_lines(r, "PROJECT.md", r"^\| MS\d "), "no MS row"),
    ("measure with no method",
     lambda r: edit(r, "PROJECT.md", "| the hosting invoice |", "| <how> |"),
     "M3 needs what is measured"),
    ("milestone that moves nothing",
     lambda r: edit(r, "PROJECT.md", "two weeks. | M1, M2 |", "two weeks. | - |"),
     "milestone MS1 moves no measure"),
    ("resource nobody chose", lambda r: edit(r, "PROJECT.md", "| hosting | D0002 |", "| hosting | Fly.io |"),
     "resource R1 names no decision"),
    ("measure nothing works toward",
     lambda r: (edit(r, "PROJECT.md", "| M1, M2, M3 |", "| M1, M2 |"),
                edit(r, D2, "serves: [M3]", "serves: [M1]")),
     "M3 is moved by no milestone"),
    ("defined twice", lambda r: edit(r, "PROJECT.md", "| M2 | bookings", "| M1 | bookings"),
     "M1 is defined twice"),
    ("decision serving nothing", lambda r: edit(r, D2, "serves: [M3]", "serves: []"),
     "serves nothing"),
    ("decision serving an unknown ID", lambda r: edit(r, D2, "serves: [M3]", "serves: [M9]"),
     "serves M9, which the ledger does not define"),
    ("one-way with two options", lambda r: drop_lines(r, D1, r"^- A hosted Postgres"),
     "lists 2 option(s); a one-way needs at least 3"),
    ("one-way with one backing", lambda r: drop_lines(r, D1, r"^- Calculation"),
     "lists 1 piece(s) of evidence; every decision needs at least 2 backings"),
    ("two-way with one backing", lambda r: drop_lines(r, D2, r"^- Measured"),
     "lists 1 piece(s) of evidence; every decision needs at least 2 backings"),
    ("evidence that does not say its kind",
     lambda r: edit(r, D1, "- Calculation: 60 members", "- Worked out: 60 members"),
     "does not start with its kind"),
    ("evidence that is all read, none verified",
     lambda r: (edit(r, D2, "- Measured: the app", "- Source: the app"),
                edit(r, D2, "- Calculation: the £4", "- Source: the £4")),
     "every backing is a source someone else wrote"),
    ("one-way backed by one kind of evidence",
     lambda r: edit(r, D1, "- Calculation: 60 members", "- Measured: 60 members"),
     "one-way with 1 kind(s) of evidence"),
    ("one-way with no way out", lambda r: drop_lines(r, D1, r"^- Moving to Postgres"),
     "one-way with no Exit section"),
    ("one-way nobody approved", lambda r: drop_lines(r, D1, r"^approved_by:"),
     "no approved_by"),
    ("accepted, never to be reopened", lambda r: drop_lines(r, D2, r"^revisit:"),
     "no revisit condition"),
    ("unknown status", lambda r: edit(r, D2, "status: accepted", "status: done"),
     "status 'done'"),
    ("unknown door", lambda r: edit(r, D2, "door: two-way", "door: maybe"), "door 'maybe'"),
    ("superseded by nothing",
     lambda r: edit(r, D2, "status: accepted", "status: superseded\nsuperseded_by: D0009"),
     "superseded by 'D0009'"),
    ("id that disagrees with the file", lambda r: edit(r, D2, "id: D0002", "id: D0003"),
     "does not match the file name"),
    ("decision file with no number",
     lambda r: (r / D2).rename(r / "decisions" / "host-on-the-pi.md"),
     "name it D0001-short-name.md"),
]


def git(root: Path, *args: str) -> None:
    env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.com",
           "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.com"}
    subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True, env=env)


def main() -> int:
    failures: list[str] = []
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp) / "base"
        shutil.copytree(EXAMPLE, base)
        code, out = run(base)
        if code != 0:
            failures.append(f"the worked example does not pass:\n{out}")

        for number, (name, breaks, expected) in enumerate(CASES):
            case = Path(tmp) / f"case{number}"
            shutil.copytree(EXAMPLE, case)
            breaks(case)
            code, out = run(case)
            if code != 1 or expected not in out:
                failures.append(f"{name}: expected exit 1 naming {expected!r}, got exit "
                                f"{code}:\n{out}")

        # Commits: one that serves a measure and says how it was verified, one that serves
        # nothing, one that serves a rejected decision, one that does not say how it was
        # verified. Only the first may pass.
        repo = Path(tmp) / "repo"
        shutil.copytree(EXAMPLE, repo)
        edit(repo, D2, "status: accepted", "status: rejected")
        git(repo, "init", "-q", "-b", "main")
        git(repo, "add", ".")
        git(repo, "commit", "-q", "-m", "Start the ledger\n\nServes: G1\nVerified: check_trace.py passes")
        (repo / "a.txt").write_text("a\n")
        git(repo, "add", ".")
        git(repo, "commit", "-q", "-m", "Refuse a second booking for the same slot\n\nServes: M1, J1\nVerified: tests/test_race.py, 1 of 200 succeeds")
        (repo / "b.txt").write_text("b\n")
        git(repo, "add", ".")
        git(repo, "commit", "-q", "-m", "Tidy things up")
        (repo / "c.txt").write_text("c\n")
        git(repo, "add", ".")
        git(repo, "commit", "-q", "-m", "Move to the Pi\n\nServes: D0002\nVerified: make load")
        (repo / "d.txt").write_text("d\n")
        git(repo, "add", ".")
        git(repo, "commit", "-q", "-m", "Send reminders at six\n\nServes: J1")
        code, out = run(repo, "--commits", "HEAD~4..HEAD")
        for expected in ("(Tidy things up): no Serves: line", "serves D0002, which is rejected",
                         "(Send reminders at six): no Verified: line"):
            if expected not in out:
                failures.append(f"commits: expected {expected!r}:\n{out}")
        if "Refuse a second booking" in out or code != 1:
            failures.append(f"commits: the traced commit was flagged, or exit was {code}:\n{out}")
        code, out = run(repo, "--commits", "HEAD..HEAD")
        if code != 1 or "no commits in the range" not in out:
            failures.append(f"empty range: expected a refusal, got exit {code}:\n{out}")

    total = len(CASES) + 4
    if failures:
        print(f"{len(failures)} of {total} cases broken:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(f"check_trace.py: the example passes, and all {total} ways of breaking it are caught.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
