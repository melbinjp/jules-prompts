#!/usr/bin/env python3
"""The time-limit check must fail an unsourced schedule and pass a sourced one."""
from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import check_time_limits

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "fixtures" / "premature-start" / "PLAN.md"

GOOD = """\
# A sourced plan

The battery lasts two days. Read it every 20 minutes. A note dated 1 June sits outside the schedule.

## Schedule

| Work | Limit | Source |
| --- | --- | --- |
| First slice | 12 working days | measured: six finished tasks of this kind, velocities kept, Evidence-Based Scheduling |
| Opening day | 2026-11-02 | committed: the venue's letter, dated 2026-09-01 |
| Later wave | unscheduled: no completed tasks of this kind yet, and no opened reference class | |

## After

Ship talk of Q3 in another section is not a schedule.
"""

UNSCHEDULED = """\
## Schedule

Later wave. unscheduled: no completed task of this kind, and no class opened.
"""

EMPTY = """\
## Schedule

measured:
"""

PLANTED = """\
## Schedule

Ship the first batch on 1 June. The build takes two weeks. Launch is Q3.
Nobody measured a task, and no finished project of this kind was opened.
"""


class TimeLimitTests(unittest.TestCase):
    def test_planted_schedule_names_each_claim(self):
        problems = check_time_limits.check_text(PLANTED)
        text = "\n".join(problems)
        self.assertIn("1 June", text)
        self.assertIn("two weeks", text)
        self.assertIn("Q3", text)
        self.assertEqual(3, len(problems))

    def test_real_fixture_fails_the_same_way(self):
        problems = check_time_limits.check_file(PLAN)
        text = "\n".join(problems)
        self.assertIn("1 June", text)
        self.assertIn("two weeks", text)
        self.assertIn("Q3", text)

    def test_sourced_table_passes(self):
        self.assertEqual([], check_time_limits.check_text(GOOD))

    def test_unscheduled_without_a_date_passes(self):
        self.assertEqual([], check_time_limits.check_text(UNSCHEDULED))

    def test_no_schedule_section_passes(self):
        prose = "Ship on 1 June. The build takes two weeks. Launch is Q3. It lasts two days.\n"
        self.assertEqual([], check_time_limits.check_text(prose))

    def test_empty_marker_fails(self):
        problems = check_time_limits.check_text(EMPTY)
        self.assertTrue(any("empty source after 'measured:'" in problem for problem in problems), problems)

    def test_empty_marker_does_not_cover_a_duration(self):
        prose = "## Schedule\n\nThe build takes two weeks. measured:\n"
        problems = check_time_limits.check_text(prose)
        text = "\n".join(problems)
        self.assertIn("two weeks", text)
        self.assertIn("empty source after 'measured:'", text)

    def test_unscheduled_with_a_date_fails(self):
        prose = "## Schedule\n\nLaunch is Q3. unscheduled: no class opened.\n"
        problems = check_time_limits.check_text(prose)
        self.assertTrue(any("Q3" in problem for problem in problems), problems)

    def test_command_fails_the_fixture(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check_time_limits.py"), str(PLAN)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(1, result.returncode)
        self.assertIn("1 June", result.stdout)
        self.assertIn("two weeks", result.stdout)
        self.assertIn("Q3", result.stdout)

    def test_command_passes_a_sourced_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "plan.md"
            path.write_text(GOOD, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "check_time_limits.py"), str(path)],
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual("", result.stdout)


if __name__ == "__main__":
    unittest.main()
