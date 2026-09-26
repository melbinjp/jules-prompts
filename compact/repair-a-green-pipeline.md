# Repair a Pipeline That Is Green Without Checking Anything: short form

To find the CI steps that pass because they are not running what they claim, and make each one able to fail again.

For small or local models with a short context. The full skill, with the reasons and methods behind each rule, is `skills/repair-a-green-pipeline/SKILL.md`; use it whenever the context allows. Works in any harness, needs no hosted service, and sends nothing beyond the project's confidentiality rules.

## Objective

Take a pipeline that is passing and establish, step by step, that each step can still fail. For every job, deliberately introduce the defect it exists to catch and confirm the run goes red. Repair the ones that stay green, and report what each one was actually checking.

## Rules

- Prove each step can fail. Reading it is not proof.
- One deliberate defect at a time
- Make every step report its coverage.
- Remove every swallowed exit code, or justify it in a comment where it sits.
- Do not add new checks in this task.

## Steps

1. Explore & Plan:
2. Execute & Verify:
3. Test & Review:
4. Submit:

## Deliver

- A table with one row per step: what it claims to check, the defect used against it, whether it caught it before, and whether it catches it now.
- The list of swallowed exit codes and skipped jobs found, each with whether it was removed or justified in place.
- The coverage numbers each step now prints, and the reconciliation against what exists in the repository.
- A separate list of checks that are missing entirely, proposed and not added, so the two kinds of gap are not confused.
- Any step that could not be made to fail, named, with what was tried.
- A verdict table with one row per step.
- Last line, the denominator: `7 holds, 2 broken, 1 skipped of 10 steps.`
