**The fix is not proven.** The arithmetic in `split_bill` is right, but the PR's evidence doesn't show it, and the module doesn't import on Python 3.8.

Checked: arithmetic ran in Docker with the `list[...]` annotation worked around: 10.00 by 3 gives 3.34+3.33+3.33=10.00, 20.00 by 3 gives 6.67+6.67+6.66=20.00, exact sums also for 100.00 by 7, 10.005 by 3, 0.01 by 3. Importing `src.split` on the 3.8 image raises `TypeError: 'type' object is not subscriptable` at `-> list[Decimal]`; same in src/tips.py. pytest is not installed and there is no network, so the suite was never run.

Why the evidence doesn't prove it:
1. The "failing test" failed for the wrong reason: the PR shows `ImportError: cannot import name 'split_bill'`, a missing function, not a lost penny.
2. The tests don't cover the bug: the two tests in tests/test_split.py are 9.00 by 3 (even) and 12.40 by 1. Neither loses a penny, so both would pass on the old code. Nothing tested 10.00 or 20.00 by 3.
3. "All split tests pass" is unsupported: no run output quoted; RUN_LOG.md only records the suite before the work started.
4. Unrelated changes bundled in: HISTORY.md says the commit also changed src/money.py (41 lines) and bumped requirements.txt; the PR gives no reason or evidence.
5. src/money.py is missing from this checkout, so tests/test_format.py cannot import format_gbp. That test was already failing before the work, and its status now is unknown.

What I changed: two regression tests in tests/test_split.py (10.00 and 20.00 by 3, shares must sum to the total). Not seen failing against the old code; not run under pytest.

Next steps: use `List[Decimal]` or `from __future__ import annotations` if 3.8 must work; put the old split_bill back and run the two new tests to see them fail with a 9.99 sum, then restore the fix; split the money.py and babel changes out.

Tally: 1 verified, 5 failed or not supported, 2 not verified, of 8 items.
