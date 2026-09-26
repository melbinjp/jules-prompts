#!/usr/bin/env python3
"""Inventory every item of the current system, and check that the coverage map lists each one.

    python scripts/inventory_map.py              # check docs/migration/coverage-map.md
    python scripts/inventory_map.py --list       # every item: its ID and its text
    python scripts/inventory_map.py --counts     # how many items each source has
    python scripts/inventory_map.py --destinations   # also check each destination section exists

WHAT IT IS FOR. The conductor replaces 26 skills, the harness and the fixtures. Before anything
is removed, every rule, procedure and failure case in them must be mapped to where it now lives,
or given a reason for its removal. This lists them all, so none can be forgotten.

WHAT IT IS NOT. It is an inventory aid. It proves that every item is named in the map, not that
the item's meaning survived the move: syntax coverage is not behaviour coverage. The mapping and
every removal reason are reviewed by a person.

WHAT IT READS. Everything is read from the frozen baseline commit, not the working tree, so the
inventory cannot drift while the conductor is written or after the old files are removed.

ITEMS, AND THEIR IDS.
    <skill>.role                 the Role paragraph of a skill
    <skill>.<S><n>               the n-th paragraph or list item of section S: O objective,
                                 C context, R requirements, G guiding principles, E execution
                                 flow, D deliverables
    workflow.step<n> / .entry<n> / .throughout<n>     workflow.json
    agents.<section>.<n>         each paragraph or bullet of harness/AGENTS.md
    trace.L<line>                each finding harness/check_trace.py can raise
    conformance.<n>              each property harness/conformance.py checks
    ledger-example.<file>        each file of the worked ledger example
    fixture.<name>.<defect>      each planted defect
    owner.<n>                    each row of QUALITY.md's "What the owner asked for" table

THE MAP. Markdown tables whose first cell holds one or more IDs (comma-separated; a range such as
`start-from-an-idea.R3-R7` covers R3 to R7), whose second cell says where the item lands, and
whose third cell says how. A row whose destination is `removed` needs its reason in the third
cell. With --destinations, a destination written as `path §Heading` must name a heading that
exists in that file.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASELINE = "f5fc9c0e721f4323f4ee79554220bb76128f796d"
MAP = ROOT / "docs" / "migration" / "coverage-map.md"

SECTIONS = {
    "Role": "role", "Objective": "O", "Context": "C", "Requirements & Constraints": "R",
    "Guiding Principles": "G", "Execution Flow": "E", "Deliverables": "D",
}
SECTION_LINE = re.compile(r"^\*\*(" + "|".join(re.escape(s) for s in SECTIONS) + r"):\*\*\s*(.*)$")
LIST_ITEM = re.compile(r"^(\s*)(?:[*+-]|\d+\.)\s+(.*)$")
RANGE = re.compile(r"^(?P<prefix>.+\.)(?P<code>[A-Za-z]*)(?P<start>\d+)-(?:[A-Za-z]+)?(?P<end>\d+)$")


def show(path: str) -> str:
    return subprocess.run(["git", "show", f"{BASELINE}:{path}"], cwd=ROOT, check=True,
                          capture_output=True, text=True).stdout


def tracked(prefix: str) -> list[str]:
    out = subprocess.run(["git", "ls-tree", "-r", "--name-only", BASELINE, prefix], cwd=ROOT,
                         check=True, capture_output=True, text=True).stdout
    return sorted(line for line in out.splitlines() if line)


def skill_slug(path: str) -> str:
    stem = Path(path).stem
    if stem.startswith("task_"):
        return stem[len("task_"):].replace("_", "-")
    return stem.replace("_", "-")


def blocks(lines: list[str]) -> list[str]:
    """Paragraphs and list items, each with its continuation lines, in order."""
    out: list[str] = []
    current: list[str] = []
    for line in lines:
        if not line.strip():
            if current:
                out.append(" ".join(current))
                current = []
            continue
        if LIST_ITEM.match(line):
            if current:
                out.append(" ".join(current))
            current = [LIST_ITEM.match(line).group(2).strip()]
        else:
            current.append(line.strip())
    if current:
        out.append(" ".join(current))
    return [b for b in out if b]


def skill_items(path: str) -> list[tuple[str, str]]:
    text = show(path)
    if text.startswith("---"):
        text = text.split("---", 2)[2]
    slug = skill_slug(path)
    by_section: dict[str, list[str]] = {}
    section = None
    for line in text.splitlines():
        m = SECTION_LINE.match(line)
        if m:
            section = SECTIONS[m.group(1)]
            by_section.setdefault(section, [])
            if m.group(2):
                by_section[section].append(m.group(2))
            continue
        if section:
            by_section[section].append(line)
    items = []
    for code, lines in by_section.items():
        found = blocks(lines)
        if code == "role":
            items.append((f"{slug}.role", " ".join(found)))
            continue
        for n, block in enumerate(found, 1):
            items.append((f"{slug}.{code}{n}", block))
    return items


def workflow_items() -> list[tuple[str, str]]:
    data = json.loads(show("workflow.json"))
    items = [(f"workflow.step{s['order']}", f"{s['title']}: done when {s['done_when']}")
             for s in data["steps"]]
    items += [(f"workflow.entry{n}", f"{e['state']} -> {e['start']}: {e['note']}")
              for n, e in enumerate(data["entries"], 1)]
    items += [(f"workflow.throughout{n}", f"{t['when']} -> {t['skill']}")
              for n, t in enumerate(data["throughout"], 1)]
    return items


def agents_items() -> list[tuple[str, str]]:
    text = show("harness/AGENTS.md")
    parts = re.split(r"^## (.+)$", text, flags=re.M)
    items = []
    for heading, body in zip(parts[1::2], parts[2::2]):
        key = re.sub(r"[^a-z0-9]+", "-", heading.lower()).strip("-")
        for n, block in enumerate(blocks(body.splitlines()), 1):
            items.append((f"agents.{key}.{n}", block))
    return items


def trace_items() -> list[tuple[str, str]]:
    items = []
    for number, line in enumerate(show("harness/check_trace.py").splitlines(), 1):
        if "problems.append(" in line:
            items.append((f"trace.L{number}", line.split("problems.append(", 1)[1].strip()))
    return items


def conformance_items() -> list[tuple[str, str]]:
    names = re.findall(r'expect\("([^"]+)"', show("harness/conformance.py"))
    return [(f"conformance.{n}", name) for n, name in enumerate(names, 1)]


def ledger_items() -> list[tuple[str, str]]:
    return [(f"ledger-example.{Path(p).name}", p) for p in tracked("harness/ledger-example")]


def fixture_items() -> list[tuple[str, str]]:
    items = []
    for path in tracked("fixtures"):
        if path.endswith("/defects.json"):
            data = json.loads(show(path))
            for defect in data["defects"]:
                items.append((f"fixture.{data['fixture']}.{defect['id']}", defect["tell"]))
    return items


def owner_items() -> list[tuple[str, str]]:
    text = show("QUALITY.md")
    section = text.split("## What the owner asked for", 1)[1].split("\n## ", 1)[0]
    rows = [line for line in section.splitlines() if line.startswith("| ") and "---" not in line]
    return [(f"owner.{n}", row.split("|")[1].strip()) for n, row in enumerate(rows[1:], 1)]


def inventory() -> list[tuple[str, str]]:
    items = []
    for path in tracked("_prompts"):
        if path.endswith(".md"):
            items += skill_items(path)
    items += workflow_items() + agents_items() + trace_items() + conformance_items()
    items += ledger_items() + fixture_items() + owner_items()
    ids = [i for i, _ in items]
    duplicates = {i for i in ids if ids.count(i) > 1}
    if duplicates:
        raise SystemExit(f"duplicate inventory IDs: {sorted(duplicates)}")
    return items


def expand(cell: str) -> list[str]:
    out = []
    for part in cell.replace("`", "").split(","):
        part = part.strip()
        if not part:
            continue
        m = RANGE.match(part)
        if m:
            for n in range(int(m.group("start")), int(m.group("end")) + 1):
                out.append(f"{m.group('prefix')}{m.group('code')}{n}")
        else:
            out.append(part)
    return out


def map_rows(text: str) -> list[tuple[int, list[str], str, str]]:
    rows = []
    for number, line in enumerate(text.splitlines(), 1):
        if not line.startswith("|") or re.match(r"^\|\s*-", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or cells[0].lower() in {"id", "ids", "items", "item"}:
            continue
        rows.append((number, expand(cells[0]), cells[1], cells[2]))
    return rows


def headings(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {m.group(1).strip() for m in re.finditer(r"^#+\s+(.+)$", path.read_text(), re.M)}


def check(destinations: bool) -> int:
    items = dict(inventory())
    if not MAP.exists():
        print(f"broken: {MAP.relative_to(ROOT)} does not exist")
        return 1
    problems = []
    mapped = set()
    for number, ids, where, how in map_rows(MAP.read_text()):
        for ident in ids:
            if ident not in items:
                problems.append(f"coverage-map.md:{number}: {ident} is not an item in the inventory")
            mapped.add(ident)
        if not where or where.lower() in {"tbd", "todo", "?", "-"}:
            problems.append(f"coverage-map.md:{number}: no destination")
        if where.lower().startswith("removed") and len(how) < 12:
            problems.append(f"coverage-map.md:{number}: removed with no reason")
        if destinations and "§" in where:
            for target in where.split(";"):
                if "§" not in target:
                    continue
                path, heading = (s.strip().strip("`") for s in target.split("§", 1))
                if heading not in headings(ROOT / path):
                    problems.append(f"coverage-map.md:{number}: {path} has no heading {heading!r}")
    missing = [i for i in items if i not in mapped]
    for ident in missing:
        problems.append(f"unmapped: {ident}: {items[ident][:90]}")
    for problem in problems:
        print(f"broken: {problem}")
    print(f"{len(items) - len(missing)} of {len(items)} items mapped, {len(problems)} problems.")
    return 1 if problems else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--list", action="store_true", help="print every item")
    parser.add_argument("--counts", action="store_true", help="print how many items each source has")
    parser.add_argument("--destinations", action="store_true",
                        help="also check that each `path §Heading` destination exists")
    args = parser.parse_args()
    if args.list:
        for ident, text in inventory():
            print(f"{ident}\t{text}")
        return 0
    if args.counts:
        counts: dict[str, int] = {}
        for ident, _ in inventory():
            counts[ident.split(".")[0]] = counts.get(ident.split(".")[0], 0) + 1
        for source, n in counts.items():
            print(f"{n:5d}  {source}")
        print(f"{sum(counts.values()):5d}  total")
        return 0
    return check(args.destinations)


if __name__ == "__main__":
    sys.exit(main())
