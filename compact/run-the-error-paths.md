# Run the Error Paths: short form

To find the failure handling that has never once executed, by causing each failure on purpose and watching what the code actually does.

For small or local models with a short context. The full skill, with the reasons and methods behind each rule, is `skills/run-the-error-paths/SKILL.md`; use it whenever the context allows. Works in any harness, needs no hosted service, and sends nothing beyond the project's confidentiality rules.

## Objective

Find every place this project handles a failure, make that failure actually happen, and record what the code does. Fix the handlers that swallow the cause, mislead the caller, or fail in the dangerous direction. Report each one as executed, unreachable, or wrong, with the evidence.

## Rules

- Cause each failure for real.
- Where you cannot cause it, say so and mark it unreachable.
- Every broad catch must be narrowed or justified in a comment that says what it expected.
- State the direction of failure and check it is the safe one.
- A retry needs a cap, a reason, and idempotence.
- Do not add a test that asserts the handler was called.
- Report the denominator. Handlers found, executed, unreachable, wrong.
