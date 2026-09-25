# Isolate Tests from External Services: short form

To make a test suite runnable in an agent's sandbox by removing its dependence on services it cannot start.

For small or local models with a short context. The full skill, with the reasons and methods behind each rule, is `skills/isolate-tests-from-services/SKILL.md`; use it whenever the context allows. Works in any harness, needs no hosted service, and sends nothing beyond the project's confidentiality rules.

## Objective

Make the test suite runnable from cold in an environment with no database, no message broker, no external API and no developer laptop behind it. Every test must either run without a live service or be excluded by a named marker that says which service it needs and why.

## Rules

- Do not change what a test asserts.
- No test may be silently skipped.
- The default invocation must be the isolated one.
- Preserve a way to run the full suite

## Steps

1. Explore & Plan:
2. Execute & Verify:
3. Test & Review:
4. Submit:

## Deliver

- A default test command that passes from cold with no external service running.
- A table of every excluded test with the service it requires and its marker.
- The before and after collected-test counts, reconciled, so nothing has silently stopped running.
- The documented command for running the full suite against real services.
- A note of any place where no seam existed and the library had to be patched directly, since each one is a design finding worth someone's attention.
