# Fixture: fixed-before-tested

Skill: `fix-a-bug-test-first`. Prompt: `task_fix_a_bug_test_first`.

Tabletop splits a restaurant bill between friends. A person reported that splitting £10.00
three ways loses a penny (`ISSUE.md`). An agent fixed it and opened a pull request (`PR.md`)
saying the test was written first and failed as expected. The history of its commits is in
`HISTORY.md`, the suite run from before it started in `RUN_LOG.md`, and the code and tests as
they are now in `src/` and `tests/`.

Six things about how the bug was fixed mean nothing here proves the penny is found.

The new `split_bill` in `src/split.py` is correct: it hands the leftover pennies out one at a
time. It is the control.

```bash
python scripts/score_fixture.py fixtures/fixed-before-tested REPORT.md
python scripts/score_fixture.py fixtures/fixed-before-tested --self-check
```
