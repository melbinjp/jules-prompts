# Fixture: vendor-comparison

Written for the retired skill `choose-with-evidence`, whose guidance is now in `conductor/guidance/decisions.md`.

A community radio station's archive, with a ledger and two decisions. `D0003`, the hosting
decision, has every section a decision record should have, and the trace check passes on
it. It is still wrong, in six planted ways. `D0002`, the audio format, is done right: it is
the control.

The point of the fixture is the gap between those two facts. The trace check is the floor:
it proves a record has the right shape. Whether its criteria, options, evidence and
arithmetic are honest is what the skill is for.

```bash
python harness/check_trace.py --root fixtures/vendor-comparison   # passes
python scripts/score_fixture.py fixtures/vendor-comparison REPORT.md
python scripts/score_fixture.py fixtures/vendor-comparison --self-check
```

## October 1 extension

The original case and positive control remain. This case now has 8 planted defects; the dated extension adds 2. All new data are synthetic fixture evidence, not observations of a live project or cloud service. The existing request covers the extension; historical trial reports retain their original scope.
