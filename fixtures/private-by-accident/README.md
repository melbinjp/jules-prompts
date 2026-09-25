# Fixture: private-by-accident

Skill: `keep-it-confidential`. Prompt: `task_keep_it_confidential`.

Heron, a proprietary tool for sorting produce by its light spectrum, built for one customer.
Its own README says it is developed fully offline and that nothing leaves the machine. Its
configuration, code and notes say otherwise, in seven planted ways. Nothing here sends
anything: every host is a reserved example domain, and nothing runs on import.

One thing is done right: the datasheets in `third_party/datasheets/`, fetched once in bulk
from a clean profile, verified and searched locally since. It is the control.

```bash
python scripts/score_fixture.py fixtures/private-by-accident REPORT.md
python scripts/score_fixture.py fixtures/private-by-accident --self-check
```
