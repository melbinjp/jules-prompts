# test: run the suite without external services

- Tests that need the database now skip when it is not there.
- Billing tests use a fake gateway instead of the sandbox.
- Removed the old integration target from the Makefile; it needed credentials nobody has.

`pytest` passes from a clean checkout with no services running.
