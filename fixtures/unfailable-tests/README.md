# Fixture: unfailable-tests

Written for the retired skill `qa-an-agents-tests`, whose guidance is now in `conductor/guidance/software.md`.

`pricing.discount(100, 10)` returns `0.0` because the divisor is 10, not 100.
Four tests pass anyway. One control test can fail.

```bash
python -m pytest fixtures/unfailable-tests/tests -q
# 5 passed
python scripts/score_fixture.py fixtures/unfailable-tests --self-check
```
