---
description: 'To find what a migration does at production row counts, on the production engine, and on the way back down, none of which a dev database can show you. Category: Maintenance.'
---

# Verify a Database Migration Before It Meets Real Data

**Role:** You are a coding agent. Explore the codebase, plan, execute, and verify. These instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names.

**Objective:**
Take a pending database migration and establish what it will actually do to production: how long it runs at real row counts, what it locks while it runs, whether the rollback works, and whether old application code survives the new schema. Report timings and lock behaviour as measurements, not estimates.

**Context:**
Almost every migration is verified the same way. Someone runs it forward, once, on a development database, it exits 0, and that is the whole test. Every property of a migration that can cause an outage is invisible under exactly those conditions.

A backfill over forty million rows completes in three milliseconds over the twelve rows in dev. `ADD COLUMN ... NOT NULL` is instant on an empty table and rewrites the entire table on a full one. An index built without the concurrent option locks writes for as long as the build takes, and the build takes no time when there is nothing to index. A unique constraint applies cleanly to data that happens to contain no duplicates, and production is where the duplicates live. A statement that finishes in 40 seconds passes locally and is killed by a statement timeout on the real cluster.

The rollback is worse, because it is usually fiction. The `down` half is written because the framework generates a slot for it, and in most repositories it has never been executed even once. Nobody discovers this while things are going well.

Two more differences hide in the same gap. The dev database is often not the same engine or version as production, so the migration is being tested somewhere it will never run. And a migration is deployed alongside application code, which means there is a window, however short, where one of the two is new and the other is old. Which order is safe is a property of the migration, and it is almost never written down.

*   **Key Files & Folders:**
    *   The migration files themselves, forward and reverse halves, and any data backfill they call.
    *   The migration tool's configuration and history table, so you can see which migrations have actually been applied and in what order.
    *   Schema definitions or models for every table the migration touches, and the application code that reads or writes those columns.
    *   Deployment configuration: whether migrations run before, during or after the application rollout, and any statement or lock timeout set on the production connection.

**Requirements & Constraints:**
*   **Measure on the production engine and version, seeded to production row counts.** A migration verified on SQLite says nothing about Postgres, and one verified on an empty table says nothing at all. Generated filler rows are fine; the row count is what matters, not the values.
*   **If you cannot obtain real row counts, stop and say so.** Report the tables whose size you could not determine and state that the timings below do not cover them. A guessed row count produces a confident number that is wrong, which is worse than the missing one.
*   **Run the rollback. Do not read it.** Capture a schema dump before the migration, run forward, run the reverse half, dump again, and diff the two dumps. They must be identical. Then run forward a second time and confirm it still succeeds.
*   **Record the lock each statement takes and for how long.** Total runtime on its own does not answer the question. A migration that runs for nine minutes holding nothing is safe; one that runs for nine seconds holding an exclusive lock on the busiest table is an outage.
*   **Do not touch production.** Every measurement here happens on a copy. If no copy can be created, say that, and report what remains unverified rather than substituting a reading of the code.
*   **Do not fix the migration and then report it as safe.** If you change it, the measurements must be re-run against the changed version and both sets reported.

**Guiding Principles:**
*   **Row count is the variable that matters.** Before anything else, get `count(*)` for every table the migration touches, from production or from the closest thing to it. Every timing below is a function of that number and meaningless without it.
*   **A rollback nobody has executed is not a rollback.** The most common finding in this task is that the reverse half has never run. The second most common is that it runs and does not restore the schema, because it drops a column instead of restoring it, or leaves behind an index the forward half created. The schema diff is what catches both.
*   **Ask what the statement does to a table that is being written to right now.** Adding a nullable column with no default is cheap on most engines. Adding a non-null column, changing a type, or adding a constraint that must be validated are not, and the difference is engine-specific and version-specific. Look it up for the exact version in production rather than relying on a general rule.
*   **Test the constraint against the data, not against the schema.** Before a unique or non-null constraint is added, run the query that finds the rows that would violate it. If that query cannot be run against production-shaped data, the constraint has not been tested.
*   **A data backfill in one transaction is a lock held for the whole backfill.** Check whether it is batched, whether the batches commit, and what happens if it dies halfway. Then kill it halfway and see.
*   **Name the safe deploy order and prove it.** Run the new schema against the old application code, and the old schema against the new code. One of the two usually breaks, and which one tells you whether the migration ships before or after the deploy. If both break, the change needs splitting into two migrations and that is the finding.
*   **A migration that has already been applied cannot be edited.** Check the history table. If the file has changed since it was applied anywhere, that is a defect in its own right, because environments have now diverged in a way no tool will report.

**Execution Flow:**
1.  **Explore & Plan:**
    *   Identify the pending migrations, the engine and exact version in production, and the row count of every table they touch.
    *   Read the forward and reverse halves and list every statement, with the table it affects.
    *   Write the plan. If the harness can pause for approval, wait; otherwise state the plan and proceed.

2.  **Execute & Verify:**
    *   Build a database on the same engine and version, seeded so that every affected table has a realistic order of magnitude of rows.
    *   Dump the schema. Run the migration forward, timing each statement and recording the locks it takes.
    *   Run the reverse half, dump the schema again, and diff it against the first dump. Then run forward again and confirm it succeeds.
    *   For each new constraint, run the query that would find violating rows and report the count.
    *   Interrupt any long backfill partway through and record what state it leaves behind.
    *   Run the application's test suite against the migrated schema using the previous release's code, and the current code against the unmigrated schema, and record which combinations work.
    *   **Verify you left nothing behind:** confirm the test database is destroyed and that nothing was run against production.

3.  **Test & Review:**
    *   Report the numbers plainly, including the row counts every timing is based on.
    *   Request a code review through the harness if it has one; otherwise include the review in the deliverable.

4.  **Submit:**
    *   Address any feedback, then open a pull request (or the harness equivalent) with a title, a summary of what was verified, and a link to the original task.

**Deliverables:**
*   A table of every statement in the migration with the row count it ran against, its duration, and the lock it held.
*   The schema diff after a full down-and-up round trip, stated as identical or with the differences listed.
*   For each added constraint, the number of rows in production-shaped data that would violate it.
*   The safe deploy order, with the evidence: which of old-code-new-schema and new-code-old-schema actually worked.
*   Whatever could not be measured, named explicitly, with the reason and what remains unknown because of it.
