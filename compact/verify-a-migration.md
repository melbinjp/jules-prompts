# Verify a Database Migration Before It Meets Real Data: short form

To find what a migration does at production row counts, on the production engine, and on the way back down, none of which a dev database can show you.

For small or local models with a short context. The full skill, with the reasons and methods behind each rule, is `skills/verify-a-migration/SKILL.md`; use it whenever the context allows. Works in any harness, needs no hosted service, and sends nothing beyond the project's confidentiality rules.

## Objective

Take a pending database migration and establish what it will actually do to production: how long it runs at real row counts, what it locks while it runs, whether the rollback works, and whether old application code survives the new schema. Report timings and lock behaviour as measurements, not estimates.

## Rules

- Measure on the production engine and version, seeded to production row counts.
- If you cannot obtain real row counts, stop and say so.
- Run the rollback. Do not read it.
- Record the lock each statement takes and for how long.
- Do not touch production. Every measurement here happens on a copy.
- Do not fix the migration and then report it as safe.

## Steps

1. Explore & Plan:
2. Execute & Verify:
3. Test & Review:
4. Submit:

## Deliver

- A table of every statement in the migration with the row count it ran against, its duration, and the lock it held.
- The schema diff after a full down-and-up round trip, stated as identical or with the differences listed.
- For each added constraint, the number of rows in production-shaped data that would violate it.
- The safe deploy order, with the evidence: which of old-code-new-schema and new-code-old-schema actually worked.
- Whatever could not be measured, named explicitly, with the reason and what remains unknown because of it.
