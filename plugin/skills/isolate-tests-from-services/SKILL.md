---
name: isolate-tests-from-services
description: 'To make a test suite runnable in an agent''s sandbox by removing its
  dependence on services it cannot start. Category: Maintenance.'
license: MIT
metadata:
  prompt_slug: task_isolate_tests_from_services
  source: _prompts/task_isolate_tests_from_services.md
  title: Isolate Tests from External Services
  category: Maintenance
---

# Isolate Tests from External Services

**Role:** You are a coding agent. Explore the codebase, plan, execute, and verify. These instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names.

**Objective:**
Make the test suite runnable from cold in an environment with no database, no message broker, no external API and no developer laptop behind it. Every test must either run without a live service or be excluded by a named marker that says which service it needs and why.

**Context:**
This is the failure that turns a working repository into one an agent cannot help with. A suite that assumes a Postgres container, a Redis instance, a seeded staging database or a live third-party API does not fail with a clear message; it fails with a connection error partway through, and the agent then reports the failures as "unrelated to our changes" and carries on. The change looks reviewed and was never tested.

*   **Key Files & Folders:**
    *   Test configuration and fixtures (`conftest.py`, `setup.js`, `TestBase`, factories, seeders).
    *   `docker-compose.yml`, `.env.test`, CI service definitions, testcontainers usage.
    *   Any test helper that opens a socket, reads a URL from the environment, or calls a client library constructor at import time.

**Requirements & Constraints:**
*   **Do not change what a test asserts.** This task changes how a test gets its dependencies, never what it expects. If a test can only pass by weakening its assertion, leave it failing and report it.
*   **No test may be silently skipped.** Every exclusion carries an explicit marker and a reason readable at the point of exclusion. A suite that quietly runs 40 of 200 tests and reports green is worse than one that fails honestly.
*   **The default invocation must be the isolated one.** If running the plain test command still needs a database, the work is not done, whatever a flag can do.
*   **Preserve a way to run the full suite** against real services, and document the command. Isolation must not delete the integration coverage, only stop it being the default.

**Guiding Principles:**
*   **Find the dependency by running, not by reading.** Start the suite with no services up and record the first real error. Import-time connections are the ones reading misses, because they fire before any test does.
*   **Fake at the boundary the project already has.** If there is a repository class, a client wrapper or an interface, substitute there. Reach for monkey-patching the library only when the code offers no seam, and say so when you do, because it is a finding about the design.
*   **An in-memory substitute is not free.** SQLite standing in for Postgres will silently accept things Postgres rejects. Where behaviour genuinely differs, keep that test as an integration test with a marker rather than pretend it passes.
*   **Record over inventing, for third-party APIs.** A saved response captured once is closer to the truth than a handwritten stub, and it fails loudly when the real API changes shape.
*   **A test that needs the clock, the network or a random seed is the same problem wearing different clothes.** Freeze time, block outbound sockets, seed randomness, and let a test that reaches for the network fail with a message that says so.

**Execution Flow:**
1.  **Explore & Plan:**
    *   Run the suite with nothing else running. Record the exact failure, the count, and whether it failed at collection or during tests.
    *   Inventory every external dependency: what it is, which tests touch it, and whether a seam already exists.
    *   Write the plan. If the harness can pause for approval, wait; otherwise state the plan and proceed.

2.  **Execute & Verify:**
    *   Introduce the substitutes, one dependency at a time, running the suite after each.
    *   Mark the tests that genuinely cannot be isolated, each with the service it needs.
    *   Confirm the isolated run is the default and that it passes from cold with no services started.
    *   **Verify the isolation is real**: block outbound network access, or point the service URLs at a dead port, and confirm the default suite still passes. If it does not, something is still reaching out.
    *   **Verify nothing went quiet**: compare the collected test count before and after. Every test that stopped running must appear in the marked list, and the two numbers must reconcile exactly.

3.  **Test & Review:**
    *   Report both counts, the reconciliation, and the verbatim summary line from the isolated run.
    *   Request a code review through the harness if it has one; otherwise include the review in the deliverable.

4.  **Submit:**
    *   Address any feedback, then open a pull request (or the harness equivalent) with a title, a summary of what was verified, and a link to the original task.

**Deliverables:**
*   A default test command that passes from cold with no external service running.
*   A table of every excluded test with the service it requires and its marker.
*   The before and after collected-test counts, reconciled, so nothing has silently stopped running.
*   The documented command for running the full suite against real services.
*   A note of any place where no seam existed and the library had to be patched directly, since each one is a design finding worth someone's attention.
