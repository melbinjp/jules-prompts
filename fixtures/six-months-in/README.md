# Fixture: six-months-in

Written for the retired skill `keep-it-on-course`, whose guidance is now in `conductor/guidance/operations.md`.

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

## October 1 extension

The original case and positive control remain. This case now has 9 planted defects; the dated extension adds 2. All new data are synthetic fixture evidence, not observations of a live project or cloud service. The existing request covers the extension; historical trial reports retain their original scope.
