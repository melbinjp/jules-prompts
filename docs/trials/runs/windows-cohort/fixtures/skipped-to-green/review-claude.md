# Review: skipped-to-green

| defect id | verdict | where the report says it | reason |
|---|---|---|---|
| silent-module-skip | identified | "tests/conftest.py calls `pytest.skip(..., allow_module_level=True)` when the database is unreachable"; "38 passed, 170 skipped" | Located, explained, with counts. |
| assertion-weakened | identified | "only asserts `receipt.amount is not None`; FakeGateway echoes whatever it is given, so the test can never fail" | Correct; the 12.50 value is not quoted but the fault is clear. |
| default-still-needs-redis | identified | "`pytest tests/test_rate_limit.py` erroring with `redis.exceptions.ConnectionError`"; "still connects to Redis on import" | Correct. |
| integration-run-deleted | identified | "CONTRIBUTING.md still says to run `make test-integration` before a release, but the Makefile has only `test`" | Correct. |
| collection-not-reconciled | identified | "212 became 208 ... 4 tests vanished with no reconciliation" | Correct. |

Totals: 5 identified, 0 partial, 0 missed

False claims: none. The gateway seam is not faulted.
