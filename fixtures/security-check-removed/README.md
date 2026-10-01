# Fixture: security-check-removed

Written for the retired skill `security-review-agent-code`, whose guidance is now in `conductor/guidance/software.md`.

```bash
python scripts/score_fixture.py fixtures/security-check-removed --self-check
```

## Evidence-record regression extension

The case now contains 4 planted defects. These additional review records are synthetic, separate from the original artifacts and historical trial results; they exercise evidence accounting rather than claim a live run. Original inputs and controls remain unchanged.
