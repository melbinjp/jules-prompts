#!/usr/bin/env python3
"""Generate skills/*/SKILL.md from _prompts/task_*.md.

_prompts/ is the canonical procedure text (Jekyll collection, MCP, website).
skills/ is the same text in the Agent Skills format (agentskills.io), so Claude
Code, Codex, Cursor and anything else that loads SKILL.md can install the
library without pasting. A second copy that can drift is a defect, which is why
check_library_integrity.py refuses a pass when these disagree.

    python scripts/generate_skills.py          # write skills/
    python scripts/generate_skills.py --check  # exit 1 if they would differ
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PROMPTS = ROOT / "_prompts"
SKILLS = ROOT / "skills"

# template_master_prompt.md is a golden copy for authors, not a task an agent
# should load as a skill.
SKIP = {"template_master_prompt"}


def split_front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    meta = yaml.safe_load(text[3:end]) or {}
    body = text[end + 4 :].lstrip("\n")
    return meta, body


def skill_name(stem: str) -> str:
    name = stem.removeprefix("task_").replace("_", "-")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise SystemExit(f"skill name {name!r} from {stem} is not agentskills-legal")
    if not (1 <= len(name) <= 64):
        raise SystemExit(f"skill name {name!r} is not 1-64 characters")
    return name


def render_skill(stem: str, meta: dict, body: str) -> str:
    name = skill_name(stem)
    description = (meta.get("description") or "").strip()
    title = (meta.get("title") or name).strip()
    category = (meta.get("category") or "").strip()
    if not description:
        raise SystemExit(f"{stem}: prompt has no description, skill would be unlistable")
    # agentskills: description says what AND when. Category is the when-hint.
    if category and category.lower() not in description.lower():
        description = f"{description} Category: {category}."
    if len(description) > 1024:
        description = description[:1021] + "..."
    front = {
        "name": name,
        "description": description,
        "license": "MIT",
        "metadata": {
            "prompt_slug": stem,
            "source": f"_prompts/{stem}.md",
            "title": title,
            "category": category,
        },
    }
    dumped = yaml.safe_dump(front, sort_keys=False, allow_unicode=True).rstrip()
    return f"---\n{dumped}\n---\n\n# {title}\n\n{body.rstrip()}\n"


def planned() -> dict[str, str]:
    out: dict[str, str] = {}
    for path in sorted(PROMPTS.glob("task_*.md")):
        if path.stem in SKIP:
            continue
        meta, body = split_front_matter(path.read_text(encoding="utf-8"))
        name = skill_name(path.stem)
        out[name] = render_skill(path.stem, meta, body)
    return out


def write(files: dict[str, str]) -> None:
    SKILLS.mkdir(exist_ok=True)
    wanted = set()
    for name, content in files.items():
        dest = SKILLS / name / "SKILL.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content, encoding="utf-8")
        wanted.add(name)
        print(f"wrote skills/{name}/SKILL.md")
    for child in SKILLS.iterdir():
        if child.is_dir() and child.name not in wanted and (child / "SKILL.md").exists():
            print(f"stale skill directory not in _prompts/: skills/{child.name}/", file=sys.stderr)


def check(files: dict[str, str]) -> int:
    problems: list[str] = []
    for name, content in files.items():
        dest = SKILLS / name / "SKILL.md"
        if not dest.exists():
            problems.append(f"missing skills/{name}/SKILL.md")
            continue
        actual = dest.read_text(encoding="utf-8")
        if actual != content:
            problems.append(f"skills/{name}/SKILL.md disagrees with _prompts/")
    for child in SKILLS.iterdir() if SKILLS.exists() else []:
        if child.is_dir() and (child / "SKILL.md").exists() and child.name not in files:
            problems.append(f"skills/{child.name}/ has no matching _prompts/task_*.md")
    print(f"checked {len(files)} skill(s) against _prompts/")
    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("skills/ agrees with _prompts/")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify, do not write")
    args = parser.parse_args()
    files = planned()
    if not files:
        print("BLIND: no task_*.md prompts found. Refusing to report a pass.")
        return 1
    if args.check:
        return check(files)
    write(files)
    return 0


if __name__ == "__main__":
    sys.exit(main())
