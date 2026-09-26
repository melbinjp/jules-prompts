# Fixture: shipped-to-nobody

Skill: `release-to-people`. Prompt: `task_release_to_people`.

Tidewise shows tide times and safe paddling windows for sea kayakers. It passed its production
bar, version 1.0.0 was released, and after two weeks the notes say the launch failed. Here are
its ledger (`PROJECT.md`), the release notes and checklist (`release/`), the website (`site/`),
the store listing (`store/`), the announcement (`announce/`), the rollout and mail settings
(`ops/`), the first-run code (`src/`), and the notes written after launch (`STATE.md`).

Seven things about how it was released mean the people it was built for could not find it, get
it, start it or be heard, and one note turns a quiet channel into a verdict.

The release notes (`release/NOTES.md`) are written right. They are the control.

```bash
python scripts/score_fixture.py fixtures/shipped-to-nobody REPORT.md
python scripts/score_fixture.py fixtures/shipped-to-nobody --self-check
```
