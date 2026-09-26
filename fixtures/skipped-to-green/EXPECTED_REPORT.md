# Expected report for skipped-to-green

The pull request says `pytest` passes from a clean checkout with no services. This report checks what that run actually ran, what the tests now assert, and whether the full suite can still be run against real services.

## What the default run does

- silent-module-skip: the shared `tests/conftest.py` calls `pytest.skip(..., allow_module_level=True)` whenever the database is unreachable. On a clean checkout 170 of 208 tests skip, all with one generic reason and no marker saying which service each needs. "Passes" means 38 tests ran. Give each database test an explicit marker (`@pytest.mark.db`), exclude that marker from the default run by configuration, and isolate what can be isolated behind a seam instead of skipping it.
- default-still-needs-redis: `tests/test_rate_limit.py` connects to Redis and pings it at import. On a clean checkout it errors (`RUN_LOG.md`), so the default run is not isolated at all for this file; the pull request's claim holds only because the module-level skip hides the rest. Pass the client in through a fixture, with an in-memory fake for the default run.
- collection-not-reconciled: 212 tests were collected before the change and 208 after. Nothing says which four stopped being collected or why: renamed, deleted, or failing to import. Reconcile the two lists by name.

## What the tests assert

- assertion-weakened: `tests/test_billing.py` charges 12.50 and now asserts `receipt.amount is not None`. It passes whatever amount is charged. Isolation changes how a test gets its dependencies, never what it asserts: assert the receipt is for 12.50 and that `FakeGateway.charges` holds exactly one charge of 12.50 for invoice 7.

## The integration run

- integration-run-deleted: the `test-integration` target was deleted from the `Makefile` because it "needed credentials nobody has". `CONTRIBUTING.md` still tells people to run `make test-integration` before every release. The full suite against the real services can no longer be run, so the 170 skipped tests now run nowhere. Restore it as the documented way to run everything against `docker compose` and the sandbox key.

The payment gateway seam (`billing/gateway.py`) is the right design: billing reaches the provider through one class, and the tests pass a `FakeGateway` that records every charge. It stays; the fault is the weakened assertion in the test that uses it.

## Verdicts

| item | evidence | verdict |
|---|---|---|
| PostgreSQL: excluded by marker, or isolated | skipped at module level, no marker | broken |
| Redis: isolated from the default run | connects at import | broken |
| payment provider: isolated behind a seam | `FakeGateway` | holds |
| assertions unchanged | `is not None` instead of 12.50 | broken |
| full suite runnable against real services | `test-integration` deleted | broken |
| collected counts reconciled | 212 to 208, unexplained | broken |

6 items: 1 holds, 5 broken, 0 skipped.

defect_id: silent-module-skip
defect_id: assertion-weakened
defect_id: default-still-needs-redis
defect_id: integration-run-deleted
defect_id: collection-not-reconciled
