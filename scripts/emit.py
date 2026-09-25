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
import hashlib
import html
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
PLUGIN_VERSION = "1.2.0"
PLUGIN_AUTHOR = {"name": "Melbin J Paulose", "url": "https://github.com/melbinjp"}
# The words a marketplace, a registry or a search matches on.
PLUGIN_KEYWORDS = [
    "agent-skills", "skill-md", "verification", "production-readiness", "security-review",
    "testing", "ci", "hardware", "physical-world", "claude-code", "codex", "jules",
]
PLUGIN_DESCRIPTION = (
    "Procedures for the failures agents actually have: work that reads as finished "
    "and is not, setup scripts that report success while broken, tests that cannot "
    "fail, pipelines that are green without checking anything, and commands to the "
    "physical world that were accepted but never happened."
)

# The published site, from the file that tells GitHub Pages which domain to serve.
SITE = "https://" + (ROOT / "CNAME").read_text(encoding="utf-8").strip()

# Where an agent finds the skills on the site: the Agent Skills discovery layout
# (github.com/cloudflare/agent-skills-discovery-rfc, v0.2.0), so a client that knows the
# convention needs nothing but the domain.
DISCOVERY = "/.well-known/agent-skills"
DISCOVERY_SCHEMA = "https://schemas.agentskills.io/discovery/0.2.0/schema.json"



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
                # `featured: <n>` in front matter puts a procedure first, in that order, on
                # the site and in llms.txt. One place decides it, for both.
                "featured": meta.get("featured"),
                "body": body.rstrip() + "\n",
                # The original front matter, so a renderer can use it rather
                # than a lossy reconstruction.
                "meta": meta,
            }
        )
    return out


def _described(prompt: dict) -> str:
    """The shared description, so a SKILL.md and the discovery index cannot disagree."""
    return generate_skills.describe(prompt["stem"], prompt["meta"])


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

    Bundling is how agent tooling ships now: a directory with a manifest and its
    skills. Generating it means the bundle cannot drift from the procedures it
    claims to contain, which is the failure this whole repository is about.

    Skills only. The bundle used to carry each procedure a second time as a
    slash command, but Claude Code now loads a plugin's commands as skills too,
    so an install listed all 27 twice (54 entries) and every session paid for
    both descriptions. A skill is already invocable by name as a slash command.
    """
    files = {}
    manifest = {
        "name": PLUGIN_NAME,
        "description": PLUGIN_DESCRIPTION,
        "version": PLUGIN_VERSION,
        "author": PLUGIN_AUTHOR,
        "homepage": SITE + "/",
        "repository": PLUGIN_REPO,
        "license": "MIT",
        "keywords": PLUGIN_KEYWORDS,
    }
    files[".claude-plugin/plugin.json"] = json.dumps(manifest, indent=2) + "\n"

    for prompt in prompts:
        files[f"skills/{prompt['slug']}/SKILL.md"] = emit_skills([prompt])[
            f"{prompt['slug']}/SKILL.md"
        ]
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


def emit_marketplace(prompts: list[dict]) -> dict[str, str]:
    """A marketplace of one, at the repository root, so the bundle installs by name:

        /plugin marketplace add melbinjp/jules-prompts
        /plugin install jules-prompts@jules-prompts

    It is also what plugin directories look for when they index GitHub.
    """
    marketplace = {
        "name": PLUGIN_NAME,
        "owner": PLUGIN_AUTHOR,
        "metadata": {"description": PLUGIN_DESCRIPTION, "version": PLUGIN_VERSION},
        "plugins": [
            {
                "name": PLUGIN_NAME,
                "source": "./plugin",
                "description": PLUGIN_DESCRIPTION,
                "version": PLUGIN_VERSION,
                "author": PLUGIN_AUTHOR,
                "homepage": SITE + "/",
                "repository": PLUGIN_REPO,
                "license": "MIT",
                "keywords": PLUGIN_KEYWORDS,
                "category": "development",
            }
        ],
    }
    return {".claude-plugin/marketplace.json": json.dumps(marketplace, indent=2) + "\n"}


def _skill_text(prompt: dict) -> str:
    return emit_skills([prompt])[f"{prompt['slug']}/SKILL.md"]


def _skill_url(prompt: dict) -> str:
    return f"{SITE}{DISCOVERY}/{prompt['slug']}/SKILL.md"


def emit_agent_skills(prompts: list[dict]) -> dict[str, str]:
    """Each SKILL.md, served by the site byte for byte at its discovery URL.

    GitHub Pages runs Jekyll, and Jekyll turns any `.md` with front matter into HTML, so a
    SKILL.md cannot simply be copied into the site: it would arrive as a page, not a skill.
    Each one is instead wrapped as a plain-text collection document whose permalink is the
    discovery URL. `.txt` has no converter, and `raw` stops Liquid touching the text, so what
    is served is exactly the SKILL.md, and its digest in the index can be checked.
    """
    files = {}
    for prompt in prompts:
        text = _skill_text(prompt)
        if "{% endraw %}" in text or "{%- endraw" in text:
            raise SystemExit(f"{prompt['stem']}: contains endraw, it cannot be served verbatim")
        front = (
            "---\n"
            f"permalink: {DISCOVERY}/{prompt['slug']}/SKILL.md\n"
            "layout: null\n"
            "sitemap: false\n"
            'excerpt_separator: ""\n'
            "---\n"
        )
        files[f"{prompt['slug']}.txt"] = front + "{% raw %}" + text + "{% endraw %}"
    return files


def _line(prompt: dict) -> str:
    return f"- [{prompt['title']}]({_skill_url(prompt)}): {prompt['description']}"


def emit_site(prompts: list[dict]) -> dict[str, str]:
    """The files that let an agent use the site with no prior knowledge of it.

    - `.well-known/agent-skills/index.json`: the discovery index, with the SHA-256 of each
      served SKILL.md, so a client can verify what it loads.
    - `llms.txt`: the same list for an agent that was simply handed the domain.
    - `_includes/workflow-steps.html`: the workflow page's steps, from workflow.json, so the
      page and the JSON cannot drift apart again (they had: four steps against five).
    """
    index = {
        "$schema": DISCOVERY_SCHEMA,
        "skills": [
            {
                "name": p["slug"],
                "type": "skill-md",
                "description": _described(p),
                "url": f"{DISCOVERY}/{p['slug']}/SKILL.md",
                "digest": "sha256:" + hashlib.sha256(_skill_text(p).encode("utf-8")).hexdigest(),
            }
            for p in prompts
        ],
    }

    featured = sorted((p for p in prompts if p["featured"]), key=lambda p: p["featured"])
    if not featured:
        raise SystemExit("no procedure is featured, so llms.txt would have no starting point")
    core = sorted(
        (p for p in prompts if p["status"] == "core" and not p["featured"]),
        key=lambda p: (p["category"], p["title"]),
    )
    legacy = sorted((p for p in prompts if p["status"] == "legacy"), key=lambda p: p["title"])
    llms = "\n".join(
        [
            "# Jules Prompts",
            "",
            "> Agent Skills for the failures agents actually have: work that reads as finished "
            "and is not, setup that reports success while broken, tests that cannot fail, and "
            "commands to the physical world that were accepted but never happened. Each skill "
            "is one self-contained Markdown file in the Agent Skills format, and none depends "
            "on a particular agent or harness.",
            "",
            "To use this site as an agent:",
            "",
            "1. Pick the skill below whose description matches your task.",
            "2. Fetch its SKILL.md and follow it. It needs nothing else from this site.",
            "3. Report every claim as holds, broken or skipped, and end with how many of each.",
            "",
            f"Discovery index, with a SHA-256 digest per skill: {SITE}{DISCOVERY}/index.json",
            f"Standing rules for every task, for a project's AGENTS.md: {SITE}/harness/AGENTS.md",
            "",
            "## Start here",
            "",
            *[_line(p) for p in featured],
            "",
            "## Core skills",
            "",
            *[_line(p) for p in core],
            "",
            "## Optional",
            "",
            *[_line(p) for p in legacy],
            f"- [Source repository]({PLUGIN_REPO}): the procedures, the planted-failure "
            "fixtures that show a skill going red, the scorer, a plugin bundle and an MCP server",
            "",
        ]
    )

    workflow = json.loads((ROOT / "workflow.json").read_text(encoding="utf-8"))
    steps = []
    for step in workflow["steps"]:
        stem = step["prompt_slug"]
        tags = [] if step.get("required") else ["optional"]
        if step.get("repeatable"):
            tags.append("repeat as needed")
        tag_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
        steps.append(
            f'<li class="step">\n'
            f'  <h2><a href="{{{{ "/prompts/{stem}.html" | relative_url }}}}">{html.escape(step["title"])}</a></h2>\n'
            f'  <p>{html.escape(step["description"])}</p>\n'
            + (f"  <p class=\"tags\">{tag_html}</p>\n" if tag_html else "")
            + "</li>"
        )
    steps_html = (
        "<!-- Generated from workflow.json by scripts/emit.py. Edit that, not this. -->\n"
        f'<p class="lede">{html.escape(workflow["description"])}</p>\n'
        '<ol class="steps">\n' + "\n".join(steps) + "\n</ol>\n"
    )

    return {
        f"{DISCOVERY.lstrip('/')}/index.json": json.dumps(index, indent=2) + "\n",
        "llms.txt": llms,
        "_includes/workflow-steps.html": steps_html,
        "_includes/report-exhibit.html": _report_exhibit(),
    }


# The report the home page shows: the expected report of the flagship skill's fixture. It is
# the one thing on the site that shows what the library produces rather than describing it, so
# it is read from the fixture, not retyped, and cannot claim a result the fixture does not.
EXHIBIT_FIXTURE = "looks-finished"
_VERDICT_ROW = re.compile(r"^\|(?P<cells>.+)\|\s*$")
_TOTAL = re.compile(r"^(\d+) holds, (\d+) broken, (\d+) skipped of (\d+) items\.$", re.M)


def _inline(text: str) -> str:
    """Escape a table cell and keep its `code` spans, the only Markdown the cells use."""
    parts = text.split("`")
    return "".join(
        f"<code>{html.escape(part)}</code>" if i % 2 else html.escape(part)
        for i, part in enumerate(parts)
    )


def _report_exhibit() -> str:
    fixtures = json.loads((ROOT / "fixtures" / "index.json").read_text(encoding="utf-8"))
    skill = next(f["skill"] for f in fixtures["fixtures"] if f["name"] == EXHIBIT_FIXTURE)
    report = (ROOT / "fixtures" / EXHIBIT_FIXTURE / "EXPECTED_REPORT.md").read_text(encoding="utf-8")
    table = report.split("## Verdicts", 1)[1]

    rows = []
    for line in table.splitlines():
        match = _VERDICT_ROW.match(line)
        if not match:
            if rows:
                break  # the table has ended
            continue
        cells = [c.strip() for c in match.group("cells").split("|")]
        if cells[0] == "item" or set(cells[0]) <= {"-", ":"}:
            continue
        item, evidence, verdict = cells[0], cells[-2], cells[-1]
        if verdict not in ("holds", "broken", "skipped"):
            raise SystemExit(f"{EXHIBIT_FIXTURE}: verdict {verdict!r} is not holds, broken or skipped")
        rows.append((item, evidence, verdict))

    total = _TOTAL.search(report)
    if not rows or not total:
        raise SystemExit(f"{EXHIBIT_FIXTURE}: no verdict table or no total line in EXPECTED_REPORT.md")
    counts = {v: sum(1 for r in rows if r[2] == v) for v in ("holds", "broken", "skipped")}
    stated = dict(zip(("holds", "broken", "skipped", "items"), map(int, total.groups())))
    if counts != {k: stated[k] for k in counts} or len(rows) != stated["items"]:
        raise SystemExit(f"{EXHIBIT_FIXTURE}: the total line disagrees with the verdict table")

    items = "\n".join(
        f'    <li class="is-{verdict}"><span class="verdict">{verdict}</span>'
        f'<span class="what">{_inline(item)}<small>{_inline(evidence)}</small></span></li>'
        for item, evidence, verdict in rows
    )
    source = f"{PLUGIN_REPO}/tree/main/fixtures/{EXHIBIT_FIXTURE}"
    return (
        f"<!-- Generated from fixtures/{EXHIBIT_FIXTURE}/EXPECTED_REPORT.md by scripts/emit.py. "
        "Edit that, not this. -->\n"
        '<figure class="report" aria-labelledby="report-title">\n'
        '  <figcaption class="report-head">\n'
        '    <span class="report-kicker">Expected report</span>\n'
        f'    <span class="report-title" id="report-title"><code>{skill}</code> on '
        f'<a href="{source}">a notes app that looks finished</a></span>\n'
        "  </figcaption>\n"
        '  <ol class="verdicts">\n'
        f"{items}\n"
        "  </ol>\n"
        f'  <p class="report-total">{html.escape(total.group(0))}</p>\n'
        "</figure>\n"
    )


# name -> (output directory relative to the repo root, renderer)
TARGETS = {
    "skills": ("skills", emit_skills),
    "plugin": ("plugin", emit_plugin),
    "marketplace": (".", emit_marketplace),
    "index": (".", emit_index),
    "agent-skills": ("_agent_skills", emit_agent_skills),
    "site": (".", emit_site),
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
