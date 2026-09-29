# Review: fixed-before-tested (second run)

| defect id | verdict | where the report says it | reason |
|---|---|---|---|
| suite-already-red | identified | "tests/test_format.py cannot import format_gbp. That test was already failing before the work"; "RUN_LOG.md only records the suite before the work started" | Found the pre-existing red format test; does not say the PR omits it, and misattributes the cause to the missing money.py rather than the recorded failure, but the defect is located with evidence. |
| red-for-the-wrong-reason | identified | "The PR shows `ImportError: cannot import name 'split_bill'`, a missing function, not a lost penny" | Exact. |
| test-and-fix-in-one-commit | partial | "HISTORY.md says the commit also changed src/money.py (41 lines) and bumped requirements.txt" | Notes the single commit holds other changes, but never names a41c2e0 nor says there is no test-only commit so the order cannot be shown. |
| paraphrased-input | identified | "9.00 by 3 (even) and 12.40 by 1. Neither loses a penny, so both would pass on the old code. Nothing tested 10.00" | Exact, and the report added 10.00/20.00 tests. |
| fix-bundled | identified | "Unrelated changes bundled in ... money.py (41 lines) and bumped requirements.txt" | Right file and size; babel not named (requirements.txt) and reverting-alone consequence only implied by "split the money.py and babel changes out". |
| sibling-missed | missed | (none; tips.py appears only for the 3.8 annotation error) | Does not say split_tip has the same round-and-multiply pattern or that 10.00 between 3 still loses a penny. |

Totals: 4 identified, 1 partial, 1 missed

False claims:
- none. The Python 3.8 `list[Decimal]` TypeError is real in the source (src/split.py line 5, src/tips.py line 5), though it is outside the planted defects. The control (split_bill correct) is correctly accepted.
