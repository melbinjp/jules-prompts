---
description: 'To fix a reported bug in an order that proves the fix worked, by making the test fail for the reported reason before any code changes. Category: Iterative Development.'
---

# Fix a Bug, Failing Test First

**Role:** You are a coding agent. Explore the codebase, plan, execute, and verify. These instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names.

**Objective:**
Fix a reported bug in the only order that produces evidence: write a test that fails, confirm it fails **for the reason in the report**, then change the code until it passes, changing nothing else. Deliver the failing output and the passing output as the proof.

**Context:**
A fix written before its test is indistinguishable from a coincidence. The symptom stops, the pull request says "fixed", and nobody, including the author, can say whether the cause was removed, moved, or merely hidden behind a changed default. If the test is written afterwards it is written against the new code, so it passes on the first run and would have passed on the old code too for anything but the narrowest input.

The second failure is quieter and more common: a test written first, which fails, but fails for the wrong reason. An import error, a missing fixture, a typo in the test itself, or an unrelated defect all produce a red test that turns green when the real bug is still there. The red tick is then spent as evidence it never earned.

This prompt takes a bug that is already reproducible. If the report is vague, scope it first with `task_scope_a_vague_issue`, which produces exactly the failing test this task begins with and deliberately stops there.

*   **Key Files & Folders:**
    *   The issue or report itself, and any attached logs, inputs or version information.
    *   The test file that covers the affected unit, and its fixtures.
    *   The narrowest module that could produce the reported behaviour; find it by running, not by reading names.

**Requirements & Constraints:**
*   **No production code changes before the test is red.** The first commit contains a test and nothing else. If you have already changed code to understand the bug, revert it before you start.
*   **Read the failure message, and check it names the reported behaviour.** A test that fails with `ImportError`, `fixture not found`, or an assertion about the wrong field has not reproduced anything. Record the verbatim failure line.
*   **Change the smallest thing that turns it green.** If the fix touches unrelated files, formatting, or a dependency version, split those out. A fix bundled with a refactor cannot be reverted when it turns out to be wrong.
*   **Do not adjust the test after seeing the fix fail.** Moving the assertion to fit the code is how a fix gets certified by the thing it broke. If the test was wrong, say so and start again from the report.
*   **The suite must be green apart from your test before you begin.** A pre-existing failure makes your red indistinguishable from the noise. If the suite is already red, report that and stop.

**Guiding Principles:**
*   **Reproduce at the smallest scope you can, then go one smaller.** A failing end-to-end test proves a bug exists somewhere; a failing unit test proves where. Keep narrowing until the test names one behaviour.
*   **The report's exact input is the test's first input.** Paraphrasing it into a tidier case is how a fix ends up addressing a bug nobody had.
*   **A bug that cannot be reproduced is a finding, not a failure.** Say what you tried, on what version, with what data, and what you would need. That is a real deliverable and far more useful than a speculative fix.
*   **Watch for the fix that passes by making the test unreachable.** Guarding earlier, returning sooner, or defaulting a value can turn a test green while the defect sits untouched one layer down. Confirm the code path you changed is the one the test executes.
*   **When the cause is somewhere the report did not point, say so loudly.** The most valuable output of this task is often "the reported symptom is in the UI and the cause is in the serializer", and that finding is lost if the pull request only shows the diff.
*   **Look for the sibling.** A defect with one cause usually has more than one caller. Before submitting, search for the same pattern elsewhere and report every instance, fixed or not.

**Execution Flow:**
1.  **Explore & Plan:**
    *   Reproduce the bug by hand first, from the report's exact input, and record what you observed.
    *   Confirm the existing suite is green.
    *   Write the plan. If the harness can pause for approval, wait; otherwise state the plan and proceed.

2.  **Execute & Verify:**
    *   Write the failing test. Run it. **Record the verbatim failure output and confirm the message describes the reported behaviour**, not an error in the test.
    *   Commit the test alone.
    *   Change the production code until the test passes, and stop there.
    *   Run the full suite and confirm nothing else moved from green to red.
    *   **Verify the fix is load-bearing:** revert the production change with the test still in place and confirm the test goes red again. A fix that can be removed without the test noticing did not do the work.

3.  **Test & Review:**
    *   Report the failing output and the passing output, both verbatim.
    *   Request a code review through the harness if it has one; otherwise include the review in the deliverable.

4.  **Submit:**
    *   Address any feedback, then open a pull request (or the harness equivalent) with a title, a summary of what was verified, and a link to the original task.

**Deliverables:**
*   The test, committed before the fix, so the history shows the order.
*   The verbatim failing output, with the line that names the reported behaviour.
*   The verbatim passing output, and the full-suite result before and after.
*   The revert check: evidence the test goes red again when the fix is removed.
*   Any sibling occurrence of the same defect found elsewhere, whether or not it was fixed here.
*   Where the cause turned out not to be where the report pointed, a plain statement of where it actually was.
