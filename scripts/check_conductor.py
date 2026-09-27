#!/usr/bin/env python3
"""Check that the candidate conductor can be copied and followed as a whole folder.

This checks the package and its local references, not the quality of its instructions
or the delivery-trial acceptance gate. Run from any directory; optionally pass a
copied conductor directory to verify an installation.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parent.parent / "conductor"
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.M)
CODE = re.compile(r"`([^`]+)`")
LINK = re.compile(r"\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)")
FILE = re.compile(r"(?P<file>(?:(?:\.\./|\./|[A-Za-z0-9_-]+/)*)(?:[A-Za-z0-9_-]+\.md))(?P<anchor>#[^\s`)]*)?(?:\s+§(?P<section>.*))?$")
BARE_FILE_SECTION = re.compile(r"(?P<file>SKILL\.md)\s+§(?P<section>\d+)(?!\d)")


def normal(text: str) -> str:
    return " ".join(text.split())


def without_fences(text: str) -> str:
    """Examples describe a target project, not dependencies of this package."""
    return re.sub(r"^(`{3,}|~{3,})[^\n]*\n.*?^\1\s*$",
                  lambda m: re.sub(r"[^\n]", " ", m.group()), text, flags=re.M | re.S)


def heading_aliases(text: str) -> set[str]:
    aliases = set()
    for heading in HEADING.findall(text):
        heading = normal(heading)
        aliases.add(heading)
        numbered = re.match(r"(\d+)\.\s+(.+)", heading)
        if numbered:
            aliases.update(numbered.groups())
    return aliases


def anchor(text: str) -> str:
    return re.sub(r"[^\w\- ]", "", text.lower()).replace(" ", "-")


def validate(root: Path) -> tuple[list[str], dict[str, int]]:
    root = root.resolve()
    problems: list[str] = []
    counts = {"files": 0, "references": 0, "sections": 0}
    entry = root / "SKILL.md"
    if not entry.is_file():
        return [f"{root}: missing SKILL.md; copy the complete conductor folder"], counts

    paths = sorted(root.rglob("*.md"))
    texts = {path: path.read_text(encoding="utf-8") for path in paths}
    counts["files"] = len(texts)
    readable = {path: without_fences(text) for path, text in texts.items()}
    headings = {path: heading_aliases(text) for path, text in readable.items()}
    entry_text = texts[entry]
    front = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", entry_text, re.S)
    if not front:
        problems.append("SKILL.md: missing or unclosed YAML front matter")
    else:
        try:
            meta = yaml.safe_load(front.group(1))
        except yaml.YAMLError as error:
            problems.append(f"SKILL.md: invalid YAML front matter: {error}")
            meta = None
        if not isinstance(meta, dict):
            problems.append("SKILL.md: front matter must be a mapping")
        else:
            if meta.get("name") != "conductor":
                problems.append("SKILL.md: name must be 'conductor', matching its install directory")
            description = meta.get("description")
            if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
                problems.append("SKILL.md: description must be nonempty text of at most 1024 characters")

    for directory in ("guidance", "templates"):
        if not list((root / directory).glob("*.md")):
            problems.append(f"{directory}/: no Markdown files; the installed package is incomplete")

    entry_members: set[Path] = set()

    def location(source: Path, offset: int) -> str:
        return f"{source.relative_to(root).as_posix()}:{texts[source].count(chr(10), 0, offset) + 1}"

    def resolve(source: Path, name: str, offset: int) -> Path | None:
        # SKILL.md is also used as the conductor's name in prose inside guidance/.
        target = entry if name == "SKILL.md" else (source.parent / name).resolve()
        counts["references"] += 1
        if not target.is_relative_to(root):
            problems.append(f"{location(source, offset)}: {name!r} leaves the conductor package")
            return None
        if target not in texts:
            problems.append(f"{location(source, offset)}: missing local file {name!r}; restore it or update the reference")
            return None
        if source == entry:
            entry_members.add(target)
        return target

    def section(source: Path, target: Path, name: str, offset: int, prose: bool = False) -> None:
        counts["sections"] += 1
        name = normal(name)
        matches = name in headings[target]
        if prose:
            # Unquoted prose includes following punctuation and words. Require a whole
            # heading (or numbered section) at the start, never a substring match.
            matches = any(re.match(re.escape(h) + r"(?=$|[\s.,;:)])", name)
                          for h in headings[target])
        if not matches:
            shown = name if len(name) <= 100 else name[:100] + "..."
            problems.append(f"{location(source, offset)}: section {shown!r} does not exist in {target.relative_to(root).as_posix()}")

    for source, text in readable.items():
        rel = source.relative_to(root)
        if source != entry and (len(rel.parts) != 2 or rel.parts[0] not in {"guidance", "templates"}):
            problems.append(f"{rel.as_posix()}: unexpected document; put supporting guidance in guidance/ or templates/")
        if len(re.findall(r"^#\s+\S", text, re.M)) != 1:
            problems.append(f"{rel.as_posix()}: expected one document title (# heading)")
        # Spaces preserve offsets so every error retains a useful source line.
        remaining = list(text)
        for match in CODE.finditer(text):
            value = normal(match.group(1))
            file_ref = FILE.fullmatch(value)
            if file_ref:
                name = file_ref.group("file")
                # These are target-project examples, not conductor dependencies.
                if name == "AGENTS.md" or re.match(r"\d{4}-", name):
                    continue
                target = resolve(source, name, match.start())
                if target and file_ref.group("section"):
                    section(source, target, file_ref.group("section"), match.start())
                if target and file_ref.group("anchor"):
                    wanted = unquote(file_ref.group("anchor")[1:])
                    if wanted not in {anchor(h) for h in HEADING.findall(readable[target])}:
                        problems.append(f"{location(source, match.start())}: missing anchor {wanted!r} in {name}")
            elif value.startswith("§"):
                # In the loading table the sections belong to that row's guidance file.
                line_start = text.rfind("\n", 0, match.start()) + 1
                line_end = text.find("\n", match.end())
                line = text[line_start:line_end if line_end >= 0 else len(text)]
                table_file = re.search(r"`(guidance/[^`]+\.md)`", line) if line.startswith("|") else None
                target = resolve(source, table_file.group(1), match.start()) if table_file else source
                if target:
                    section(source, target, value[1:], match.start())
            for pos in range(match.start(), match.end()):
                if remaining[pos] != "\n":
                    remaining[pos] = " "

        for match in LINK.finditer(text):
            value = unquote(match.group(1))
            if "://" in value or value.startswith("mailto:"):
                continue
            name, _, fragment = value.partition("#")
            if name and not name.endswith(".md"):
                continue
            target = resolve(source, name, match.start()) if name else source
            if target and fragment and fragment not in {anchor(h) for h in HEADING.findall(readable[target])}:
                problems.append(f"{location(source, match.start())}: missing anchor {fragment!r} in {name or source.name}")
            for pos in range(match.start(), match.end()):
                if remaining[pos] != "\n":
                    remaining[pos] = " "

        prose = "".join(remaining)
        for match in BARE_FILE_SECTION.finditer(prose):
            target = resolve(source, match.group("file"), match.start())
            if target:
                section(source, target, match.group("section"), match.start())
            remaining[match.start():match.end()] = " " * (match.end() - match.start())
        prose = "".join(remaining)
        for match in re.finditer(r"§", prose):
            section(source, source, prose[match.end():].split("\n\n", 1)[0], match.start(), prose=True)

    for path in paths:
        if path != entry and path not in entry_members:
            problems.append(f"SKILL.md: {path.relative_to(root).as_posix()} is not listed; every supporting file must be discoverable from the entry point")
    return problems, counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, nargs="?", default=ROOT)
    args = parser.parse_args()
    problems, counts = validate(args.directory)
    print(f"conductor: {counts['files']} files, {counts['references']} local references, {counts['sections']} section references checked")
    for problem in problems:
        print(f"  - {problem}")
    if not problems:
        print("conductor package and references agree; delivery acceptance remains a separate trial gate")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
