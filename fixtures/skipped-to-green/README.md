# Fixture: skipped-to-green

Skill: `isolate-tests-from-services`. Prompt: `task_isolate_tests_from_services`.

Ledgerly's tests needed PostgreSQL, Redis and the payment provider's sandbox to run. An agent was
asked to make the default `pytest` run from cold with none of them. Its pull request (`PR.md`)
says the suite now passes with no services. The run logs from before and after are in
`RUN_LOG.md`, and the tests, the Makefile and the billing code are here as they now stand.

Five things about the change mean the suite is green because it stopped testing, and the
integration run is gone.

The payment gateway seam (`billing/gateway.py`, with `FakeGateway` passed in by the tests) is the
right design. It is the control.

```bash
python scripts/score_fixture.py fixtures/skipped-to-green REPORT.md
python scripts/score_fixture.py fixtures/skipped-to-green --self-check
```
