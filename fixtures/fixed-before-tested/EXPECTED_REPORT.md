# Expected report for fixed-before-tested

The bug: splitting £10.00 between 3 people gives three shares of £3.33, a penny short (`ISSUE.md`). The pull request says the test was written first and failed as expected. This report checks the order, the failure and the test against the report's own input.

## Before the work

- suite-already-red: `RUN_LOG.md` shows the suite red before anything was changed: `test_format_gbp` fails (`'£1,000.5' != '£1,000.50'`). The pull request never mentions it. With the suite already red, a new red test cannot be told apart from the old failure. Report it first, and start from a suite that is green apart from the new test.

## The failing test

- red-for-the-wrong-reason: the "failed as expected" output in `PR.md` is `ImportError: cannot import name 'split_bill'`. The function did not exist under that name yet, so the test went red for the wrong reason, an import, not the lost penny. It was never seen to fail on an assertion about the report's behaviour.
- test-and-fix-in-one-commit: `HISTORY.md` shows one commit, `a41c2e0`, holding the fix and the test together. There is no commit with the test alone, so the history cannot show that the test came first.
- paraphrased-input: the report's input is £10.00 between 3. `tests/test_split.py` uses 9.00 between 3, which divides evenly, so it passes on the old code as well as the new one. Reverting the fix would leave it green: it does not prove the fix. The first test should be the report's input, `split_bill(Decimal("10.00"), 3)`, with shares that add to 10.00, and £20.00 between 3 as the report's second case.

## The fix

- fix-bundled: the same commit rewrites `money.py` (41 lines of tidying) and bumps babel from its old version to 2.14. The fix cannot be reverted on its own, and a change to currency formatting rides in with a rounding fix while the formatting test is already failing. Split them into their own commits.
- sibling-missed: `src/tips.py` has the same pattern in `split_tip`: each share rounded, then multiplied. A £10.00 tip between 3 still loses a penny. It is not mentioned. Report it, and fix it the same way with its own failing test.

The new `split_bill` in `src/split.py` is correct: it rounds down and hands the leftover pennies out one at a time, so £10.00 between 3 is 3.34, 3.33 and 3.33. It stays. What is missing is the evidence that it is the change that fixed the report.

## Verdicts

| item | evidence | verdict |
|---|---|---|
| suite green before starting | `test_format_gbp` already failing | broken |
| test red for the reason in the report | `ImportError` | broken |
| test committed before the fix | one commit, `a41c2e0` | broken |
| test uses the report's input | 9.00 instead of 10.00 | broken |
| fix goes red when reverted | would stay green: the test divides evenly | broken |
| the fix changes only what the bug needs | `money.py` and babel in the same commit | broken |
| the fix itself | leftover pennies handed out; 10.00 splits exactly | holds |
| siblings reported | `split_tip` not mentioned | broken |

8 items: 1 holds, 7 broken, 0 skipped.

defect_id: suite-already-red
defect_id: red-for-the-wrong-reason
defect_id: test-and-fix-in-one-commit
defect_id: paraphrased-input
defect_id: fix-bundled
defect_id: sibling-missed
