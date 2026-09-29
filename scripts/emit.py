#!/usr/bin/env python3
"""Every consumable form of the conductor, generated from `conductor/`.

`conductor/` is the one procedure source: `SKILL.md`, `guidance/` and `templates/`, written
by hand. Everything an agent or a person actually loads is generated from it, and every
generated form is checked byte for byte against a fresh generation, so a copy that has drifted
fails the build rather than quietly disagreeing with its source.

    python scripts/emit.py                 # write every target
    python scripts/emit.py --check         # exit 1 if any would change
    python scripts/emit.py --target skills # just one
    python scripts/emit.py --list          # what targets exist

**To add a target**, write a function that takes the loaded package and returns
`{relative_path: file_text_or_bytes}`, then add it to `TARGETS`. The integrity check and the
byte tests pick it up with no further change, which is the point: the guarantee is not
per-format, it is structural.

Every file is written as exact UTF-8 with LF line endings (the archive as fixed bytes), so a
digest published for a file is the digest of what any checkout produces.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import io
import json
import re
import sys
import zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PACKAGE = ROOT / "conductor"

PLUGIN_NAME = "jules-prompts"
SKILL_NAME = "conductor"
PLUGIN_REPO = "https://github.com/melbinjp/jules-prompts"
PLUGIN_VERSION = "3.0.0"
PLUGIN_AUTHOR = {"name": "Melbin J Paulose", "url": "https://github.com/melbinjp"}
# The words a marketplace, a registry or a search matches on.
PLUGIN_KEYWORDS = [
    "agent-skills", "skill-md", "project-delivery", "verification", "project-management",
    "decision-records", "production-readiness", "hardware", "physical-world", "claude-code",
    "codex", "jules",
]
PLUGIN_DESCRIPTION = (
    "One entry point for delivering any project, software, physical, service or hybrid, from "
    "nothing or from any existing state to an accepted result, and for handing over whatever "
    "must keep running. It loads focused guidance only when the work needs it, and counts "
    "nothing as done without evidence about the actual result."
)

# The published site, from the file that tells GitHub Pages which domain to serve.
SITE = "https://" + (ROOT / "CNAME").read_text(encoding="utf-8").strip()

# Where an agent finds the conductor on the site: the Agent Skills discovery layout
# (github.com/cloudflare/agent-skills-discovery-rfc, v0.2.0), so a client that knows the
# convention needs nothing but the domain. The conductor is a folder, so the index lists it as
# an `archive`; the same files are also served one by one, byte for byte.
DISCOVERY = "/.well-known/agent-skills"
DISCOVERY_SCHEMA = "https://schemas.agentskills.io/discovery/0.2.0/schema.json"
ARCHIVE_URL = f"{DISCOVERY}/{SKILL_NAME}.zip"
PAGES = "/conductor"

Files = dict  # relative path -> text, or bytes for the archive


def split_front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    meta = yaml.safe_load(text[3:end]) or {}
    body = text[end + 4 :].lstrip("\n")
    return meta, body


def as_bytes(content: str | bytes) -> bytes:
    return content if isinstance(content, bytes) else content.encode("utf-8")


def sha256(content: str | bytes) -> str:
    return "sha256:" + hashlib.sha256(as_bytes(content)).hexdigest()


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


# --- the package ------------------------------------------------------------------


def _summary(body: str) -> str:
    """The first paragraph after the title, as one plain sentence or two."""
    lines = body.split("\n")
    at = next((i for i, line in enumerate(lines) if line.startswith("# ")), -1)
    paragraph: list[str] = []
    for line in lines[at + 1 :]:
        if not line.strip():
            if paragraph:
                break
            continue
        if line.startswith(("#", "|", "```")):
            break
        paragraph.append(line.strip())
    text = " ".join(paragraph).replace("`", "").replace("*", "")
    # A pointer to another file is for a reader in the package; in a description it is noise.
    text = re.sub(r"\s*\([^()]*\.md[^()]*\)", "", text)
    # Sentences end at a full stop after a word or bracket and before a capital, outside brackets.
    sentences, start, depth = [], 0, 0
    for i, ch in enumerate(text):
        depth += (ch == "(") - (ch == ")")
        if (ch == "." and depth == 0 and i > 0 and (text[i - 1].isalpha() or text[i - 1] == ")")
                and text[i + 1 : i + 3].strip() and text[i + 1] == " " and text[i + 2].isupper()):
            sentences.append(text[start : i + 1])
            start = i + 2
    sentences.append(text[start:])
    out = sentences[0]
    for extra in sentences[1:]:
        if len(out) + len(extra) + 1 > 280 or ".md" in extra:
            break
        out += " " + extra
    return out


def load_package() -> list[dict]:
    """Every file of the conductor, in reading order, with the facts each form needs."""
    if not (PACKAGE / "SKILL.md").is_file():
        raise SystemExit(f"{PACKAGE / 'SKILL.md'} is missing")
    texts: dict[str, str] = {}
    for path in sorted(PACKAGE.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(PACKAGE).as_posix()
        text = path.read_bytes().decode("utf-8")
        if "\r" in text:
            raise SystemExit(f"conductor/{rel} has CR characters; the package is LF only, so "
                             "published digests are the same on every platform")
        texts[rel] = text

    entry_meta, _ = split_front_matter(texts["SKILL.md"])
    if entry_meta.get("name") != SKILL_NAME or not (entry_meta.get("description") or "").strip():
        raise SystemExit("conductor/SKILL.md needs name 'conductor' and a description")

    # The order guidance is listed in is the order SKILL.md's loading table gives.
    table = texts["SKILL.md"].split("## Guidance to load", 1)[-1]

    def rank(rel: str) -> tuple[int, str]:
        at = table.find(f"`{rel}`")
        return (at if at >= 0 else len(table), rel)

    ordered = ["SKILL.md"]
    for prefix in ("guidance/", "templates/"):
        ordered += sorted((r for r in texts if r.startswith(prefix)), key=rank)
    unexpected = sorted(set(texts) - set(ordered))
    if unexpected:
        raise SystemExit(f"conductor/ holds files outside SKILL.md, guidance/ and templates/: {unexpected}")

    docs = []
    for rel in ordered:
        text = texts[rel]
        if rel == "SKILL.md":
            meta, body = split_front_matter(text)
            description = meta["description"].strip()
            kind, name, page = "skill", SKILL_NAME, f"{PAGES}/"
        else:
            body = text
            kind = rel.split("/", 1)[0].removesuffix("s")  # guidance, template
            stem = rel.rsplit("/", 1)[-1].removesuffix(".md")
            name = f"{SKILL_NAME}-{kind}-{stem}"
            description = _summary(body)
            page = f"{PAGES}/{rel.removesuffix('.md')}.html"
        title = next((l[2:].strip() for l in body.split("\n") if l.startswith("# ")), None)
        if not title or not description:
            raise SystemExit(f"conductor/{rel}: needs a title and a first paragraph")
        docs.append({
            "path": rel,
            "kind": kind,
            "name": name,
            "title": title,
            "description": description,
            "body": body,
            "text": text,
            "page": page,
            "source": f"{DISCOVERY}/{SKILL_NAME}/{rel}",
        })
    if len(docs[0]["description"]) > 1024:
        raise SystemExit("the conductor's description is over 1024 characters, the Agent Skills limit")
    return docs


def _entry(docs: list[dict]) -> dict:
    return docs[0]


# --- targets -----------------------------------------------------------------------


def emit_skills(docs: list[dict]) -> Files:
    """The conductor as an Agent Skill folder, an exact copy of the package."""
    return {f"{SKILL_NAME}/{d['path']}": d["text"] for d in docs}


def emit_plugin(docs: list[dict]) -> Files:
    """The Claude Code plugin: a manifest and the conductor folder, so it installs in one step.

    Bundling is how agent tooling ships now. Generating the bundle means it cannot drift from the
    procedure it claims to contain, which is the failure this whole repository is about.
    """
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
    files: Files = {".claude-plugin/plugin.json": json.dumps(manifest, indent=2) + "\n"}
    for d in docs:
        files[f"skills/{SKILL_NAME}/{d['path']}"] = d["text"]
    return files


def emit_marketplace(docs: list[dict]) -> Files:
    """A marketplace of one, at the repository root, so the plugin installs by name:

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


def emit_index(docs: list[dict]) -> Files:
    """The MCP server's index (`library.json`) and the older list some clients read.

    Every file of the conductor is listed with the SHA-256 of its bytes, so a client can verify
    what it loaded, including SKILL.md.
    """
    label = {"skill": "Conductor", "guidance": "Guidance", "template": "Template"}
    library = {
        "library": PLUGIN_NAME,
        "source": PLUGIN_REPO,
        "entry": SKILL_NAME,
        "version": PLUGIN_VERSION,
        "count": len(docs),
        "files": [
            {
                "name": d["name"],
                "kind": d["kind"],
                "title": d["title"],
                "description": d["description"],
                "path": f"conductor/{d['path']}",
                "digest": sha256(d["text"]),
            }
            for d in docs
        ],
    }
    prompts = {
        "version": "3.0",
        "repository": PLUGIN_REPO,
        "documentation": SITE + "/",
        "skills_index": f"{SITE}{DISCOVERY}/index.json",
        "total_prompts": len(docs),
        "categories": [label[k] for k in ("skill", "guidance", "template")],
        "prompts": [
            {
                "slug": d["name"],
                "title": d["title"],
                "description": d["description"],
                "category": label[d["kind"]],
                "url": d["page"],
                "skill": d["source"],
                "source_path": f"conductor/{d['path']}",
            }
            for d in docs
        ],
    }
    return {
        "library.json": json.dumps(library, indent=2) + "\n",
        "prompts.json": json.dumps(prompts, indent=2) + "\n",
    }


def emit_agent_skills(docs: list[dict]) -> Files:
    """Each file of the conductor, served by the site byte for byte at its discovery URL.

    GitHub Pages runs Jekyll, and Jekyll turns any `.md` with front matter into HTML, so a
    SKILL.md cannot simply be copied into the site: it would arrive as a page, not a skill.
    Each file is instead wrapped as a plain-text collection document whose permalink is the
    discovery URL. `.txt` has no converter, and `raw` stops Liquid touching the text, so what
    is served is exactly the source file, and its digest can be checked.
    """
    files: Files = {}
    for d in docs:
        if "{% endraw %}" in d["text"] or "{%- endraw" in d["text"]:
            raise SystemExit(f"conductor/{d['path']}: contains endraw, it cannot be served verbatim")
        front = (
            "---\n"
            f"permalink: {d['source']}\n"
            "layout: null\n"
            "sitemap: false\n"
            'excerpt_separator: ""\n'
            "---\n"
        )
        files[f"{SKILL_NAME}/{d['path'].removesuffix('.md')}.txt"] = front + "{% raw %}" + d["text"] + "{% endraw %}"
    return files


def build_archive(docs: list[dict]) -> bytes:
    """The conductor folder as a zip that is the same bytes on every platform and Python.

    Stored, not compressed: the compressed bytes of a file depend on the zlib in use, and a
    digest that changes with the machine that built it verifies nothing. Files sit at the
    archive root (the discovery format's layout), in reading order, with a fixed time and mode.
    """
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_STORED) as archive:
        for d in docs:
            info = zipfile.ZipInfo(d["path"], date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_STORED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, d["text"].encode("utf-8"))
    return buffer.getvalue()


def emit_archive(docs: list[dict]) -> Files:
    return {ARCHIVE_URL.lstrip("/"): build_archive(docs)}


def _line(d: dict) -> str:
    return f"- [{d['title']}]({SITE}{d['source']}): {d['description']}"


def emit_site(docs: list[dict]) -> Files:
    """The files that let an agent use the site with no prior knowledge of it.

    - `.well-known/agent-skills/index.json`: the discovery index, with the SHA-256 of the archive
      of the whole conductor folder, so a client can verify what it loads.
    - `llms.txt`: the same, for an agent that was simply handed the domain, with a link to every file.
    - `_includes/`: the guidance list, the control loop and the report the pages show, each read
      from the conductor or a fixture so the pages cannot claim what the sources do not say.
    """
    entry = _entry(docs)
    archive = build_archive(docs)
    index = {
        "$schema": DISCOVERY_SCHEMA,
        "skills": [
            {
                "name": SKILL_NAME,
                "type": "archive",
                "description": entry["description"],
                "url": ARCHIVE_URL,
                "digest": sha256(archive),
            }
        ],
    }
    guidance = [d for d in docs if d["kind"] == "guidance"]
    templates = [d for d in docs if d["kind"] == "template"]
    llms = "\n".join(
        [
            "# Jules Prompts",
            "",
            f"> The conductor: {entry['description'][0].lower()}{entry['description'][1:]}",
            "",
            "To use it as an agent:",
            "",
            "1. Get the whole folder: the archive below, or SKILL.md and every file it tells you to load. "
            "SKILL.md alone is incomplete, because it refers to the guidance and templates.",
            "2. Read SKILL.md whole and follow it. Load one guidance file at a time, and only the "
            "sections the current work needs, when the context window is small.",
            "3. End every report with its counts: verified, failed, not verified and not applicable.",
            "",
            f"The whole folder as one archive (zip, SKILL.md at its root): {SITE}{ARCHIVE_URL}",
            f"SHA-256 of that archive: {sha256(archive)}",
            f"Discovery index (Agent Skills 0.2.0): {SITE}{DISCOVERY}/index.json",
            f"SHA-256 of SKILL.md: {sha256(entry['text'])}",
            f"Every file with its SHA-256: {SITE}/library.json",
            "",
            "## The conductor",
            "",
            _line(entry),
            "",
            "## Guidance",
            "",
            *[_line(d) for d in guidance],
            "",
            "## Templates",
            "",
            *[_line(d) for d in templates],
            "",
            "## Optional",
            "",
            f"- [Standing rules for a project's AGENTS.md]({SITE}/harness/AGENTS.md): short rules that "
            "apply on every task, pointing at the conductor",
            f"- [The ledger check]({SITE}/harness/check_trace.py): for projects that already keep the "
            "older ledger (Python, no dependencies)",
            f"- [The test a self-built agent harness must pass]({SITE}/harness/conformance.py): "
            "Python and git, nothing else",
            f"- [Source repository]({PLUGIN_REPO}): the conductor, its regression fixtures with planted "
            "defects, the scorer, a plugin bundle and an MCP server",
            "",
        ]
    )
    return {
        f"{DISCOVERY.lstrip('/')}/index.json": json.dumps(index, indent=2) + "\n",
        "llms.txt": llms,
        "_includes/conductor-guidance.html": _guidance_list(docs),
        "_includes/conductor-loop.html": _loop_list(docs),
        "_includes/report-exhibit.html": _report_exhibit(),
    }


def _guidance_list(docs: list[dict]) -> str:
    items = "\n".join(
        f'  <li><a href="{{{{ "{d["page"]}" | relative_url }}}}">{html.escape(d["title"])}</a>\n'
        f"    <p>{html.escape(d['description'])}</p></li>"
        for d in docs
        if d["kind"] == "guidance"
    )
    return (
        "<!-- Generated from conductor/ by scripts/emit.py. Edit that, not this. -->\n"
        f'<ul class="skill-list">\n{items}\n</ul>\n'
    )


def _loop_list(docs: list[dict]) -> str:
    """The control loop's eight responsibilities, as SKILL.md states them."""
    body = _entry(docs)["body"]
    loop = body.split("## 2. The control loop", 1)[1].split("\n## ", 1)[0]
    steps = re.findall(r"^\d+\.\s+\*\*(.+?)\*\*", loop, re.M)
    if len(steps) < 3:
        raise SystemExit("conductor/SKILL.md: no numbered control loop to show on the home page")
    items = "\n".join(f"  <li>{html.escape(step.rstrip('.'))}</li>" for step in steps)
    return (
        "<!-- Generated from conductor/SKILL.md by scripts/emit.py. Edit that, not this. -->\n"
        f'<ol class="path">\n{items}\n</ol>\n'
    )


# The report the home page shows: the expected report of the flagship fixture. It is the one
# thing on the site that shows what the conductor is held to rather than describing it, so it is
# read from the fixture, not retyped, and cannot claim a result the fixture does not.
EXHIBIT_FIXTURE = "looks-finished"
_VERDICT_ROW = re.compile(r"^\|(?P<cells>.+)\|\s*$")
_TOTAL = re.compile(r"^(\d+) holds, (\d+) broken, (\d+) skipped of (\d+) items\.$", re.M)
# The fixtures score with the scorer's three words; the conductor reports in plain terms.
TERMS = {"holds": "verified", "broken": "failed", "skipped": "not verified"}


def _inline(text: str) -> str:
    """Escape a table cell and keep its `code` spans, the only Markdown the cells use."""
    parts = text.split("`")
    return "".join(
        f"<code>{html.escape(part)}</code>" if i % 2 else html.escape(part)
        for i, part in enumerate(parts)
    )


def _report_exhibit() -> str:
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
        if verdict not in TERMS:
            raise SystemExit(f"{EXHIBIT_FIXTURE}: verdict {verdict!r} is not holds, broken or skipped")
        rows.append((item, evidence, verdict))

    total = _TOTAL.search(report)
    if not rows or not total:
        raise SystemExit(f"{EXHIBIT_FIXTURE}: no verdict table or no total line in EXPECTED_REPORT.md")
    counts = {v: sum(1 for r in rows if r[2] == v) for v in TERMS}
    stated = dict(zip(("holds", "broken", "skipped", "items"), map(int, total.groups())))
    if counts != {k: stated[k] for k in counts} or len(rows) != stated["items"]:
        raise SystemExit(f"{EXHIBIT_FIXTURE}: the total line disagrees with the verdict table")

    items = "\n".join(
        f'    <li class="is-{verdict}"><span class="verdict">{TERMS[verdict]}</span>'
        f'<span class="what">{_inline(item)}<small>{_inline(evidence)}</small></span></li>'
        for item, evidence, verdict in rows
    )
    source = f"{PLUGIN_REPO}/tree/main/fixtures/{EXHIBIT_FIXTURE}"
    line = (f"{stated['holds']} verified, {stated['broken']} failed, {stated['skipped']} not verified "
            f"of {stated['items']} items.")
    return (
        f"<!-- Generated from fixtures/{EXHIBIT_FIXTURE}/EXPECTED_REPORT.md by scripts/emit.py. "
        "Edit that, not this. -->\n"
        '<figure class="report" aria-labelledby="report-title">\n'
        '  <figcaption class="report-head">\n'
        '    <span class="report-kicker">Expected report, in the conductor\'s terms</span>\n'
        '    <span class="report-title" id="report-title">What the conductor is held to on '
        f'<a href="{source}">a notes app that looks finished</a></span>\n'
        "  </figcaption>\n"
        '  <ol class="verdicts">\n'
        f"{items}\n"
        "  </ol>\n"
        f'  <p class="report-total">{html.escape(line)}</p>\n'
        "</figure>\n"
    )


def _page_body(doc: dict) -> tuple[str, list[dict]]:
    """The page's Markdown: no title (the layout draws it), and an id on every section."""
    lines = doc["body"].rstrip("\n").split("\n")
    out, toc, used, fence = [], [], set(), None
    dropped_title = False
    for line in lines:
        marker = re.match(r"^(`{3,}|~{3,})", line)
        if marker:
            fence = None if fence and line.startswith(fence) else (fence or marker.group(1))
        if fence is None and not marker:
            if line.startswith("# ") and not dropped_title:
                dropped_title = True
                continue
            heading = re.match(r"^##\s+(.+?)\s*$", line)
            if heading:
                text = heading.group(1)
                base = slugify(text) or "section"
                anchor, n = base, 2
                while anchor in used:
                    anchor, n = f"{base}-{n}", n + 1
                used.add(anchor)
                toc.append({"id": anchor, "title": text})
                line = f"## {text} {{#{anchor}}}"
        out.append(line)
    return "\n".join(out).strip("\n") + "\n", toc


def emit_pages(docs: list[dict]) -> Files:
    """One page per file of the conductor, through the site's layout.

    The Markdown is the file's own text with its title removed (the layout draws that) and an id
    added to each section for the contents list. It is a reading copy: the files agents load are
    the byte-for-byte ones under `.well-known/agent-skills/conductor/`.
    """
    files: Files = {}
    for d in docs:
        body, toc = _page_body(d)
        if "{% endraw %}" in body or "{%- endraw" in body:
            raise SystemExit(f"conductor/{d['path']}: contains endraw, it cannot be shown on a page")
        front = (
            "---\n"
            "layout: guide\n"
            'excerpt_separator: ""\n'
            f"title: {json.dumps(d['title'], ensure_ascii=False)}\n"
            f"description: {json.dumps(d['description'], ensure_ascii=False)}\n"
            f"permalink: {d['page']}\n"
            f"kind: {d['kind']}\n"
            f"file: {json.dumps(d['path'])}\n"
            f"source_url: {d['source']}\n"
            f"toc: {json.dumps(toc, ensure_ascii=False)}\n"
            "---\n"
        )
        name = "index.md" if d["kind"] == "skill" else d["path"]
        files[name] = front + "{% raw %}" + body + "{% endraw %}\n"
    return files


# --- pages that moved --------------------------------------------------------------

# Where each retired skill's content went. The conductor's coverage map
# (docs/migration/coverage-map.md) names the destination of every rule; this is the file that
# holds most of a skill's, or the entry point where the skill was a path through the whole
# project. A saved link to the skill's page, or to its SKILL.md, lands there.
RETIRED_SKILLS = {
    "act-on-the-physical-world": "guidance/physical.md",
    "automate-a-workflow": "guidance/software.md",
    "change-with-a-reason": "SKILL.md",
    "choose-with-evidence": "guidance/decisions.md",
    "design-the-experience": "guidance/design.md",
    "fix-a-bug-test-first": "guidance/software.md",
    "handle-an-incident": "guidance/operations.md",
    "isolate-tests-from-services": "guidance/software.md",
    "keep-it-confidential": "guidance/confidentiality.md",
    "keep-it-on-course": "guidance/operations.md",
    "map-the-architecture": "guidance/software.md",
    "prove-the-docs": "guidance/software.md",
    "qa-an-agents-tests": "guidance/software.md",
    "release-to-people": "guidance/product.md",
    "repair-a-green-pipeline": "guidance/software.md",
    "repair-setup-script": "guidance/software.md",
    "review-an-agent-pr": "guidance/software.md",
    "run-autonomously": "guidance/autonomy.md",
    "run-the-error-paths": "guidance/software.md",
    "scope-a-vague-issue": "guidance/software.md",
    "security-review-agent-code": "guidance/software.md",
    "start-from-an-idea": "SKILL.md",
    "take-to-production": "guidance/quality.md",
    "translate-the-docs": "guidance/software.md",
    "update-dependencies": "guidance/software.md",
    "verify-a-migration": "guidance/software.md",
}

# Pages removed before the conductor, and the address they last redirected to, now redirected
# to what holds that content. Each of these once pointed at a skill that has itself been retired.
MOVED = {
    "/prompts/task_analyze_and_improve_ui_ux.html": "guidance/design.md",
    "/prompts/task_build_api_frontend.html": "guidance/design.md",
    "/prompts/task_build_from_plan.html": "SKILL.md",
    "/prompts/task_curate_repo.html": "SKILL.md",
    "/prompts/task_fix_and_refine.html": "guidance/quality.md",
    "/prompts/task_harden_repo_initial.html": "guidance/quality.md",
    "/prompts/task_harden_repo_iterative.html": "guidance/operations.md",
    "/prompts/task_audit_repo.html": "guidance/quality.md",
    "/prompts/task_generate_prompt_from_description.html": "SKILL.md",
    "/prompts/task_prove_the_fix.html": "guidance/software.md",
    "/prompts/template_master_prompt.html": "SKILL.md",
    "/environment-setup/": "guidance/software.md",
    # The guide, the skills page and the workflow page listed the skills; the conductor is the list now.
    "/prompts-guide/": "SKILL.md",
    "/tasks.html": "SKILL.md",
    "/workflow/": "SKILL.md",
}
for _slug, _target in RETIRED_SKILLS.items():
    MOVED[f"/prompts/task_{_slug.replace('-', '_')}.html"] = _target


def _redirect_page(old: str, doc: dict) -> str:
    target = SITE + doc["page"]
    title = html.escape(doc["title"])
    return (
        "---\n"
        f"permalink: {old}\n"
        "sitemap: false\n"
        "---\n"
        "<!doctype html>\n"
        '<html lang="en">\n'
        "<head>\n"
        '<meta charset="utf-8">\n'
        f"<title>Moved to {title}</title>\n"
        f'<link rel="canonical" href="{target}">\n'
        f'<meta http-equiv="refresh" content="0; url={target}">\n'
        '<meta name="robots" content="noindex">\n'
        "</head>\n"
        "<body>\n"
        f'<p>This page was replaced by <a href="{target}">{title}</a>.</p>\n'
        "</body>\n"
        "</html>\n"
    )


def emit_redirects(docs: list[dict]) -> Files:
    """A stub at each retired address, pointing at what holds its content now.

    - every retired page (`MOVED`) becomes a redirect page;
    - each retired skill's `SKILL.md` address, which agents saved from the old discovery index,
      serves a short notice in the same place that names the conductor;
    - `/workflow.json`, the old machine-readable path, serves a notice as JSON.
    """
    by_path = {d["path"]: d for d in docs}
    out: Files = {}
    for old, path in sorted(MOVED.items()):
        if path not in by_path:
            raise SystemExit(f"{old} redirects to conductor/{path}, which is not a file")
        name = old.strip("/").replace("/", "_").removesuffix(".html") or "index"
        out[f"{name}.html"] = _redirect_page(old, by_path[path])

    entry = _entry(docs)
    for slug, path in sorted(RETIRED_SKILLS.items()):
        if path not in by_path:
            raise SystemExit(f"{slug} maps to conductor/{path}, which is not a file")
        target = by_path[path]
        note = (
            f"The skill {slug} was retired. What it held is now part of the conductor, "
            "the one entry point of this library.\n\n"
            f"Conductor (read this first): {SITE}{entry['source']}\n"
            f"Whole folder, with SHA-256 in the index: {SITE}{ARCHIVE_URL}\n"
            f"Where this skill's guidance went: {SITE}{target['source']}\n"
            f"Index: {SITE}{DISCOVERY}/index.json\n"
        )
        out[f"agent-skills-{slug}.txt"] = (
            "---\n"
            f"permalink: {DISCOVERY}/{slug}/SKILL.md\n"
            "layout: null\n"
            "sitemap: false\n"
            'excerpt_separator: ""\n'
            "---\n"
            f"{{% raw %}}{note}{{% endraw %}}"
        )

    notice = {
        "moved": True,
        "note": "workflow.json was retired. The conductor replaces the fixed path with a control loop "
                "that starts where the project's first unmet acceptance is.",
        "replaced_by": SITE + entry["source"],
        "archive": SITE + ARCHIVE_URL,
        "index": f"{SITE}{DISCOVERY}/index.json",
    }
    out["workflow-json.json"] = (
        "---\npermalink: /workflow.json\nlayout: null\nsitemap: false\n---\n"
        f"{{% raw %}}{json.dumps(notice, indent=2)}\n{{% endraw %}}"
    )
    return out


# name -> (output directory relative to the repo root, renderer)
TARGETS = {
    "skills": ("skills", emit_skills),
    "plugin": ("plugin", emit_plugin),
    "marketplace": (".", emit_marketplace),
    "index": (".", emit_index),
    "agent-skills": ("_agent_skills", emit_agent_skills),
    "archive": (".", emit_archive),
    "site": (".", emit_site),
    "pages": ("_conductor_pages", emit_pages),
    "redirects": ("redirects", emit_redirects),
}


def render(target: str, docs: list[dict]) -> dict[Path, str | bytes]:
    directory, renderer = TARGETS[target]
    base = ROOT if directory == "." else ROOT / directory
    return {base / relative: content for relative, content in renderer(docs).items()}


def orphans(target: str, expected: dict[Path, str | bytes]) -> list[Path]:
    """Files in a target's own directory that nothing generates any more."""
    directory, _ = TARGETS[target]
    base = ROOT / directory
    if directory == "." or not base.is_dir():
        return []
    return sorted(path for path in base.rglob("*")
                  if path.is_file() and path not in expected and path.name != "README.md")


def write(target: str, docs: list[dict]) -> list[Path]:
    written = []
    expected = render(target, docs)
    for path, content in expected.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        data = as_bytes(content)
        if not path.exists() or path.read_bytes() != data:
            path.write_bytes(data)
        written.append(path)
    # A file that was removed from the source takes its generated forms with it.
    for path in orphans(target, expected):
        path.unlink()
        for parent in path.parents:
            if parent == ROOT or any(parent.iterdir()):
                break
            parent.rmdir()
    return written


def differences(target: str, docs: list[dict]) -> list[str]:
    """What a fresh generation would change. Empty means the copy is honest."""
    problems = []
    expected = render(target, docs)
    for path, content in expected.items():
        if not path.exists():
            problems.append(f"{path.relative_to(ROOT).as_posix()} is missing")
        elif path.read_bytes() != as_bytes(content):
            problems.append(f"{path.relative_to(ROOT).as_posix()} differs from its source")

    # A file nobody generates any more is drift in the other direction.
    for path in orphans(target, expected):
        problems.append(f"{path.relative_to(ROOT).as_posix()} is not generated from conductor/")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="exit 1 if anything would change")
    parser.add_argument("--target", action="append", choices=sorted(TARGETS))
    parser.add_argument("--list", action="store_true", help="list the targets")
    args = parser.parse_args()

    if args.list:
        for name, (directory, _) in sorted(TARGETS.items()):
            print(f"  {name:12} -> {directory}/")
        return 0

    docs = load_package()
    targets = args.target or sorted(TARGETS)

    if args.check:
        problems = [p for t in targets for p in differences(t, docs)]
        if problems:
            print(f"{len(problems)} generated file(s) disagree with conductor/:\n")
            for problem in problems:
                print(f"  {problem}")
            print("\nRun: python scripts/emit.py")
            return 1
        print(f"every generated form agrees with conductor/ ({len(docs)} files, {len(targets)} targets)")
        return 0

    for target in targets:
        written = write(target, docs)
        print(f"{target}: {len(written)} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
