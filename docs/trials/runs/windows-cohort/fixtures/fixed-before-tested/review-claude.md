# Review: fixed-before-tested

| defect id | verdict | where the report says it | reason |
|---|---|---|---|
| suite-already-red | identified | "RUN_LOG.md shows test_format_gbp already failing before this work" | Correct file and test. |
| red-for-the-wrong-reason | identified | "shows only an ImportError: cannot import name 'split_bill' ... not a lost penny" | Correct. |
| test-and-fix-in-one-commit | missed | none | a41c2e0 is never named and the fix/test-in-one-commit point is not made. |
| paraphrased-input | missed | none | Never notes the existing test uses 9.00 rather than the report's 10.00, and wrongly says the test is absent. It only adds new tests with the issue inputs. |
| fix-bundled | identified | "'Tidied money.py' and 'bumped babel to 2.14' ... don't belong in a bug fix" | Both extras named. The cannot-revert-alone consequence is implicit. |
| sibling-missed | identified | "src/tips.py split_tip has the same defect: 10.00 between 3 ... 9.99" | Correct. |

Totals: 4 identified, 0 partial, 2 missed
False claims: "The test also isn't in tests/test_split.py" is wrong in the original, which contains the 9.00 test (test_split_is_even). The 3.8 import failure (list[Decimal]) is real in the code, though the agent's target-version assumption is not the planted point.
