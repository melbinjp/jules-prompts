"""Does this library agree with itself?

    python scripts/check_library_integrity.py

The prompt set, the workflow, the generated skills and the fixtures are views of one library,
and they had drifted before: a prompt once shipped with no entry in the guide that listed them.
Nothing checked that they agreed, so this does.

That is a small gap with an awkward property. A library whose own index is incomplete is
making a claim it cannot support, and this one is specifically sold as machine-readable, so
the index is the product rather than documentation about it.

Skills and fixtures are the same kind of claim. `skills/` is generated from `_prompts/`; a
copy that can drift is a defect. A skill with no fixture has never been seen to fail, and a
fixture whose EXPECTED_REPORT.md does not name its planted defects is a check that cannot fail.

**This check is written to be able to fail.** No step in it swallows an exit code and there
is no `continue-on-error` on the workflow that runs it. A verification that cannot fail is
indistinguishable from one that was never run.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PROMPTS = ROOT / "_prompts"
WORKFLOW = ROOT / "workflow.json"
CONFIG = ROOT / "_config.yml"
FIXTURES = ROOT / "fixtures"
SKILLS = ROOT / "skills"

sys.path.insert(0, str(ROOT / "scripts"))
import generate_skills  # noqa: E402
import score_fixture  # noqa: E402

REQUIRED_FIELDS = ("layout", "title", "description", "category", "type")

# Tool names, branch names and a role line that only Jules understood. Naming Jules in a
# list of harnesses the instructions do *not* depend on is allowed; addressing the agent as
# Jules, telling it to call set_plan or google_search, or naming its branches jules/..., is
# not. The last three were still in four legacy prompts after the unwrap, because this list
# only named the tools that had already been found.
FORBIDDEN_IN_PROMPTS = (
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

# This library takes any idea and makes it happen. A procedure that tells an agent to decide
# whether an idea deserves to exist, or to end a project when a number is missed, works against
# that: it turns a constraint into a verdict. The first version of the lifecycle skills did
# both, with a "should it exist" step and stop conditions, and read the owner's worry about
# half-built projects as a reason to build fewer. A blocked route gets another route.
PROJECT_ENDING = (
    "stop condition",
    "kill criteri",
    "whether it should exist",
    "whether it should be built",
    "should not be built",
    "don't build it",
    "do not build it",
)

# Projects can be private, proprietary, offline, or built without the tools everyone else uses.
# Every procedure says so in the same words, so an agent never reads "open a pull request" or
# "search the web" as a requirement to use a hosted service the project cannot or must not use.
SERVICE_AGNOSTIC = "They do not assume any hosted service either"

# The sections every skill has, in the order the Skill Template gives them.
SECTIONS = ("Objective", "Context", "Requirements & Constraints", "Guiding Principles",
            "Execution Flow", "Deliverables")

# Every procedure renders through the skill layout, which is what gives its page a title,
# its tier and the ways to load it. A prompt on any other layout renders as a bare body.
PROMPT_LAYOUT = "skill"

# kramdown reads a list item with a bare pipe in it as a table row. "`repo` | `site`" in a
# Context list rendered as a two-row table on the live site. A pipe inside a code span is
# fine, so code spans are removed before looking.
LIST_ITEM = re.compile(r"^\s*(?:[*+-]|\d+\.)\s")
CODE_SPAN = re.compile(r"`[^`]*`")


def front_matter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end]
    try:
        data = yaml.safe_load(block)
    except yaml.YAMLError:
        return {"__malformed__": True}
    if not isinstance(data, dict):
        return {"__malformed__": True}
    return {k: True for k in data}


def main() -> int:
    problems: list[str] = []

    files = sorted(p.stem for p in PROMPTS.glob("*.md"))
    if not files:
        print("BLIND: no prompt files found at all. Refusing to report a pass.")
        return 1

    for p in sorted(PROMPTS.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        fm = front_matter(text)
        if fm.get("__malformed__"):
            problems.append(f"{p.name} front matter is not valid YAML, so it will not render")
            continue
        if not fm:
            problems.append(f"{p.name} has no YAML front matter, so it will not render")
            continue
        for field in REQUIRED_FIELDS:
            if field not in fm:
                problems.append(f"{p.name} front matter is missing '{field}'")
        for needle in FORBIDDEN_IN_PROMPTS:
            if needle in text:
                problems.append(f"{p.name} still contains Jules-specific harness {needle!r}")
        # Every skill has the same shape, and ends in a verdict someone can check. Fifteen once
        # did not: four had no deliverables at all, and the site said every skill ends in one.
        if p.stem.startswith("task_"):
            for section in SECTIONS:
                if f"**{section}:**" not in text:
                    problems.append(f"{p.name} has no {section} section")
            ending = text[text.rfind("**Deliverables:**"):] if "**Deliverables:**" in text else ""
            if not all(v in ending for v in ("`holds`", "`broken`", "`skipped`")) or "denominator" not in ending:
                problems.append(f"{p.name} does not end in holds, broken or skipped with a denominator")
        if SERVICE_AGNOSTIC not in text:
            problems.append(f"{p.name} does not say it assumes no hosted service, so an agent "
                            "may read its steps as requiring one")
        for needle in PROJECT_ENDING:
            if needle in text.lower():
                problems.append(f"{p.name} tells an agent to end or refuse a project "
                                f"({needle!r}); a blocked route gets another route")
        layout = (yaml.safe_load(text[3:text.find("\n---", 3)]) or {}).get("layout")
        if layout != PROMPT_LAYOUT:
            problems.append(f"{p.name} uses layout {layout!r}, not {PROMPT_LAYOUT!r}, so its "
                            "page has no title or install panel")
        for number, line in enumerate(text.splitlines(), 1):
            if LIST_ITEM.match(line) and "|" in CODE_SPAN.sub("", line):
                problems.append(f"{p.name}:{number} has a bare '|' in a list item, which "
                                "renders as a table on the site")

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

    workflow = json.loads(WORKFLOW.read_text(encoding="utf-8"))
    steps = workflow["steps"]
    for s in steps:
        if s["prompt_slug"] not in files:
            problems.append(f"workflow.json step {s['order']} points at "
                            f"{s['prompt_slug']}, which is not in _prompts/")
        if not (s.get("done_when") or "").strip():
            problems.append(f"workflow.json step {s['order']} does not say when it is done")
        for branch in s.get("branches", []):
            if branch not in files:
                problems.append(f"workflow.json step {s['order']} calls on {branch}, which is "
                                "not in _prompts/")
    orders = [s["order"] for s in steps]
    if orders != list(range(1, len(steps) + 1)):
        problems.append(f"workflow.json step orders are {orders}, not 1..{len(steps)}")

    # A project in any state enters the path where its state says. Every entry starts at a step
    # of the path, so no state leads somewhere the path does not go; and a project that already
    # exists is founded again on paper, so what it already is gets a reason like everything else.
    on_path = {s["prompt_slug"] for s in steps}
    entries = workflow.get("entries") or []
    if not entries:
        problems.append("workflow.json has no entries, so a project not at the start has no way in")
    for e in entries:
        if e.get("start") not in on_path:
            problems.append(f"workflow.json entry {e.get('state')!r} starts at {e.get('start')}, "
                            "which is not a step of the path")
        for then in e.get("then", []):
            if then not in files:
                problems.append(f"workflow.json entry {e.get('state')!r} continues to {then}, "
                                "which is not in _prompts/")
        if not (e.get("note") or "").strip():
            problems.append(f"workflow.json entry {e.get('state')!r} does not say what happens there")
    existing = [e for e in entries if "already exists" in e.get("state", "")]
    if not existing or existing[0].get("start") != "task_start_from_an_idea":
        problems.append("workflow.json: a project that already exists must start by being founded "
                        "again on paper (task_start_from_an_idea), or its existing parts have no reason")
    for t in workflow.get("throughout") or []:
        if t.get("skill") not in files:
            problems.append(f"workflow.json throughout names {t.get('skill')}, which is not in _prompts/")

    # skills/ is a generated view of _prompts/. Disagreement is the defect.
    planned = generate_skills.planned()
    if not planned:
        problems.append("BLIND: generate_skills.planned() returned nothing")
    skill_problems_before = len(problems)
    if generate_skills.check(planned) != 0:
        # generate_skills.check already printed; record that it failed.
        if len(problems) == skill_problems_before:
            problems.append("skills/ disagrees with _prompts/ (see generate_skills --check)")

    # Fixtures: every index entry exists, points at a real skill, and its expected
    # report names every planted defect. A fixture that cannot fail is not a fixture.
    index_path = FIXTURES / "index.json"
    fixture_count = 0
    expected_ok = 0
    if not index_path.exists():
        problems.append("fixtures/index.json is missing")
    else:
        index = json.loads(index_path.read_text(encoding="utf-8"))
        listed = index.get("fixtures") or []
        if not listed:
            problems.append("BLIND: fixtures/index.json lists no fixtures")
        listed_names = []
        for entry in listed:
            name = entry.get("name")
            skill = entry.get("skill")
            listed_names.append(name)
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
            spec = score_fixture.load_defects(fixture_dir)
            if spec.get("skill") != skill:
                problems.append(
                    f"fixtures/{name}: index skill {skill!r} != defects.json skill {spec.get('skill')!r}"
                )
            if skill not in planned:
                problems.append(f"fixtures/{name} points at skill {skill!r}, which is not generated")
            report = expected_path.read_text(encoding="utf-8")
            out = score_fixture.score(report, spec)
            if out["holds"] != out["planted"] or out["invented"]:
                problems.append(
                    f"fixtures/{name}/EXPECTED_REPORT.md names {out['holds']} of {out['planted']} "
                    f"planted defects (invented {out['invented']})"
                )
            else:
                expected_ok += 1
        on_disk = sorted(
            p.name for p in FIXTURES.iterdir()
            if p.is_dir() and (p / "defects.json").exists()
        )
        for name in on_disk:
            if name not in listed_names:
                problems.append(f"fixtures/{name}/ exists but is not in fixtures/index.json")
        # Every skill has been seen to fail. The site says so, and a skill without a fixture
        # would make that a claim; ten of them once did.
        tested = {entry.get("skill") for entry in listed}
        for skill in sorted(planned):
            if skill not in tested:
                problems.append(f"skill {skill} has no fixture, so nobody has seen it catch anything")

    print(
        f"checked {len(files)} prompt(s), "
        f"{len(steps)} workflow step(s), {len(planned)} skill(s), "
        f"{fixture_count} fixture(s) ({expected_ok} expected reports hold); _config.yml "
        f"{'parses' if config_ok else 'DOES NOT PARSE'}"
    )
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("the prompt set, the workflow, the skills and the fixtures agree, and every skill has a fixture")
    return 0


if __name__ == "__main__":
    sys.exit(main())
