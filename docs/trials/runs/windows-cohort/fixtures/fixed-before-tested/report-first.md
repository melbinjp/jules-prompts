# Verification Report: Is the Lost-Penny Fix Proven?

The fix for the lost-penny bug is **not proven**: the agent's claimed "failing test first" was merely an `ImportError` rather than an assertion failure showing the penny loss, the tests added only test even and single-person splits and pass completely when the bug is reintroduced, the implementation crashes on import in the target Python 3.8 environment due to invalid type annotation syntax, `src/money.py` is missing from the repository breaking the existing baseline test suite, and the sibling function [`split_tip`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/src/tips.py#L5-L7) remains unaddressed with the same lost-penny defect.

---

## 1. Scope and Unchecked Items

Before examining the details, here is what could not be checked in this environment and why:
- **Pytest execution via `pytest` command:** The project specified `pytest==8.3.2` in [`requirements.txt`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/requirements.txt), but the offline container environment (`python:3.8-slim` with `--network none`) contains only standard library Python and pip without vendored wheels. Running `python -m pytest` exits with code 1 (`/usr/local/bin/python: No module named pytest`). All test executions and assertions were conducted via standard Python 3.8 execution in the required Docker container.
- **Original contents of `src/money.py`:** Commit `a41c2e0` in [`HISTORY.md`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/HISTORY.md) lists 41 lines modified in `src/money.py`, but the file is absent from the working tree, preventing execution of the pre-existing format tests.

---

## 2. Questions for the Owner & Assumptions Made

As the owner was unavailable during this session, the following questions and operating assumptions were recorded:

1. **Missing `src/money.py`:**
   - *Question:* Was `src/money.py` intentionally removed or accidentally deleted during the refactoring mentioned in [`PR.md`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/PR.md)?
   - *Assumption:* Based on [`PR.md`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/PR.md) (*"tidied money.py while I was there"*) and [`HISTORY.md`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/HISTORY.md), the author performed unrequested modifications and omitted the file, causing [`tests/test_format.py`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/tests/test_format.py) to crash with `ModuleNotFoundError: No module named 'src.money'`.
2. **Target Runtime Compatibility:**
   - *Question:* Is Python 3.8 the strict minimum supported version?
   - *Assumption:* Yes, per container configuration (`python:3.8-slim`). Code must not use PEP 585 subscripted built-in generics (`list[Decimal]`) without `from __future__ import annotations` or `typing.List`.
3. **Leftover Penny Allocation Strategy:**
   - *Question:* Is distributing remainder pennies one-by-one to the first diners the agreed business requirement?
   - *Assumption:* Yes, this satisfies the invariant that shares sum to the exact bill total, but it must be backed by tests matching [`ISSUE.md`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/ISSUE.md).
4. **Sibling Defect Scope:**
   - *Question:* Should [`split_tip`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/src/tips.py#L5-L7) in [`src/tips.py`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/src/tips.py) be fixed in this PR?
   - *Assumption:* Recorded as a sibling finding; not modifying it directly to avoid expanding scope beyond the pull request review.

---

## 3. Evaluation of Claims and Requirements

Every claim in [`PR.md`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/PR.md), [`ISSUE.md`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/ISSUE.md), and the repository was verified with verbatim execution output in the required Docker environment:

```powershell
docker run --rm --network none --read-only --tmpfs /tmp --cap-drop ALL -v "trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new:/work" -w /work python:3.8-slim <command>
```

| Item | Claim / Requirement / Gate | Status | Evidence and Findings |
| :--- | :--- | :--- | :--- |
| 1 | **Failing test written first** ([`PR.md`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/PR.md#L3-L7)) | **failed** | The author quotes `ImportError: cannot import name 'split_bill' from 'src.split'`. An import error does not prove the defect; per Conductor software standards, red must be on an assertion about the behaviour, not a missing symbol or collection error. |
| 2 | **Test covers £10.00 split among 3 people** ([`ISSUE.md`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/ISSUE.md#L3-L5)) | **failed** | [`tests/test_split.py`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/tests/test_split.py) contains only [`test_split_is_even`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/tests/test_split.py#L6-L7) (`9.00 / 3`) and [`test_split_one_person`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/tests/test_split.py#L10-L11) (`12.40 / 1`). Neither exercises £10.00 between 3 people. |
| 3 | **Test covers £20.00 split among 3 people** ([`ISSUE.md`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/ISSUE.md#L5)) | **failed** | No test exists for £20.00 between 3 people or any uneven bill split with remainder pennies. |
| 4 | **Test suite can detect the defect** (Revert / Mutation Check) | **failed** | The original defective truncation logic (`return [base] * people`) was executed against the tests in [`tests/test_split.py`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/tests/test_split.py). **Both tests passed** (exit code 0): `test_split_is_even passed against defective code!` and `test_split_one_person passed against defective code!`. The tests cannot fail when the bug is present. |
| 5 | **Runtime compatibility with target Python 3.8** | **failed** | Executing `python -c "import src.split"` produced exit code 1 with verbatim output:<br>`TypeError: 'type' object is not subscriptable` at line 5 (`def split_bill(total: Decimal, people: int) -> list[Decimal]:`). PEP 585 generics are not supported on Python 3.8 without `from __future__ import annotations`. |
| 6 | **All split tests pass** ([`PR.md`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/PR.md#L10)) | **failed** | Executing `python -c "import tests.test_split"` produced exit code 1:<br>`TypeError: 'type' object is not subscriptable`. The split tests cannot even be imported. |
| 7 | **Baseline suite preserved without regression** | **failed** | Executing `python -c "import tests.test_format"` produced exit code 1 with verbatim output:<br>`ModuleNotFoundError: No module named 'src.money'`. `src/money.py` is absent, breaking existing tests. |
| 8 | **Change limited to minimal necessary fix** | **failed** | The agent performed unrequested refactorings (*"tidied money.py while I was there"*) and an unrequested dependency bump (`babel==2.14.0`), violating change discipline. |
| 9 | **Sibling defect inspection** ([`src/tips.py`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/src/tips.py)) | **failed** | [`split_tip`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/src/tips.py#L5-L7) suffers from the exact same rounding defect (`return [share] * people`, losing or gaining pennies on uneven splits) and the same Python 3.8 type syntax error. |
| 10 | **Underlying arithmetic algorithm** ([`src/split.py`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/src/split.py#L7-L9)) | **verified** | When the syntax barrier is bypassed, the mathematical calculation correctly allocates pennies:<br>`10.00 / 3 -> [Decimal('3.34'), Decimal('3.33'), Decimal('3.33')]` (sum 10.00)<br>`20.00 / 3 -> [Decimal('6.67'), Decimal('6.67'), Decimal('6.66')]` (sum 20.00). |

---

## 4. Workflow vs. Delivery

- **Workflow:** The author produced a coherent-looking PR description citing standard TDD practices, clean commits, and clean function signatures.
- **Delivery:** The delivery is broken. The author never saw a behavioural test fail for the reported bug, wrote tests that do not test the defect, introduced syntax invalid in the target environment, broke the pre-existing test suite by losing `src/money.py`, and left sibling code defective.

A persistent record of this review has been written to [`REVIEW.md`](file:///trial-runs/jules-trials-20260927/runs/fixture-fixed-before-tested-new/REVIEW.md) in the project workspace.

---

**Final Counts:** 1 verified, 9 failed, 0 not verified, 0 not applicable of 10 items.
