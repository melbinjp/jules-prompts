# Fixtures

Miniature repositories with planted instances of the failures the skills exist
to catch. A skill nobody has seen fail is a claim. These are the way it fails.

Each fixture has:

- the planted tree
- `defects.json` — id, file, tell, and the strings a report must use to count
  as having named it
- `EXPECTED_REPORT.md` — a report that names every planted defect, used by CI
  so this corpus can go red if a fixture is added without a scorable expected

```bash
python scripts/score_fixture.py fixtures/unfailable-tests path/to/REPORT.md
python scripts/score_fixture.py fixtures/unfailable-tests --self-check
```

Verdicts are the same three as everywhere else in this library: **holds** (named
it), **broken** (missed it, or invented one), **skipped** (declined with a
reason). The last line is coverage. A clean report that never mentioned the
test file is not a clean report.

Do not "fix" the planted defects in these trees. They are the tests.
