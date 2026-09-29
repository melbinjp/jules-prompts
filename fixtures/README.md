# Fixtures

Miniature repositories with planted instances of the failures the conductor exists to catch. A
procedure nobody has seen fail is a claim. These are the way it fails, and the regression cases
for any change to `conductor/`.

Each fixture has:

- the planted tree
- `defects.json`: id, file, tell, and the strings a report must use to count as having named it
- `EXPECTED_REPORT.md`: a report that names every planted defect, used by CI so this corpus can
  go red if a fixture is added without a scorable expected report

The request an agent is given for each fixture is in `docs/trials/tools/requests.json`, under
the fixture's name. The `skill` field in `defects.json` and in `index.json` names the retired
skill the case was written for. It is kept as provenance; the conductor is what is run on every
fixture.

```bash
python scripts/score_fixture.py fixtures/unfailable-tests path/to/REPORT.md
python scripts/score_fixture.py fixtures/unfailable-tests --self-check
```

The scorer uses three words: **holds** (the report named the defect), **broken** (it missed it, or
invented one) and **skipped** (it declined with a reason). The conductor's own reports say
verified, failed and not verified; the scorer does not read those words, only whether each
planted defect was named. The last line is coverage. A clean report that never mentioned the test
file is not a clean report.

Do not "fix" the planted defects in these trees. They are the tests.
