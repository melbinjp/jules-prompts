#!/usr/bin/env python3
"""Fail a schedule that states a date, a quarter or a duration with no source.

Only a heading '## Schedule' is checked. A file with no such section passes,
because it claimed no schedule. Inside the section, each paragraph or table row
is one item.

An item passes when it is 'unscheduled:' with text after the colon and no date,
quarter or duration, or when every such claim sits beside 'committed:',
'measured:' or 'reference class:' and the text after that colon is not empty.
A marker with nothing after the colon fails on its own.

Exit 0 when every file passes, 1 when one fails, 2 when no file was given.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

MARKERS = ("committed:", "measured:", "reference class:", "unscheduled:")
SOURCE_MARKERS = ("committed:", "measured:", "reference class:")
_MONTHS = (
    "January|February|March|April|May|June|July|August|"
    "September|October|November|December"
)
_WORDS = (
    "one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
    "thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|"
    "twenty|thirty|forty|fifty|sixty"
)
_NUMBER = rf"(?:\d+(?:\.\d+)?|{_WORDS})"
CLAIM = re.compile(
    rf"\b\d{{4}}-\d{{2}}-\d{{2}}\b"
    rf"|\b\d{{1,2}}(?:st|nd|rd|th)?\s+(?:{_MONTHS})\b"
    rf"|\b(?:{_MONTHS})\s+\d{{1,2}}(?:st|nd|rd|th)?\b"
    rf"|\bQ[1-4]\b"
    rf"|\b{_NUMBER}\s+(?:working\s+|calendar\s+)?(?:minutes?|hours?|days?|weeks?|months?|years?)\b",
    re.IGNORECASE,
)
_HEADING = re.compile(r"^##\s+Schedule\s*$", re.M)
_NEXT = re.compile(r"^##\s+\S", re.M)
_MARKER = re.compile(r"(?<![\w])(?:" + "|".join(re.escape(m) for m in MARKERS) + r")")
_RULE = re.compile(r"^\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$")


def schedule_section(text: str) -> str | None:
    match = _HEADING.search(text)
    if not match:
        return None
    rest = text[match.end():]
    if rest.startswith("\n"):
        rest = rest[1:]
    nxt = _NEXT.search(rest)
    return rest[: nxt.start()] if nxt else rest


def items_of(section: str) -> list[str]:
    found: list[str] = []
    for block in re.split(r"\n\s*\n", section.strip()):
        rows = [line for line in block.splitlines() if line.strip()]
        if rows and all(line.strip().startswith("|") for line in rows):
            for line in rows:
                if _RULE.fullmatch(line.strip()):
                    continue
                found.append(line.strip())
        elif block.strip():
            found.append(block.strip())
    return found


def _bodies(item: str) -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    matches = list(_MARKER.finditer(item))
    for index, match in enumerate(matches):
        marker = match.group(0)
        end = matches[index + 1].start() if index + 1 < len(matches) else len(item)
        body = item[match.end():end]
        body = body.strip().strip("|").strip()
        found.append((marker, body))
    return found


def check_text(text: str) -> list[str]:
    section = schedule_section(text)
    if section is None:
        return []
    problems: list[str] = []
    for item in items_of(section):
        bodies = _bodies(item)
        claims = [match.group(0) for match in CLAIM.finditer(item)]
        for marker, body in bodies:
            if not body:
                problems.append(f"empty source after {marker!r}")
        sourced = any(marker in SOURCE_MARKERS and body for marker, body in bodies)
        unscheduled = any(marker == "unscheduled:" for marker, _ in bodies)
        if unscheduled and claims:
            for claim in claims:
                problems.append(f"unscheduled item also states {claim!r}")
        elif claims and not sourced:
            for claim in claims:
                problems.append(f"unsourced time limit: {claim!r}")
    return problems


def check_file(path: Path) -> list[str]:
    if not path.is_file():
        return [f"not a file: {path}"]
    return check_text(path.read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="Markdown files whose ## Schedule section is checked")
    args = parser.parse_args(argv)
    failed = False
    for path in args.paths:
        problems = check_file(path)
        for problem in problems:
            print(f"{path}: {problem}")
            failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
