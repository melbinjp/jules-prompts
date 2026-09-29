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

  agents   the discovery index lists the conductor as an archive of the whole folder, and the
           archive served is the one the emitter builds, with the digest the index states; every
           file of the conductor is also served byte for byte at its own address; llms.txt lists
           every file, states the same digests and every link in it resolves; each conductor
           page points at the file it shows.
  moved    every retired address (the old skill pages, the old skills' SKILL.md addresses,
           /tasks.html, /workflow/ and /workflow.json) is served and lands on a page or file
           that exists, and none of them is in the sitemap.
  people   every HTML page is a whole page with a <title> and one <h1>; conductor pages carry
           their title and description; no Markdown has turned into a table.
  search   every page names a link-preview image the site serves, at 1200 by 630; every
           block of structured data parses; the home page and every conductor page have one, and
           a conductor page's names the file's title and where its Markdown is served.
  budget   no page pulls a script, stylesheet or font from another origin, and no web font
           is shipped at all (text is set in the reader's own system font); the stylesheet,
           the script, the preview image and every page stay under a size budget.

It reports the denominator and exits 1 on any problem. It is written to be able to fail:
run it against a build of the old site and it goes red.
"""
from __future__ import annotations

import hashlib
import io
import json
import re
import sys
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import emit  # noqa: E402  the same reading of conductor/ that generated the site's files

SITE_HOST = (ROOT / "CNAME").read_text(encoding="utf-8").strip()
INDEX = ".well-known/agent-skills/index.json"
SCHEMA = "https://schemas.agentskills.io/discovery/0.2.0/schema.json"

# Budgets, in bytes. Generous against today's sizes, tight against a framework creeping in.
BUDGET = {"css": 16_000, "js": 8_000, "page": 120_000, "image": 150_000}

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
    docs = emit.load_package()
    by_source = {d["source"]: d for d in docs}
    by_page = {d["page"]: d for d in docs}

    def sha(data: bytes) -> str:
        return "sha256:" + hashlib.sha256(data).hexdigest()

    # --- agents -------------------------------------------------------------------
    index_path = site / INDEX
    entries: list[dict] = []
    if not index_path.exists():
        problems.append(f"/{INDEX} is not served, so no discovery client can find the conductor")
    else:
        index = json.loads(index_path.read_text(encoding="utf-8"))
        if index.get("$schema") != SCHEMA:
            problems.append(f"/{INDEX} $schema is {index.get('$schema')!r}, not {SCHEMA!r}")
        entries = index.get("skills", [])
    names = [e.get("name") for e in entries]
    if names != ["conductor"]:
        problems.append(f"the discovery index lists {names}, not exactly the conductor")

    archive_digest = None
    for entry in entries[:1]:
        checked += 1
        if entry.get("type") != "archive":
            problems.append(f"the conductor is a folder, so its index type is 'archive', not {entry.get('type')!r}")
        if entry.get("description") != docs[0]["description"]:
            problems.append("the index description differs from the SKILL.md description")
        served = local(site, entry.get("url", ""))
        if served is None or not served.is_file():
            problems.append(f"the archive {entry.get('url')} is not served")
        else:
            data = served.read_bytes()
            archive_digest = sha(data)
            if entry.get("digest") != archive_digest:
                problems.append(f"index digest {entry.get('digest')} != served archive {archive_digest}")
            if data != emit.build_archive(docs):
                problems.append("the served archive is not the one built from conductor/")
            try:
                with zipfile.ZipFile(io.BytesIO(data)) as archive:
                    members = archive.namelist()
                    for member in members:
                        if member.startswith("/") or ".." in Path(member).parts:
                            problems.append(f"the archive holds an unsafe path {member!r}")
                    if sorted(members) != sorted(d["path"] for d in docs):
                        problems.append("the archive does not hold exactly the files of conductor/")
                    for d in docs:
                        if d["path"] in members and archive.read(d["path"]) != d["text"].encode("utf-8"):
                            problems.append(f"archive member {d['path']} differs from conductor/{d['path']}")
            except zipfile.BadZipFile:
                problems.append("the served archive is not a zip file")

    # Every file of the conductor, also served on its own, byte for byte.
    for d in docs:
        checked += 1
        served = local(site, d["source"])
        if served is None or not served.is_file():
            problems.append(f"{d['source']} is not served")
        elif served.read_bytes() != d["text"].encode("utf-8"):
            problems.append(f"the served {d['source']} differs from conductor/{d['path']}")

    llms = site / "llms.txt"
    if not llms.exists():
        problems.append("/llms.txt is not served")
    else:
        text = llms.read_text(encoding="utf-8")
        links = re.findall(r"\]\((https?://[^)\s]+)\)|:\s(https?://\S+)", text)
        for d in docs:
            if d["source"] not in text:
                problems.append(f"llms.txt does not list {d['path']}")
        if archive_digest and archive_digest not in text:
            problems.append("llms.txt does not state the archive's SHA-256, or states another")
        if emit.sha256(docs[0]["text"]) not in text:
            problems.append("llms.txt does not state SKILL.md's SHA-256, or states another")
        for pair in links:
            url = pair[0] or pair[1]
            checked += 1
            target = local(site, url)
            if target is not None and not target.is_file():
                problems.append(f"llms.txt links {url}, which the site does not serve")

    # --- moved --------------------------------------------------------------------
    sitemap = (site / "sitemap.xml").read_text(encoding="utf-8") if (site / "sitemap.xml").exists() else ""
    if f"{emit.SITE}/conductor/" not in sitemap:
        problems.append("the sitemap does not list the conductor page")
    refresh = re.compile(r'http-equiv="refresh" content="0; url=([^"]+)"')
    for old, path in sorted(emit.MOVED.items()):
        checked += 1
        stub = local(site, old)
        if stub is None or not stub.is_file():
            problems.append(f"the retired address {old} is not served")
            continue
        found = refresh.search(stub.read_text(encoding="utf-8"))
        wanted = emit.SITE + next(d["page"] for d in docs if d["path"] == path)
        if not found or found.group(1) != wanted:
            problems.append(f"{old} does not redirect to {wanted}")
        elif (local(site, found.group(1)) or stub).is_file() is False:
            problems.append(f"{old} redirects to {found.group(1)}, which the site does not serve")
        if old in sitemap:
            problems.append(f"the retired address {old} is in the sitemap")
    for slug, path in sorted(emit.RETIRED_SKILLS.items()):
        checked += 1
        notice = site / ".well-known" / "agent-skills" / slug / "SKILL.md"
        if not notice.is_file():
            problems.append(f"the retired skill's address /.well-known/agent-skills/{slug}/SKILL.md is not served")
            continue
        text = notice.read_text(encoding="utf-8")
        target = next(d for d in docs if d["path"] == path)
        for wanted in (emit.SITE + docs[0]["source"], emit.SITE + target["source"]):
            if wanted not in text:
                problems.append(f"the notice at the retired {slug} address does not point at {wanted}")
    checked += 1
    workflow = site / "workflow.json"
    try:
        notice = json.loads(workflow.read_text(encoding="utf-8"))
        if not notice.get("moved") or notice.get("replaced_by") != emit.SITE + docs[0]["source"]:
            problems.append("/workflow.json does not say where the conductor is")
    except (OSError, json.JSONDecodeError):
        problems.append("/workflow.json is not served as JSON")

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

        url = "/" + rel.removesuffix("index.html")
        doc = by_page.get(url)
        if rel.startswith("conductor/") and doc is None:
            problems.append(f"{rel} is a page under /conductor/ that no file of conductor/ explains")
        if doc is not None:
            if page.h1 and page.h1[0] != doc["title"]:
                problems.append(f"{rel} <h1> is {page.h1[0]!r}, not the title {doc['title']!r}")
            source_tables = len(re.findall(r"^\|.*\|\s*$\n^\|\s*:?-", doc["text"], re.M))
            if page.tables > source_tables:
                problems.append(f"{rel} renders {page.tables} table(s); its source has {source_tables}")
            if page.alternates.get("text/markdown") != doc["source"]:
                problems.append(f"{rel} does not point agents at {doc['source']}")
            article = next((n for n in nodes if n.get("@type") == "TechArticle"), None)
            if article is None:
                problems.append(f"{rel}: no TechArticle in its structured data")
            else:
                if article.get("headline") != doc["title"]:
                    problems.append(f"{rel}: structured headline {article.get('headline')!r} is not {doc['title']!r}")
                content = article.get("encoding", {}).get("contentUrl", "")
                if not content.endswith(doc["source"]):
                    problems.append(f"{rel}: structured data points at {content!r}, not {doc['source']}")
    for page_url in by_page:
        checked += 1
        built = site / page_url.lstrip("/")
        built = built / "index.html" if page_url.endswith("/") else built
        if not built.is_file():
            problems.append(f"the page {page_url} for a conductor file is not served")

    # --- budget -------------------------------------------------------------------
    for kind, path in (
        ("css", site / "assets/css/style.css"),
        ("js", site / "assets/js/main.js"),
        ("image", site / "assets/og.png"),
    ):
        checked += 1
        if not path.exists():
            problems.append(f"{path.relative_to(site)} is missing")
        elif path.stat().st_size > BUDGET[kind]:
            problems.append(f"{path.relative_to(site)} is {path.stat().st_size} bytes, over {BUDGET[kind]}")

    # One typeface, the reader's own: a web font is a download and a distraction the site
    # decided against. It shipped one until the site was made quieter.
    checked += 1
    shipped = sorted(str(f.relative_to(site)) for f in site.rglob("*") if f.suffix in (".woff", ".woff2", ".ttf", ".otf"))
    css = (site / "assets/css/style.css").read_text(encoding="utf-8") if (site / "assets/css/style.css").exists() else ""
    if shipped or "@font-face" in css:
        problems.append(f"the site ships a web font ({', '.join(shipped) or '@font-face in the stylesheet'})")

    print(f"checked {len(docs)} conductor file(s), {len(emit.MOVED)} retired page(s), "
          f"{len(emit.RETIRED_SKILLS)} retired skill address(es), {len(pages)} page(s); {checked} checks in all")
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for problem in problems:
            print(f"  - {problem}")
        return 1
    print("the site serves the conductor verbatim, every retired address lands somewhere, and every page is "
          "whole, titled, self-hosted and described")
    return 0


if __name__ == "__main__":
    sys.exit(main())
