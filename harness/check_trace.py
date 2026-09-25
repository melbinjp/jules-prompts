#!/usr/bin/env python3
"""Does every part of this project have a reason, and does every reason lead to the goal?

    python check_trace.py                       # the ledger in this directory
    python check_trace.py --root path/to/project
    python check_trace.py --commits origin/main..HEAD   # and every commit in the range

Copy this file into a project that keeps a ledger, and run it in CI. It needs Python 3.8 or
later and nothing else. It is the mechanical half of the jules-prompts lifecycle skills
(found-a-project, choose-with-evidence, change-with-a-reason, keep-it-on-course): the skills
decide what the ledger says, and this refuses a change that the ledger cannot account for.

THE LEDGER is two things in the project's repository.

`PROJECT.md` defines IDs in the first cell of Markdown table rows:

    G1   the goal: the change in the world, for whom
    M1   a success measure: what, target, by when, how it is measured
    J1   a journey that must never fail (optional)
    R1   a resource the project needs, and the decision that chose its source, or "owned"
    K1   a course change: when this is measured, the project switches to the route it names
    MS1  a milestone: something a person can use when it is done, and the measures it moves

`decisions/D0001-short-name.md` records one decision each, with front matter:

    ---
    id: D0001
    status: accepted        # proposed, accepted, superseded or rejected
    serves: [M1, J1]        # the IDs this decision exists for
    door: one-way           # one-way (costly to reverse) or two-way
    approved_by: A. Owner  # required for an accepted one-way decision
    revisit: when monthly hosting passes $50, or on 2027-03-01
    superseded_by:          # the decision that replaced it, when superseded
    ---

and the sections `## Options`, `## Evidence` and, for a one-way decision, `## Exit`, whose
list items are counted. Each piece of evidence starts with its kind:

    - Measured: 200 concurrent attempts on one slot gave 1 booking and 199 refusals.
    - Calculation: 50 bookings a day is 18,000 rows a year.

The kinds are Measured, Calculation, Simulation, Proof, Prototype, Test and Source. Every
decision has at least two backings, and at least one of them was verified (every kind but
Source is something someone ran, worked out or built). A two-way decision needs two options;
a one-way decision, which is costly to reverse, needs three options, two different kinds of
evidence, a way out, and a person's name.

A commit says which ID it serves and how it was verified, in two trailer lines:

    Serves: M2
    Verified: bench/pageload.txt, 6.1 s to 1.4 s

A commit that serves nothing, serves a decision that was rejected or replaced, or does not
say how it was verified, is drift.

Every finding is `broken`, with the file and the reason. The last line is the denominator.
This check is written to be able to fail: an empty or missing ledger is refused, not passed.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

KINDS = ("MS", "G", "M", "J", "R", "K")
ID = re.compile(r"\b(?:MS|G|M|J|R|K)\d+\b|\bD\d{4}\b")
ROW_ID = re.compile(r"^\|\s*\**((?:MS|G|M|J|R|K)\d+)\**\s*\|")
DECISION_FILE = re.compile(r"^(D\d{4})-[a-z0-9-]+\.md$")
STATUSES = {"proposed", "accepted", "superseded", "rejected"}
DOORS = {"one-way", "two-way"}
SERVES = re.compile(r"(?im)^serves:\s*(.+)$")
VERIFIED = re.compile(r"(?im)^verified:\s*\S")
EVIDENCE_KINDS = {"measured", "calculation", "simulation", "proof", "prototype", "test", "source"}
EVIDENCE_KIND = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+\**([A-Za-z]+)\**\s*:")
PLACEHOLDER = re.compile(r"^(?:<[^>]*>|tbd|todo|\?|-|—)?$", re.I)


def kind(ident: str) -> str:
    for k in KINDS:
        if ident.startswith(k) and ident[len(k):].isdigit():
            return k
    return "D"


def front_matter(text: str) -> tuple[dict, str]:
    """Flat `key: value` front matter; `[a, b]` becomes a list. Enough for the ledger."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    meta: dict = {}
    for line in text[3:end].splitlines():
        line = line.split(" #", 1)[0].rstrip()
        if ":" not in line or line.startswith("#"):
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            meta[key.strip()] = [v.strip() for v in value[1:-1].split(",") if v.strip()]
        else:
            meta[key.strip()] = value
    return meta, text[end + 4:]


def section_items(body: str, heading: str) -> list[str]:
    """List items under `## <heading>`, up to the next heading of the same or higher level."""
    items: list[str] = []
    inside = False
    for line in body.splitlines():
        match = re.match(r"^(#{1,6})\s+(.*)$", line)
        if match:
            inside = match.group(2).strip().lower() == heading.lower()
            continue
        if inside and re.match(r"^\s*(?:[-*+]|\d+\.)\s+\S", line):
            items.append(line.strip())
    return items


def read_project(root: Path, problems: list[str]) -> dict[str, list[str]]:
    """Every ID PROJECT.md defines, with the cells of the row that defines it."""
    path = root / "PROJECT.md"
    rows: dict[str, list[str]] = {}
    if not path.exists():
        problems.append("PROJECT.md: missing. There is no ledger to trace anything to.")
        return rows
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        match = ROW_ID.match(line)
        if not match:
            continue
        ident = match.group(1)
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if ident in rows:
            problems.append(f"PROJECT.md:{number}: {ident} is defined twice")
        rows[ident] = cells
    return rows


def check_project(rows: dict[str, list[str]], problems: list[str]) -> None:
    by_kind: dict[str, list[str]] = {k: [] for k in KINDS}
    for ident in rows:
        by_kind[kind(ident)].append(ident)
    for k, what in (("G", "a goal"), ("M", "a success measure"), ("K", "a course change "
                    "for when the first route does not work"), ("MS", "a milestone")):
        if not by_kind[k]:
            problems.append(f"PROJECT.md: defines no {k} row, so it has no {what}")
    goals = by_kind["G"]
    for ident in by_kind["M"]:
        cells = rows[ident]
        filled = [c for c in cells[1:] if not PLACEHOLDER.match(c)]
        if len(filled) < 4:
            problems.append(f"PROJECT.md: {ident} needs what is measured, the target, by when "
                            f"and how it is measured; it has {len(filled)} of 4")
        if len(goals) > 1 and not any(g in ID.findall(" ".join(cells[1:])) for g in goals):
            problems.append(f"PROJECT.md: {ident} does not say which goal it measures")
    for ident in by_kind["MS"]:
        refs = ID.findall(" ".join(rows[ident][1:]))
        if not any(kind(r) == "M" for r in refs):
            problems.append(f"PROJECT.md: milestone {ident} moves no measure")
    for ident in by_kind["R"]:
        text = " ".join(rows[ident][1:])
        if not re.search(r"\bD\d{4}\b", text) and not re.search(r"\bowned\b", text, re.I):
            problems.append(f"PROJECT.md: resource {ident} names no decision that chose its "
                            "source, and is not marked owned")


def read_decisions(root: Path, problems: list[str]) -> dict[str, dict]:
    folder = root / "decisions"
    decisions: dict[str, dict] = {}
    if not folder.is_dir():
        return decisions
    for path in sorted(folder.glob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        where = f"decisions/{path.name}"
        match = DECISION_FILE.match(path.name)
        if not match:
            problems.append(f"{where}: name it D0001-short-name.md so it can be referenced")
            continue
        meta, body = front_matter(path.read_text(encoding="utf-8"))
        ident = meta.get("id", "")
        if ident != match.group(1):
            problems.append(f"{where}: id {ident!r} does not match the file name")
            continue
        if ident in decisions:
            problems.append(f"{where}: {ident} is used by two files")
            continue
        decisions[ident] = {"where": where, "meta": meta, "body": body}
    return decisions


def check_decisions(decisions: dict[str, dict], defined: set[str], problems: list[str]) -> None:
    for ident, d in decisions.items():
        where, meta, body = d["where"], d["meta"], d["body"]
        status = meta.get("status", "")
        door = meta.get("door", "")
        if status not in STATUSES:
            problems.append(f"{where}: status {status!r} is not one of {sorted(STATUSES)}")
        if door not in DOORS:
            problems.append(f"{where}: door {door!r} is not one-way or two-way")
        serves = meta.get("serves") or []
        if isinstance(serves, str):
            serves = ID.findall(serves)
        if not serves:
            problems.append(f"{where}: serves nothing, so nothing says why it exists")
        for ref in serves:
            if ref not in defined:
                problems.append(f"{where}: serves {ref}, which the ledger does not define")
        one_way = door == "one-way"
        options = section_items(body, "Options")
        evidence = section_items(body, "Evidence")
        need_options = 3 if one_way else 2
        if len(options) < need_options:
            problems.append(f"{where}: lists {len(options)} option(s); a {door or 'decision'} "
                            f"needs at least {need_options}")
        if len(evidence) < 2:
            problems.append(f"{where}: lists {len(evidence)} piece(s) of evidence; every "
                            "decision needs at least 2 backings")
        kinds = []
        for item in evidence:
            match = EVIDENCE_KIND.match(item)
            kind_word = match.group(1).lower() if match else ""
            if kind_word not in EVIDENCE_KINDS:
                problems.append(f"{where}: evidence {item[:50]!r} does not start with its kind "
                                "(Measured, Calculation, Simulation, Proof, Prototype, Test or "
                                "Source)")
            else:
                kinds.append(kind_word)
        if evidence and kinds and all(k == "source" for k in kinds):
            problems.append(f"{where}: every backing is a source someone else wrote; at least "
                            "one must be measured, calculated, simulated, proved, prototyped "
                            "or tested")
        if one_way and len(set(kinds)) < 2:
            problems.append(f"{where}: one-way with {len(set(kinds))} kind(s) of evidence; it "
                            "needs two different kinds")
        if status == "accepted" and not meta.get("revisit"):
            problems.append(f"{where}: accepted with no revisit condition, so nothing would "
                            "ever reopen it")
        if one_way and not section_items(body, "Exit"):
            problems.append(f"{where}: one-way with no Exit section: what reversing it costs, "
                            "and how")
        if one_way and status == "accepted" and not meta.get("approved_by"):
            problems.append(f"{where}: one-way and accepted with no approved_by: a person "
                            "decides what cannot be undone")
        if status == "superseded":
            by = meta.get("superseded_by", "")
            if by not in decisions:
                problems.append(f"{where}: superseded by {by!r}, which is not a decision here")


def check_commits(root: Path, span: str, defined: set[str], decisions: dict[str, dict],
                  problems: list[str]) -> int:
    try:
        out = subprocess.run(
            ["git", "-C", str(root), "log", "--no-merges", "--format=%h%x1f%s%x1f%B%x1e", span],
            check=True, capture_output=True, text=True,
        ).stdout
    except (OSError, subprocess.CalledProcessError) as error:
        problems.append(f"git log {span}: could not read the commits ({error})")
        return 0
    count = 0
    for record in filter(str.strip, out.split("\x1e")):
        short, subject, message = record.strip().split("\x1f", 2)
        count += 1
        refs = [r for line in SERVES.findall(message) for r in ID.findall(line)]
        label = f"commit {short} ({subject[:60]})"
        if not VERIFIED.search(message):
            problems.append(f"{label}: no Verified: line, so nothing says how it was checked")
        if not refs:
            problems.append(f"{label}: no Serves: line, so nothing says why it was made")
            continue
        for ref in refs:
            if ref not in defined:
                problems.append(f"{label}: serves {ref}, which the ledger does not define")
            elif ref in decisions:
                status = decisions[ref]["meta"].get("status")
                if status != "accepted":
                    problems.append(f"{label}: serves {ref}, which is {status}, not accepted")
    if count == 0:
        problems.append(f"git log {span}: no commits in the range. Refusing to report a pass "
                        "on nothing; check the range.")
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path("."), help="the project (default: .)")
    parser.add_argument("--commits", metavar="RANGE",
                        help="also check every commit in a git range, e.g. origin/main..HEAD")
    args = parser.parse_args()
    root = args.root.resolve()

    problems: list[str] = []
    rows = read_project(root, problems)
    decisions = read_decisions(root, problems)
    defined = set(rows) | set(decisions)
    if rows:
        check_project(rows, problems)
    check_decisions(decisions, defined, problems)

    # A measure that no milestone moves and no accepted decision serves is a promise with no
    # work behind it.
    served = {r for ident in rows if kind(ident) == "MS" for r in ID.findall(" ".join(rows[ident][1:]))}
    for d in decisions.values():
        if d["meta"].get("status") == "accepted":
            serves = d["meta"].get("serves") or []
            served |= set(serves if isinstance(serves, list) else ID.findall(serves))
    for ident in rows:
        if kind(ident) == "M" and ident not in served:
            problems.append(f"PROJECT.md: {ident} is moved by no milestone and served by no "
                            "accepted decision")

    commits = check_commits(root, args.commits, defined, decisions, problems) if args.commits else 0

    for p in problems:
        print(f"broken   {p}")
    checked = len(rows) + len(decisions) + commits
    print(f"{checked} checked ({len(rows)} ledger rows, {len(decisions)} decisions, "
          f"{commits} commits), {len(problems)} broken.")
    return 1 if problems or not rows else 0


if __name__ == "__main__":
    sys.exit(main())
