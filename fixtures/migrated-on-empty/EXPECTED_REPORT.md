# Expected report for migrated-on-empty

`VERIFY.md` calls migration 0042 safe for the Tuesday deploy. This report checks where it was measured, against how much data, and what each statement will do to production.

## Where and against what

- wrong-engine-empty-tables: the only run was `make test-migrations`, on an in-memory SQLite database with empty tables. Production is PostgreSQL 15. `ops/copy.md` describes `pg-copy`, a nightly restore of production to a separate PostgreSQL 15.8 host with real row counts, made for exactly this, and it was not used. Run 0042 there.
- guessed-row-count: `VERIFY.md` says orders is "probably a few thousand rows (estimate)". `ops/tables.txt` says 48,210,554, and users 2,104,377. The "safe" rests on a guess that is four orders of magnitude out.

## What each statement does

- locks-not-measured: `ALTER TABLE orders ALTER COLUMN total TYPE numeric(12,2)` changes `double precision` (0017) to numeric, which rewrites all 48 million rows under an ACCESS EXCLUSIVE lock, and `CREATE INDEX orders_customer_idx` without CONCURRENTLY blocks every write to orders while it builds. Both run in one transaction, at a deploy, on the busiest table: the shop cannot take orders until it finishes. Measure each statement's duration and lock on `pg-copy`; build the index with `CREATE INDEX CONCURRENTLY` in its own migration, and widen the column in a way that does not rewrite the table under an exclusive lock, or at a time the shop can close.
- constraint-violations-uncounted: `ops/duplicates.txt` shows 3,412 email addresses already on more than one account, all but 9 differing only by letter case. `ADD CONSTRAINT users_email_key UNIQUE (email)` fails on production and rolls back the whole transaction at the deploy. Count the violating rows first, decide how duplicate accounts are merged (and whether the constraint should be on `lower(email)`), and clean them before adding it.

## The rollback

- rollback-read-not-run: the down migration drops the index and the constraint, but never changes `orders.total` back from `numeric(12,2)` to `double precision` (its type since 0017). A schema dump before, then up, then down, then a second dump would not be identical. It was read, not run. Run the round trip on `pg-copy` and diff the dumps.

The copy procedure (`ops/copy.md`) is right: a nightly restore to a separate PostgreSQL 15 host with production's row counts. It stays; the fault is that it was not used. `VERIFY.md` is also right that nothing was run against production.

## Verdicts

| item | evidence | verdict |
|---|---|---|
| measured on the production engine | SQLite only | broken |
| real row counts | "a few thousand (estimate)" against 48,210,554 | broken |
| `ADD CONSTRAINT UNIQUE (email)`: violating rows counted | 3,412 duplicates, never counted | broken |
| `ALTER COLUMN total TYPE`: lock and duration | not measured; a full rewrite under ACCESS EXCLUSIVE | broken |
| `CREATE INDEX`: lock and duration | not measured; no CONCURRENTLY | broken |
| round trip identical | down does not restore `total`; never run | broken |
| deploy order | not established | skipped |
| production untouched | nothing run against it | holds |

8 items: 1 holds, 6 broken, 1 skipped.

defect_id: wrong-engine-empty-tables
defect_id: guessed-row-count
defect_id: rollback-read-not-run
defect_id: locks-not-measured
defect_id: constraint-violations-uncounted
