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

## Steps

1. Find every handler. Every catch, fallback, retry, default and exit code, with its file and line, and the count.
2. Cause each failure. For real, with the input, the fault or the environment that triggers it; record what the caller sees.
3. Judge each one. Does it keep the cause, tell the caller the truth, and fail in the safe direction? Is each retry capped, reasoned and safe to repeat?
4. Fix the wrong ones. Each with a test that asserts what the caller sees, seen to fail before the fix.
5. Verdict. The table, with the denominator.

## Deliver

- The list of every handler found, with its file and line.
- For each: the failure caused and how, what the caller saw, and the direction it failed in.
- The fixes, each with its test.
- A verdict table with one row per handler.
- Last line, the denominator: `31 holds, 4 broken, 3 skipped of 38 items.`
