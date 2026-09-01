#!/usr/bin/env python3
"""Every consumable form of the library, generated from `_prompts/`.

`_prompts/` is the canonical procedure text. Everything an agent actually loads
is generated from it, and every generated form is checked byte for byte against
a fresh generation, so a copy that has drifted fails the build rather than
quietly disagreeing with its source.

That was already true for `skills/`. It is a registry now because the number of
forms an agent ecosystem consumes keeps growing: skills, slash commands,
plugins, subagent definitions, hooks, MCP servers. The shape of this library
does not change when one of those appears. What changes is one entry here.

    python scripts/emit.py                 # write every target
    python scripts/emit.py --check         # exit 1 if any would change
    python scripts/emit.py --target skills # just one
    python scripts/emit.py --list          # what targets exist

**To add a target**, write a function that takes the loaded prompts and returns
`{relative_path: file_text}`, then add it to `TARGETS`. The integrity check
picks it up with no further change, which is the point: the guarantee is not
per-format, it is structural.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate_skills  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PROMPTS = ROOT / "_prompts"

# A golden copy for authors, not a procedure an agent should load.
SKIP = {"template_master_prompt"}

PLUGIN_NAME = "jules-prompts"
PLUGIN_REPO = "https://github.com/melbinjp/jules-prompts"


def split_front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    meta = yaml.safe_load(text[3:end]) or {}
    body = text[end + 4 :].lstrip("\n")
    return meta, body


def slug(stem: str) -> str:
    name = stem.removeprefix("task_").replace("_", "-")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise SystemExit(f"name {name!r} from {stem} is not agentskills-legal")
    if not (1 <= len(name) <= 64):
        raise SystemExit(f"name {name!r} is not 1-64 characters")
    return name


def load_prompts() -> list[dict]:
    """Every canonical procedure, sorted, with its front matter and body."""
    out = []
    for path in sorted(PROMPTS.glob("*.md")):
        if path.stem in SKIP:
            continue
        meta, body = split_front_matter(path.read_text(encoding="utf-8"))
        description = (meta.get("description") or "").strip()
        if not description:
            raise SystemExit(f"{path.name}: no description, it would be unlistable")
        out.append(
            {
                "stem": path.stem,
                "slug": slug(path.stem),
                "title": (meta.get("title") or path.stem).strip(),
                "description": description,
                "category": (meta.get("category") or "").strip(),
                # Absent means core. Only legacy is written down, so the default
                # costs nothing to maintain.
                "status": (meta.get("status") or "core").strip(),
                "body": body.rstrip() + "\n",
                # The original front matter, so a renderer can use it rather
                # than a lossy reconstruction.
                "meta": meta,
            }
        )
    return out


def _described(prompt: dict) -> str:
    """agentskills wants a description that says what and when."""
    description = prompt["description"]
    category = prompt["category"]
    if category and category.lower() not in description.lower():
        description = f"{description} Category: {category}."
    if prompt["status"] == "legacy" and "legacy" not in description.lower():
        description = f"{description} Legacy: general-purpose, kept for completeness."
    return description


# --- targets -----------------------------------------------------------------


def emit_skills(prompts: list[dict]) -> dict[str, str]:
    """Agent Skills, at agentskills.io/specification.

    Delegates to `generate_skills.render_skill` rather than reimplementing the
    format. A second implementation of one output is precisely the drift this
    library is about, and the first draft of this function proved it: its YAML
    wrapped differently and it dropped the `license` and `metadata` keys, so it
    reported all 25 skills as disagreeing with their source when nothing was
    wrong with them.
    """
    files = {}
    for prompt in prompts:
        text = generate_skills.render_skill(prompt["stem"], prompt["meta"], prompt["body"])
        files[f"{prompt['slug']}/SKILL.md"] = text
    return files


def emit_plugin(prompts: list[dict]) -> dict[str, str]:
    """A plugin, so the library installs in one step rather than a copy per skill.

    Bundling is how agent tooling ships now: a directory with a manifest, its
    skills, and its slash commands. Generating it means the bundle cannot drift
    from the procedures it claims to contain, which is the failure this whole
    repository is about.
    """
    files = {}
    manifest = {
        "name": PLUGIN_NAME,
        "description": (
            "Procedures for the failures coding agents actually have: setup scripts that "
            "report success while broken, tests that cannot fail, pipelines that are green "
            "without checking anything, and pull requests that only read as finished."
        ),
        "version": "1.0.0",
        "homepage": PLUGIN_REPO,
        "license": "MIT",
    }
    files[".claude-plugin/plugin.json"] = json.dumps(manifest, indent=2) + "\n"

    for prompt in prompts:
        files[f"skills/{prompt['slug']}/SKILL.md"] = emit_skills([prompt])[
            f"{prompt['slug']}/SKILL.md"
        ]
        # A slash command is the same procedure, invoked by name.
        command = (
            "---\n"
            + yaml.safe_dump(
                {"description": _described(prompt)},
                sort_keys=False,
                allow_unicode=True,
                width=10_000,
            )
            + "---\n\n"
            + f"# {prompt['title']}\n\n"
            + prompt["body"]
        )
        files[f"commands/{prompt['slug']}.md"] = command
    return files


def emit_index(prompts: list[dict]) -> dict[str, str]:
    """One machine-readable list of everything, including which tier it is in."""
    payload = {
        "library": PLUGIN_NAME,
        "source": PLUGIN_REPO,
        "count": len(prompts),
        "procedures": [
            {
                "slug": p["slug"],
                "title": p["title"],
                "description": p["description"],
                "category": p["category"],
                "status": p["status"],
                "prompt": f"_prompts/{p['stem']}.md",
                "skill": f"skills/{p['slug']}/SKILL.md",
            }
            for p in prompts
        ],
    }
    return {"library.json": json.dumps(payload, indent=2) + "\n"}


# name -> (output directory relative to the repo root, renderer)
TARGETS = {
    "skills": ("skills", emit_skills),
    "plugin": ("plugin", emit_plugin),
    "index": (".", emit_index),
}


def render(target: str, prompts: list[dict]) -> dict[Path, str]:
    directory, renderer = TARGETS[target]
    base = ROOT if directory == "." else ROOT / directory
    return {base / relative: text for relative, text in renderer(prompts).items()}


def write(target: str, prompts: list[dict]) -> list[Path]:
    written = []
    for path, text in render(target, prompts).items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or path.read_text(encoding="utf-8") != text:
            path.write_text(text, encoding="utf-8")
        written.append(path)
    return written


def differences(target: str, prompts: list[dict]) -> list[str]:
    """What a fresh generation would change. Empty means the copy is honest."""
    problems = []
    expected = render(target, prompts)
    for path, text in expected.items():
        if not path.exists():
            problems.append(f"{path.relative_to(ROOT)} is missing")
        elif path.read_text(encoding="utf-8") != text:
            problems.append(f"{path.relative_to(ROOT)} differs from its source")

    # A file nobody generates any more is drift in the other direction.
    directory, _ = TARGETS[target]
    if directory != ".":
        base = ROOT / directory
        if base.is_dir():
            for path in base.rglob("*"):
                if path.is_file() and path not in expected and path.name != "README.md":
                    problems.append(f"{path.relative_to(ROOT)} is not generated by any prompt")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="exit 1 if anything would change")
    parser.add_argument("--target", action="append", choices=sorted(TARGETS))
    parser.add_argument("--list", action="store_true", help="list the targets")
    args = parser.parse_args()

    if args.list:
        for name, (directory, _) in sorted(TARGETS.items()):
            print(f"  {name:8} -> {directory}/")
        return 0

    prompts = load_prompts()
    targets = args.target or sorted(TARGETS)

    if args.check:
        problems = [p for t in targets for p in differences(t, prompts)]
        if problems:
            print(f"{len(problems)} generated file(s) disagree with _prompts/:\n")
            for problem in problems:
                print(f"  {problem}")
            print("\nRun: python scripts/emit.py")
            return 1
        print(f"every generated form agrees with _prompts/ ({len(prompts)} procedures)")
        return 0

    for target in targets:
        written = write(target, prompts)
        print(f"{target}: {len(written)} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
