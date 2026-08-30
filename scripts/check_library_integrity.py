"""Does this library agree with itself?

    python scripts/check_library_integrity.py

`prompts.json` is fetched by agents rather than read by people, and `PROMPTS_GUIDE.md` is
what a human reads first. The README asks for the prompt set, the guide, and the workflow to
stay aligned. Nothing checked that they did, and they had already drifted:
`task_build_api_frontend` shipped with a prompt file and no guide entry.

That is a small gap with an awkward property. A library whose own index is incomplete is
making a claim it cannot support, and this one is specifically sold as machine-readable, so
the index is the product rather than documentation about it.

Skills and fixtures are the same kind of claim. `skills/` is generated from `_prompts/`; a
copy that can drift is a defect. A fixture whose EXPECTED_REPORT.md does not name its
planted defects is a check that cannot fail.

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
GUIDE = ROOT / "PROMPTS_GUIDE.md"
WORKFLOW = ROOT / "workflow.json"
CONFIG = ROOT / "_config.yml"
FIXTURES = ROOT / "fixtures"
SKILLS = ROOT / "skills"

sys.path.insert(0, str(ROOT / "scripts"))
import generate_skills  # noqa: E402
import score_fixture  # noqa: E402

REQUIRED_FIELDS = ("layout", "title", "description", "category", "type")

GUIDE_ENTRY = re.compile(r"^### \[`([a-z0-9_]+)\.md`\]", re.M)

# Tool names and a role line that only Jules understood. Naming Jules in a list of
# harnesses the instructions do *not* depend on is allowed; addressing the agent as
# Jules, or telling it to call set_plan, is not.
FORBIDDEN_IN_PROMPTS = (
    "You are Jules",
    "`set_plan`",
    "request_code_review",
    "record_memory",
    "`submit` tool",
    "Jules' own FAQ",
    "Jules' own FAQ",
)


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

    guide = GUIDE.read_text(encoding="utf-8")
    documented = sorted(set(GUIDE_ENTRY.findall(guide)))

    for slug in files:
        if slug not in documented:
            problems.append(f"{slug}.md has no entry in PROMPTS_GUIDE.md")
    for slug in documented:
        if slug not in files:
            problems.append(f"PROMPTS_GUIDE.md documents {slug}.md, which does not exist")

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

    config_ok = True
    try:
        cfg = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
        if not isinstance(cfg, dict):
            problems.append("_config.yml did not parse to a mapping")
            config_ok = False
    except yaml.YAMLError as e:
        problems.append(f"_config.yml is not valid YAML, so Jekyll cannot build: {e}")
        config_ok = False

    steps = json.loads(WORKFLOW.read_text(encoding="utf-8"))["steps"]
    for s in steps:
        if s["prompt_slug"] not in files:
            problems.append(f"workflow.json step {s['order']} points at "
                            f"{s['prompt_slug']}, which is not in _prompts/")
    orders = [s["order"] for s in steps]
    if orders != list(range(1, len(steps) + 1)):
        problems.append(f"workflow.json step orders are {orders}, not 1..{len(steps)}")

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

    print(
        f"checked {len(files)} prompt(s), {len(documented)} guide entry(ies), "
        f"{len(steps)} workflow step(s), {len(planned)} skill(s), "
        f"{fixture_count} fixture(s) ({expected_ok} expected reports hold); _config.yml "
        f"{'parses' if config_ok else 'DOES NOT PARSE'}"
    )
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("the prompt set, the guide, the workflow, the skills and the fixtures agree")
    return 0


if __name__ == "__main__":
    sys.exit(main())
