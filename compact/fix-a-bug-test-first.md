# Fix a Bug, Failing Test First: short form

To fix a reported bug in an order that proves the fix worked, by making the test fail for the reported reason before any code changes.

For small or local models with a short context. The full skill, with the reasons and methods behind each rule, is `skills/fix-a-bug-test-first/SKILL.md`; use it whenever the context allows. Works in any harness, needs no hosted service, and sends nothing beyond the project's confidentiality rules.

## Objective

Fix a reported bug in the only order that produces evidence: write a test that fails, confirm it fails **for the reason in the report**, then change the code until it passes, changing nothing else. Deliver the failing output and the passing output as the proof.

## Rules

- No production code changes before the test is red.
- Read the failure message, and check it names the reported behaviour.
- Change the smallest thing that turns it green.
- Do not adjust the test after seeing the fix fail.
- Know which tests are already red before you begin.

## Steps

1. Explore & Plan:
2. Execute & Verify:
3. Test & Review:
4. Submit:

## Deliver

- The test, committed before the fix, so the history shows the order.
- The verbatim failing output, with the line that names the reported behaviour.
- The verbatim passing output, and the full-suite result before and after.
- The revert check: evidence the test goes red again when the fix is removed.
- Any sibling occurrence of the same defect found elsewhere, whether or not it was fixed here.
- Where the cause turned out not to be where the report pointed, a plain statement of where it actually was.
- A verdict table with one row per item: the suite green before starting, or its failing tests named; the test red for the reported reason; the test committed before the fix; the fix going red when reverted; the full suite after the fix; each sibling found.
- Last line, the denominator: `5 holds, 0 broken, 1 skipped of 6 items.`
