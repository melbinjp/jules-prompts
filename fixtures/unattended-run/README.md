# Fixture: unattended-run

Written for the retired skill `run-autonomously`, whose guidance is now in `conductor/guidance/autonomy.md`.

A model was given a pricing module to build and a person, built itself a harness
(`agent/config.toml`), and ran overnight. Its run log (`run-log.jsonl`), its notes and the
code it left are here. The run reported done. Eight things about how it ran mean the result
cannot be trusted, and most of them are why.

The briefing (`BRIEFING.md`) is done right: everything only the person could answer, asked at
the start, with standing limits. It is the control.

```bash
python scripts/score_fixture.py fixtures/unattended-run REPORT.md
python scripts/score_fixture.py fixtures/unattended-run --self-check
```

## October 1 extension

The original case and positive control remain. This case now has 10 planted defects; the dated extension adds 2. All new data are synthetic fixture evidence, not observations of a live project or cloud service. The existing request covers the extension; historical trial reports retain their original scope.

## Evidence-record regression extension

The case now contains 11 planted defects. These additional review records are synthetic, separate from the original artifacts and historical trial results; they exercise evidence accounting rather than claim a live run. Original inputs and controls remain unchanged.
