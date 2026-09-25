#!/usr/bin/env python3
"""Does the built site give an agent, and a person, what it claims to?

    python scripts/check_site.py _site

Run it on the output of the GitHub Pages build, not on the source. The source can agree
with itself perfectly (check_library_integrity.py and emit.py --check prove that) while the
site serves something else: the live site had skill pages with no title, lines of a prompt
rendered as tables, fifty layout-less fragments of plugin/ in its sitemap, a workflow page
that disagreed with workflow.json, and not one SKILL.md an agent could fetch. None of that
was visible in the repository. All of it was visible in _site.

What it checks, each against the built files:

  agents   every skill in the discovery index is served, byte for byte the SKILL.md in
           skills/, with the digest the index states; every procedure has an entry; llms.txt
           lists every skill and every link in it resolves; each skill page points at its
           SKILL.md.
  people   every HTML page is a whole page with a <title> and one <h1>; skill pages carry
           their title and description; no prompt text has turned into a table.
  search   every page names a link-preview image the site serves, at 1200 by 630; every
           block of structured data parses; the home page and every skill page have one, and
           a skill page's names the skill's title and its SKILL.md.
  budget   no page pulls a script, stylesheet or font from another origin; the stylesheet,
           the script, the font, the preview image and every page stay under a size budget.

It reports the denominator and exits 1 on any problem. It is written to be able to fail:
run it against a build of the old site and it goes red.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
SITE_HOST = (ROOT / "CNAME").read_text(encoding="utf-8").strip()
INDEX = ".well-known/agent-skills/index.json"
SCHEMA = "https://schemas.agentskills.io/discovery/0.2.0/schema.json"

# Budgets, in bytes. Generous against today's sizes, tight against a framework creeping in.
BUDGET = {"css": 24_000, "js": 8_000, "page": 120_000, "font": 40_000, "image": 150_000}
FONT = "assets/fonts/martian-mono-latin-wght.woff2"

# Origins a page may load from. The favicon is shared across wecanuseai.com tools.
ALLOWED_ORIGINS = {"favicon.wecanuseai.com"}


class Page(HTMLParser):
    """The few facts about a page this check needs."""

    def __init__(self) -> None:
        super().__init__()
        self.has_html = False
        self.title = ""
        self.h1: list[str] = []
        self.loads: list[str] = []
        self.alternates: dict[str, str] = {}
        self.tables = 0
        self.meta: dict[str, str] = {}
        self.structured: list[str] = []
        self._in = None
        self._h1 = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.has_html = True
        elif tag == "title":
            self._in = "title"
        elif tag == "h1":
            self._in, self._h1 = "h1", ""
        elif tag == "script" and a.get("src"):
            self.loads.append(a["src"])
        elif tag == "script" and a.get("type") == "application/ld+json":
            self._in = "ld"
            self.structured.append("")
        elif tag == "link" and a.get("rel") in ("stylesheet", "preload"):
            self.loads.append(a.get("href", ""))
        elif tag == "meta" and a.get("property"):
            self.meta[a["property"]] = a.get("content", "")
        elif tag == "link" and a.get("rel") == "alternate" and a.get("type"):
            self.alternates[a["type"]] = a.get("href", "")
        elif tag == "table":
            self.tables += 1

    def handle_endtag(self, tag):
        if tag == "h1" and self._in == "h1":
            self.h1.append(self._h1.strip())
        if tag in ("title", "h1") or (tag == "script" and self._in == "ld"):
            self._in = None

    def handle_data(self, data):
        if self._in == "title":
            self.title += data
        elif self._in == "h1":
            self._h1 += data
        elif self._in == "ld":
            self.structured[-1] += data


def parse(path: Path) -> Page:
    page = Page()
    page.feed(path.read_text(encoding="utf-8"))
    return page


def local(site: Path, url: str) -> Path | None:
    """The file a same-site URL is served from, or None for another origin."""
    parsed = urlparse(url)
    if parsed.netloc and parsed.netloc != SITE_HOST:
        return None
    path = parsed.path
    target = site / path.lstrip("/")
    if path.endswith("/"):
        target = target / "index.html"
    return target


def png_size(path: Path) -> tuple[int, int] | None:
    """Width and height from a PNG's header, or None if it is not a PNG."""
    head = path.read_bytes()[:24]
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return int.from_bytes(head[16:20], "big"), int.from_bytes(head[20:24], "big")


def structured_nodes(page: Page, rel: str, problems: list[str]) -> list[dict]:
    """Every schema.org node on a page, or a problem for each block that does not parse."""
    nodes = []
    for block in page.structured:
        try:
            data = json.loads(block)
        except json.JSONDecodeError as e:
            problems.append(f"{rel}: structured data does not parse ({e})")
            continue
        if data.get("@context") != "https://schema.org":
            problems.append(f"{rel}: structured data has no schema.org @context")
        nodes.extend(data.get("@graph", [data]))
    return nodes


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    site = Path(sys.argv[1])
    if not (site / "index.html").exists():
        print(f"BLIND: {site} has no index.html. Build the site first. Refusing to report a pass.")
        return 1

    problems: list[str] = []
    checked = 0

    # --- agents -------------------------------------------------------------------
    library = json.loads((ROOT / "library.json").read_text(encoding="utf-8"))
    procedures = {p["slug"]: p for p in library["procedures"]}

    index_path = site / INDEX
    entries: dict[str, dict] = {}
    if not index_path.exists():
        problems.append(f"/{INDEX} is not served, so no discovery client can find a skill")
    else:
        index = json.loads(index_path.read_text(encoding="utf-8"))
        if index.get("$schema") != SCHEMA:
            problems.append(f"/{INDEX} $schema is {index.get('$schema')!r}, not {SCHEMA!r}")
        entries = {e.get("name"): e for e in index.get("skills", [])}

    for slug in procedures:
        checked += 1
        entry = entries.get(slug)
        if entry is None:
            problems.append(f"skill {slug} is in library.json but not in the discovery index")
            continue
        served = local(site, entry["url"])
        source = ROOT / "skills" / slug / "SKILL.md"
        if served is None or not served.is_file():
            problems.append(f"skill {slug}: {entry['url']} is not served")
            continue
        body = served.read_bytes()
        if body != source.read_bytes():
            problems.append(f"skill {slug}: the served SKILL.md differs from skills/{slug}/SKILL.md")
        digest = "sha256:" + hashlib.sha256(body).hexdigest()
        if entry.get("digest") != digest:
            problems.append(f"skill {slug}: index digest {entry.get('digest')} != served {digest}")
    for name in entries:
        if name not in procedures:
            problems.append(f"the discovery index lists {name}, which is not a procedure")

    llms = site / "llms.txt"
    if not llms.exists():
        problems.append("/llms.txt is not served")
    else:
        text = llms.read_text(encoding="utf-8")
        links = re.findall(r"\]\((https?://[^)\s]+)\)|:\s(https?://\S+)", text)
        for slug in procedures:
            if f"/.well-known/agent-skills/{slug}/SKILL.md" not in text:
                problems.append(f"llms.txt does not list {slug}")
        for pair in links:
            url = pair[0] or pair[1]
            checked += 1
            target = local(site, url)
            if target is not None and not target.is_file():
                problems.append(f"llms.txt links {url}, which the site does not serve")

    # --- people -------------------------------------------------------------------
    pages = sorted(p for p in site.rglob("*.html"))
    for path in pages:
        rel = path.relative_to(site).as_posix()
        text = path.read_text(encoding="utf-8")
        if 'http-equiv="refresh"' in text:
            continue  # a redirect stub, deliberately bare
        checked += 1
        page = parse(path)
        if not page.has_html:
            problems.append(f"{rel} is a fragment with no <html>: rendered without a layout")
            continue
        if not page.title.strip():
            problems.append(f"{rel} has no <title>")
        if len(page.h1) != 1:
            problems.append(f"{rel} has {len(page.h1)} <h1> elements, not one")
        for url in page.loads:
            host = urlparse(url).netloc
            if host and host != SITE_HOST and host not in ALLOWED_ORIGINS:
                problems.append(f"{rel} loads {url} from another origin")
        if len(text.encode("utf-8")) > BUDGET["page"]:
            problems.append(f"{rel} is {len(text.encode('utf-8'))} bytes, over {BUDGET['page']}")

        # What a search engine, a link preview and an assistant reading the page are given.
        image = page.meta.get("og:image", "")
        target = local(site, image) if urlparse(image).netloc else None
        if target is None:
            problems.append(f"{rel}: og:image {image!r} is not an absolute URL on this site")
        elif not target.is_file():
            problems.append(f"{rel}: og:image {image} is not served")
        elif png_size(target) != (1200, 630):
            problems.append(f"{rel}: og:image is {png_size(target)}, not a 1200 by 630 PNG")
        nodes = structured_nodes(page, rel, problems)
        types = {n.get("@type") for n in nodes}
        if rel == "index.html" and not {"WebSite", "FAQPage"} <= types:
            problems.append(f"{rel}: structured data has {sorted(map(str, types))}, not WebSite and FAQPage")

        if rel.startswith("prompts/"):
            stem = path.stem
            source = (ROOT / "_prompts" / f"{stem}.md").read_text(encoding="utf-8")
            title = re.search(r"^title:\s*(.+)$", source, re.M).group(1).strip()
            if page.h1 and page.h1[0] != title:
                problems.append(f"{rel} <h1> is {page.h1[0]!r}, not the title {title!r}")
            source_tables = len(re.findall(r"^\|.*\|\s*$\n^\|\s*:?-", source, re.M))
            if page.tables > source_tables:
                problems.append(f"{rel} renders {page.tables} table(s); its source has {source_tables}")
            if stem.startswith("task_"):
                slug = stem.removeprefix("task_").replace("_", "-")
                want = f"/.well-known/agent-skills/{slug}/SKILL.md"
                if page.alternates.get("text/markdown") != want:
                    problems.append(f"{rel} does not point agents at {want}")
                article = next((n for n in nodes if n.get("@type") == "TechArticle"), None)
                if article is None:
                    problems.append(f"{rel}: no TechArticle in its structured data")
                else:
                    if article.get("headline") != title:
                        problems.append(f"{rel}: structured headline {article.get('headline')!r} is not {title!r}")
                    content = article.get("encoding", {}).get("contentUrl", "")
                    if not content.endswith(want):
                        problems.append(f"{rel}: structured data points at {content!r}, not {want}")

    # --- budget -------------------------------------------------------------------
    for kind, path in (
        ("css", site / "assets/css/style.css"),
        ("js", site / "assets/js/main.js"),
        ("font", site / FONT),
        ("image", site / "assets/og.png"),
    ):
        checked += 1
        if not path.exists():
            problems.append(f"{path.relative_to(site)} is missing")
        elif path.stat().st_size > BUDGET[kind]:
            problems.append(f"{path.relative_to(site)} is {path.stat().st_size} bytes, over {BUDGET[kind]}")

    print(f"checked {len(procedures)} skill(s), {len(pages)} page(s); {checked} checks in all")
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for problem in problems:
            print(f"  - {problem}")
        return 1
    print("the site serves every skill verbatim, and every page is whole, titled, self-hosted and described")
    return 0


if __name__ == "__main__":
    sys.exit(main())
