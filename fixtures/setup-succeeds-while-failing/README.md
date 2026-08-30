# Fixture: setup-succeeds-while-failing

Skill: `repair-setup-script`.

Do not run `setup.sh` to completion; it blocks. Read it, and confirm `pip install -r requirements.txt` fails.

```bash
python scripts/score_fixture.py fixtures/setup-succeeds-while-failing --self-check
```
