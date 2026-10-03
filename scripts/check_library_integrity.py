"""Does this repository agree with itself?

    python scripts/check_library_integrity.py

The conductor, its regression fixtures, the request each fixture is run with and the site's
configuration are views of one library. This checks the parts of that agreement that no other
check covers: `check_conductor.py` for the package and its references, `emit.py --check` for the
generated forms, `check_site.py` for the built site. Which old check became which of these is in
`docs/migration/checks.md`.

A fixture is a claim that the conductor can be seen to fail. A fixture whose EXPECTED_REPORT.md
does not name its planted defects is a check that cannot fail, and a fixture with no request is
one nobody can run.

**This check is written to be able to fail.** No step in it swallows an exit code and there is
no `continue-on-error` on the workflow that runs it. A verification that cannot fail is
indistinguishable from one that was never run.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONDUCTOR = ROOT / "conductor"
CONFIG = ROOT / "_config.yml"
FIXTURES = ROOT / "fixtures"
REQUESTS = ROOT / "docs" / "trials" / "tools" / "requests.json"
RELEASE = ROOT / "docs" / "RELEASE.md"

sys.path.insert(0, str(ROOT / "scripts"))
import check_conductor  # noqa: E402
import score_fixture  # noqa: E402

# Tool names, branch names and a role line that only Jules understood. Naming Jules in a list of
# harnesses the instructions do *not* depend on is allowed; addressing the agent as Jules,
# telling it to call set_plan or google_search, or naming its branches jules/..., is not.
FORBIDDEN_IN_CONDUCTOR = (
    "You are Jules",
    "`set_plan`",
    "request_code_review",
    "record_memory",
    "`submit` tool",
    "Jules' own FAQ",
    "google_search",
    "view_text_website",
    "`jules/",
)

# The conductor may be used on a private, proprietary or offline project, so it says once, in the
# file every agent reads first, that no step assumes a hosted service.
SERVICE_AGNOSTIC = "hosted service"

# The paths of the retired 26-skill library. Their guidance lives in the conductor; the tag
# `library-26-final` keeps the old files. Their return would make two sources of truth.
RETIRED_PATHS = ("_prompts", "workflow.json", "compact", "scripts/generate_skills.py")

# kramdown reads a list item with a bare pipe in it as a table row, and the site renders the
# conductor through kramdown. A pipe inside a code span is fine, so code spans are removed first.
LIST_ITEM = re.compile(r"^\s*(?:[*+-]|\d+\.)\s")
CODE_SPAN = re.compile(r"`[^`]*`")

RELEASE_SECTIONS = ("Supported scope", "Known limitations", "Evidence", "Migration from the 26-skill library")
# The windows-cohort trial scored the corpus at this size. Later defects raised the live
# total. The release keeps both numbers. The live total is read from the fixture index.
TRIAL_DENOMINATOR = 146
STATUS_FILES = (
    ROOT / "docs" / "RELEASE.md",
    ROOT / "docs" / "VISION.md",
    ROOT / "docs" / "migration" / "coverage-map.md",
)


def main() -> int:
    problems: list[str] = []

    # --- the conductor ------------------------------------------------------------------
    conductor_problems, counts = check_conductor.validate(CONDUCTOR)
    problems.extend(f"conductor/{problem}" for problem in conductor_problems)
    if counts["files"] == 0:
        print("BLIND: no conductor files found at all. Refusing to report a pass.")
        return 1
    for path in sorted(CONDUCTOR.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        for needle in FORBIDDEN_IN_CONDUCTOR:
            if needle in text:
                problems.append(f"{rel} contains Jules-specific harness {needle!r}")
        in_fence = False
        for number, line in enumerate(text.splitlines(), 1):
            if line.startswith(("```", "~~~")):
                in_fence = not in_fence
            if not in_fence and LIST_ITEM.match(line) and "|" in CODE_SPAN.sub("", line):
                problems.append(f"{rel}:{number} has a bare '|' in a list item, which renders as a table on the site")
    entry = (CONDUCTOR / "SKILL.md").read_text(encoding="utf-8")
    if SERVICE_AGNOSTIC not in entry:
        problems.append("conductor/SKILL.md does not say it assumes no hosted service, so an agent "
                        "may read its steps as requiring one")

    # --- retired machinery stays retired ------------------------------------------------
    for retired in RETIRED_PATHS:
        if (ROOT / retired).exists():
            problems.append(f"{retired} is back, but the 26-skill library is retired; the conductor is the only source")

    # --- site configuration -------------------------------------------------------------
    config_ok = True
    try:
        cfg = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
        if not isinstance(cfg, dict):
            problems.append("_config.yml did not parse to a mapping")
            config_ok = False
    except yaml.YAMLError as e:
        problems.append(f"_config.yml is not valid YAML, so Jekyll cannot build: {e}")
        config_ok = False

    # _data/ feeds the home page and its structured data. A value with an unquoted colon in it
    # does not parse, and the only place that showed was the Pages build.
    for data_file in sorted((ROOT / "_data").glob("*.yml")):
        try:
            yaml.safe_load(data_file.read_text(encoding="utf-8"))
        except yaml.YAMLError as e:
            problems.append(f"_data/{data_file.name} is not valid YAML, so Jekyll cannot build: {e}")

    # --- fixtures: the conductor's regression cases -------------------------------------
    # Every one has its planted defects listed, an expected report that names them all, and the
    # request an agent is given; and the three lists of fixtures agree.
    index_path = FIXTURES / "index.json"
    fixture_count = 0
    expected_ok = 0
    requests: dict = {}
    if not REQUESTS.exists():
        problems.append("docs/trials/tools/requests.json is missing, so no fixture can be run")
    else:
        requests = json.loads(REQUESTS.read_text(encoding="utf-8"))
    planted_total = None
    if not index_path.exists():
        problems.append("fixtures/index.json is missing")
    else:
        listed = json.loads(index_path.read_text(encoding="utf-8")).get("fixtures") or []
        planted_total = sum(int(entry.get("planted") or 0) for entry in listed)
        if not listed:
            problems.append("BLIND: fixtures/index.json lists no fixtures")
        listed_names = [entry.get("name") for entry in listed]
        for entry in listed:
            name = entry.get("name")
            fixture_dir = FIXTURES / name
            if not fixture_dir.is_dir():
                problems.append(f"fixtures/index.json lists {name}, which has no directory")
                continue
            fixture_count += 1
            spec_path = fixture_dir / "defects.json"
            expected_path = fixture_dir / "EXPECTED_REPORT.md"
            if not spec_path.exists():
                problems.append(f"fixtures/{name}/defects.json is missing")
                continue
            if not expected_path.exists():
                problems.append(f"fixtures/{name}/EXPECTED_REPORT.md is missing")
                continue
            if not (requests.get(name) or "").strip():
                problems.append(f"fixtures/{name} has no request in docs/trials/tools/requests.json")
            spec = score_fixture.load_defects(fixture_dir)
            if entry.get("planted") != len(spec["defects"]):
                problems.append(f"fixtures/index.json says {name} plants {entry.get('planted')}, "
                                f"defects.json lists {len(spec['defects'])}")
            out = score_fixture.score(expected_path.read_text(encoding="utf-8"), spec)
            if out["holds"] != out["planted"] or out["invented"]:
                problems.append(
                    f"fixtures/{name}/EXPECTED_REPORT.md names {out['holds']} of {out['planted']} "
                    f"planted defects (invented {out['invented']})"
                )
            else:
                expected_ok += 1
        for path in sorted(FIXTURES.iterdir()):
            if path.is_dir() and (path / "defects.json").exists() and path.name not in listed_names:
                problems.append(f"fixtures/{path.name}/ exists but is not in fixtures/index.json")
        for name in requests:
            if name not in listed_names:
                problems.append(f"docs/trials/tools/requests.json has a request for {name}, which is not a fixture")

    # --- the release document -----------------------------------------------------------
    if not RELEASE.exists():
        problems.append("docs/RELEASE.md is missing")
    else:
        headings = set(re.findall(r"^##\s+(.+?)\s*$", RELEASE.read_text(encoding="utf-8"), re.M))
        for section in RELEASE_SECTIONS:
            if section not in headings:
                problems.append(f"docs/RELEASE.md has no '{section}' section")
        release_text = RELEASE.read_text(encoding="utf-8")
        if not re.search(rf"\b{TRIAL_DENOMINATOR}\b", release_text):
            problems.append(
                f"docs/RELEASE.md does not keep the trial denominator {TRIAL_DENOMINATOR}"
            )
    if planted_total is not None:
        for path in STATUS_FILES:
            label = path.relative_to(ROOT).as_posix()
            text = path.read_text(encoding="utf-8") if path.exists() else ""
            if not re.search(rf"\b{planted_total}\b", text):
                problems.append(f"{label} does not state the planted total {planted_total}")

    print(
        f"checked conductor: {counts['files']} files, {counts['references']} local references, "
        f"{counts['sections']} section references"
    )
    print(
        f"checked {fixture_count} fixture(s) ({expected_ok} expected reports name every planted defect); "
        f"_config.yml {'parses' if config_ok else 'DOES NOT PARSE'}"
    )
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("the conductor package is complete and its regression fixtures agree with their requests and expected reports")
    return 0


if __name__ == "__main__":
    sys.exit(main())
