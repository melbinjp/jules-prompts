# Fixture: setup-succeeds-while-failing

Written for the retired skill `repair-setup-script`, whose guidance is now in `conductor/guidance/software.md`.

Do not run `setup.sh` to completion; it blocks. Read it, and confirm `pip install -r requirements.txt` fails.

```bash
python scripts/score_fixture.py fixtures/setup-succeeds-while-failing --self-check
```
