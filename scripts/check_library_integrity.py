"""Does this library agree with itself?

    python scripts/check_library_integrity.py

`prompts.json` is fetched by agents rather than read by people, and `PROMPTS_GUIDE.md` is
what a human reads first. The README asks for the prompt set, the guide, and the workflow to
stay aligned. Nothing checked that they did, and they had already drifted:
`task_build_api_frontend` shipped with a prompt file and no guide entry.

That is a small gap with an awkward property. A library whose own index is incomplete is
making a claim it cannot support, and this one is specifically sold as machine-readable, so
the index is the product rather than documentation about it.

**This check is written to be able to fail.** No step in it swallows an exit code and there
is no `continue-on-error` on the workflow that runs it. A verification that cannot fail is
indistinguishable from one that was never run.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS = ROOT / "_prompts"
GUIDE = ROOT / "PROMPTS_GUIDE.md"
WORKFLOW = ROOT / "workflow.json"

# Every prompt carries YAML front matter, and `prompts.json` is generated from these fields.
# A missing one renders as an empty string in the JSON rather than an error, which is the
# quiet kind of breakage this file exists to make loud.
REQUIRED_FIELDS = ("layout", "title", "description", "category", "type")

GUIDE_ENTRY = re.compile(r"^### \[`([a-z0-9_]+)\.md`\]", re.M)
FIELD = re.compile(r"^([a-z_]+):", re.M)


def front_matter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end]
    return {m.group(1): True for m in FIELD.finditer(block)}


def main() -> int:
    problems: list[str] = []

    files = sorted(p.stem for p in PROMPTS.glob("*.md"))
    if not files:
        print("BLIND: no prompt files found at all. Refusing to report a pass.")
        return 1

    guide = GUIDE.read_text(encoding="utf-8")
    documented = sorted(set(GUIDE_ENTRY.findall(guide)))

    for slug in files:
        if slug not in documented:
            problems.append(f"{slug}.md has no entry in PROMPTS_GUIDE.md")
    for slug in documented:
        if slug not in files:
            problems.append(f"PROMPTS_GUIDE.md documents {slug}.md, which does not exist")

    for p in sorted(PROMPTS.glob("*.md")):
        fm = front_matter(p.read_text(encoding="utf-8"))
        if not fm:
            problems.append(f"{p.name} has no YAML front matter, so it will not render")
            continue
        for field in REQUIRED_FIELDS:
            if field not in fm:
                problems.append(f"{p.name} front matter is missing '{field}'")

    steps = json.loads(WORKFLOW.read_text(encoding="utf-8"))["steps"]
    for s in steps:
        if s["prompt_slug"] not in files:
            problems.append(f"workflow.json step {s['order']} points at "
                            f"{s['prompt_slug']}, which is not in _prompts/")
    orders = [s["order"] for s in steps]
    if orders != list(range(1, len(steps) + 1)):
        problems.append(f"workflow.json step orders are {orders}, not 1..{len(steps)}")

    # Say what was READ, not only what was wrong. A check that reports "OK" without its
    # coverage cannot be told apart from one whose globs stopped matching.
    print(f"checked {len(files)} prompt(s), {len(documented)} guide entry(ies), "
          f"{len(steps)} workflow step(s)")
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("the prompt set, the guide and the workflow agree")
    return 0


if __name__ == "__main__":
    sys.exit(main())
