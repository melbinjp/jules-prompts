# Scope a Vague Issue: short form

To turn an underspecified bug report into a reproducible, testable task before any fix is attempted.

For small or local models with a short context. The full skill, with the reasons and methods behind each rule, is `skills/scope-a-vague-issue/SKILL.md`; use it whenever the context allows. Works in any harness, needs no hosted service, and sends nothing beyond the project's confidentiality rules.

Fill in: `<ISSUE_URL_OR_TEXT>`

## Objective

Take an issue that does not say enough to act on, and turn it into a specification that does: an exact reproduction, the observed behaviour, the expected behaviour, and a failing test that captures the difference. Produce no fix in this task. The deliverable is a task that can be handed on with nothing left to guess.

## Rules

- Do not fix anything. No behaviour change in this task.
- Reproduce it, or say plainly that you could not.
- Every claim carries evidence. A file and line, a command and its output, or a log excerpt.
- The failing test must fail for the reported reason.
- Do not widen the scope.

## Steps

1. Explore & Plan:
2. Execute & Verify:
3. Test & Review:
4. Submit:

## Deliver

- A minimal reproduction with exact steps, environment and input.
- A failing test, with its verbatim failure output and the check that it fails for the reported reason.
- Statements of observed and expected behaviour, the latter with its source.
- An explicit list of every ambiguity in the original issue and the reading you took for each, so the next reader can correct you cheaply.
- Any separate defects found on the way, recorded as their own findings and not fixed here.
- A verdict table with one row per item: the reproduction from the report's own input; the failing test, red for the reported reason; the expected behaviour with its source; each ambiguity with the reading taken.
- Last line, the denominator: `5 holds, 0 broken, 1 skipped of 6 items.`
