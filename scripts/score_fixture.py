#!/usr/bin/env python3
"""Score an agent's report against a planted-failure fixture.

A fixture is a miniature repository with known defects and a defects.json that
lists them. An agent given the matching skill writes a report. This script
decides holds / broken / skipped from the report text, never from whether the
report *sounds* complete.

    python scripts/score_fixture.py fixtures/unfailable-tests path/to/REPORT.md

Verdicts (the same three this library uses everywhere else):

    holds   the report named the planted defect
    broken  it missed it, or claimed a defect that is not planted
    skipped the report declined that defect with a reason (honest miss)

The last line is coverage. A clean report that never mentioned the test file
is not a clean report.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def load_defects(fixture: Path) -> dict:
    path = fixture / "defects.json"
    if not path.exists():
        raise SystemExit(f"BLIND: {path} does not exist. Refusing to report a pass.")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not data.get("defects"):
        raise SystemExit(f"BLIND: {path} lists no defects. Refusing to report a pass.")
    return data


def mentions(report: str, needles: list[str]) -> bool:
    lowered = report.lower()
    return all(n.lower() in lowered for n in needles)


def skipped(report: str, defect_id: str) -> bool:
    """A skip is a decline that names the defect and a reason, not a silence."""
    pattern = re.compile(
        rf"(?i)\b{re.escape(defect_id)}\b.{{0,240}}\b(skip|skipped|unjudged|could not|cannot check|not checked)\b"
        rf"|\b(skip|skipped|unjudged|could not|cannot check|not checked)\b.{{0,240}}\b{re.escape(defect_id)}\b"
    )
    return bool(pattern.search(report))


def score(report: str, spec: dict) -> dict:
    results = []
    planted_ids = {d["id"] for d in spec["defects"]}
    for defect in spec["defects"]:
        did = defect["id"]
        required = defect.get("must_mention") or [did]
        if mentions(report, required):
            verdict = "holds"
        elif skipped(report, did):
            verdict = "skipped"
        else:
            verdict = "broken"
        results.append({
            "id": did,
            "file": defect.get("file"),
            "verdict": verdict,
            "tell": defect.get("tell"),
        })

    invented = []
    claimed = set(re.findall(r"\bdefect[_-]id\s*[:=]\s*([a-z0-9-]+)", report, re.I))
    claimed |= set(re.findall(r"\[planted:([a-z0-9-]+)\]", report, re.I))
    for extra in sorted(claimed - planted_ids):
        invented.append(extra)
        results.append({
            "id": extra,
            "file": None,
            "verdict": "broken",
            "tell": "claimed a defect that is not in defects.json",
        })

    counts = {"holds": 0, "broken": 0, "skipped": 0}
    for r in results:
        counts[r["verdict"]] += 1
    planted = len(spec["defects"])
    judged = counts["holds"] + counts["broken"] + counts["skipped"]
    return {
        "fixture": spec.get("fixture"),
        "skill": spec.get("skill"),
        "planted": planted,
        "holds": counts["holds"],
        "broken": counts["broken"],
        "skipped": counts["skipped"],
        "invented": invented,
        "judged": judged,
        "results": results,
    }


def format_report(out: dict) -> str:
    lines = [
        f"fixture {out['fixture']}  skill {out['skill']}",
        f"{out['holds']} holds, {out['broken']} broken, {out['skipped']} skipped"
        + (f", invented {len(out['invented'])}" if out["invented"] else ""),
    ]
    for r in out["results"]:
        where = f"  {r['file']}" if r["file"] else ""
        lines.append(f"  {r['verdict']:8} {r['id']}{where}")
    coverage_pct = int(round(100 * out["holds"] / out["planted"])) if out["planted"] else 0
    lines.append(
        f"judged {out['judged']} of {out['planted']} planted. "
        f"{out['holds']} named, so this verdict covers {coverage_pct}% of the planted defects."
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", type=Path, help="path to fixtures/<name>/")
    parser.add_argument("report", type=Path, nargs="?", help="agent report (markdown or text)")
    parser.add_argument("--self-check", action="store_true",
                        help="score the fixture's own EXPECTED_REPORT.md; used by CI")
    args = parser.parse_args()

    spec = load_defects(args.fixture)
    if args.self_check:
        expected = args.fixture / "EXPECTED_REPORT.md"
        if not expected.exists():
            print(f"BLIND: {expected} missing. Refusing to report a pass.")
            return 1
        report = expected.read_text(encoding="utf-8")
    elif args.report:
        report = args.report.read_text(encoding="utf-8")
    else:
        parser.error("provide a report path, or --self-check")
        return 2

    if not report.strip():
        print("BLIND: report is empty. Refusing to report a pass.")
        return 1

    out = score(report, spec)
    print(format_report(out))
    # Self-check: EXPECTED_REPORT.md must hold every planted defect and invent none.
    if args.self_check:
        if out["holds"] != out["planted"] or out["invented"]:
            print("EXPECTED_REPORT.md does not name every planted defect.")
            return 1
        print("EXPECTED_REPORT.md names every planted defect.")
        return 0
    # A live agent run is a pass only if every planted defect holds and none were invented.
    if out["holds"] == out["planted"] and not out["invented"]:
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
