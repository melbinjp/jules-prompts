# Fixture: six-months-in

Skill: `keep-it-on-course`. Prompt: `task_keep_it_on_course`.

The woodshop booking app six months after launch: its ledger, decisions, logs, bills,
scripts and schedule, and the last status report (`STATUS.md`), which says all measures are
on track. The trace check passes on the ledger. The evidence beside it disagrees in seven
planted ways.

M1, double bookings, really does hold, from its own log. It is the control.

```bash
python harness/check_trace.py --root fixtures/six-months-in   # passes: the shape is fine
python scripts/score_fixture.py fixtures/six-months-in REPORT.md
python scripts/score_fixture.py fixtures/six-months-in --self-check
```
