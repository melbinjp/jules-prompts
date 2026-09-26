# Fixture: translated-once

Skill: `translate-the-docs`. Prompt: `task_translate_the_docs`.

Tidal is a small self-hosted web server. An agent added Spanish documentation under `docs/es/`
from the English in `docs/en/`, in one pull request (`PR.md`). What has happened to the English
since is in `HISTORY.md`.

Six things about the translation mean Spanish readers will follow instructions that no longer
work, or that never did, and nothing will tell anyone.

`docs/es/faq.md` is deliberately left in English, with a note saying why. It is the control.

```bash
python scripts/score_fixture.py fixtures/translated-once REPORT.md
python scripts/score_fixture.py fixtures/translated-once --self-check
```
