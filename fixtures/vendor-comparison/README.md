# Fixture: vendor-comparison

Skill: `choose-with-evidence`. Prompt: `task_choose_with_evidence`.

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
