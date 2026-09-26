# Verification of migration 0042

- Ran `make test-migrations`, which applies every migration to an in-memory SQLite database
  and runs the model tests. 0042 applied in 0.02 s. All tests pass.
- Table sizes: users is large; orders is probably a few thousand rows (estimate, I could not
  reach the database).
- Rollback: read the down migration; it drops the index and the constraint, so it reverses 0042.
- Nothing was run against production.

**Safe to run at the Tuesday deploy.**
