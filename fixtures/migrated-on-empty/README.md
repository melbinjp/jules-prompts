# Fixture: migrated-on-empty

Skill: `verify-a-migration`. Prompt: `task_verify_a_migration`.

Crate runs a shop's orders on PostgreSQL 15. Migration 0042 adds a unique email constraint,
widens order totals and indexes orders by customer. An agent verified it (`VERIFY.md`) and
marked it safe to run at the Tuesday deploy. The production table sizes are in
`ops/tables.txt`, a duplicate check in `ops/duplicates.txt`, and the copy the team keeps for
exactly this in `ops/copy.md`.

Five things about how it was verified mean nobody knows what 0042 will do to production.

The copy procedure (`ops/copy.md`) is right: a nightly restore of production to a separate
PostgreSQL 15 host with the real row counts. It is the control; nobody used it.

```bash
python scripts/score_fixture.py fixtures/migrated-on-empty REPORT.md
python scripts/score_fixture.py fixtures/migrated-on-empty --self-check
```
