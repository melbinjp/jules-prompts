---
layout: default
title: QA the Tests an Agent Wrote
description: To find the tests that pass because they were written from the implementation rather than from the requirement, and cannot fail.
category: Maintenance
type: Task
---
**Role:** You are a coding agent. Explore the codebase, plan, execute, and verify. These instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names.

**Objective:**
Audit a test suite an agent wrote, and find the tests that cannot fail. For every test added or changed by agent work, prove it fails when the behaviour it names is broken. Fix or delete the ones that do not, and report the count.

**Context:**
An agent asked to add tests will add tests, and they will pass. That is the whole problem. A test written while looking at the implementation asserts what the code *does*, and a test that asserts what the code does can never catch the code doing the wrong thing. It goes green on the first run and stays green through every future defect in the thing it claims to cover.

This failure has no symptom. Coverage goes up, the suite is fast, the pull request reads as careful work, and the number of real regressions caught is zero. It is strictly worse than having no test, because the absent test is visible in the coverage report and the useless one is counted as protection.

The tells are consistent and mechanical: a test that mocks the unit under test; a test whose assertion is `assertTrue(result)` or `expect(x).toBeDefined()`; a test that reconstructs the implementation's own arithmetic in the expected value; a test whose only assertion is that no exception was raised; a test whose fixtures were captured by running the code it tests.

*   **Key Files & Folders:**
    *   Every test file touched by agent-authored commits or pull requests. `git log --diff-filter=AM` over the test directory is the starting list.
    *   Fixtures, snapshots and recorded responses added alongside them, especially any snapshot committed on the same commit as the code it snapshots.
    *   Mock and patch setup, and anything that substitutes the module being tested rather than its dependencies.

**Requirements & Constraints:**
*   **Prove each test can fail. Do not read it and decide.** Break the behaviour on purpose, run the test, and record whether it went red. A test nobody has seen fail is a claim, not a check.
*   **Revert every deliberate break.** Mutate, observe, restore, and verify the suite is green again before moving on. Confirm with `git diff` that the tree is clean of your mutations at the end.
*   **A test that cannot fail is either fixed or deleted, never left.** If you cannot make it meaningful, delete it and say so. Leaving it is choosing to keep a false signal.
*   **Do not raise coverage.** This task lowers it when a useless test is removed, and that is the correct direction. Report the change; do not compensate for it.
*   **Do not change the behaviour under test.** If a test fails once made meaningful, that is a real finding. Report it as a defect and leave it failing rather than adjusting the assertion until it passes.

**Guiding Principles:**
*   **Mutate the code, not the test.** Invert a condition, return a constant, drop a field, skip a call. If the suite stays green, you have found one. This is the only method here that answers the actual question, and it takes seconds per test.
*   **A test that mocks what it tests is measuring the mock.** The most common shape: the unit is patched, the patched return value is asserted, and the test passes on an empty implementation. Check by deleting the function body and running the test.
*   **Suspect any expected value that could have been produced by running the code.** A hand-derived expected value comes from the requirement; a captured one comes from whatever the code happened to do that day, including its bugs. Where the requirement states a number, that number belongs in the test.
*   **An assertion on shape is not an assertion on value.** `is not None`, `toBeDefined`, `status == 200` and `len(result) > 0` survive almost every real defect. They are worth keeping only alongside an assertion that says what the value should be.
*   **Check what the suite COLLECTS. The passed count is the wrong number.** A file that fails to import, a test whose name does not match the runner's pattern, and a fixture that errors during setup all produce a green run with a smaller number in it. Compare the collected count against the number of test functions you can count by hand.
*   **A skipped test is an untested test wearing a green tick.** Read every skip, mark and conditional exclusion added by the agent, and report each with the reason given and whether the reason is still true.

**Execution Flow:**
1.  **Explore & Plan:**
    *   Build the list of agent-authored tests from version control history rather than from names or comments.
    *   Run the suite from cold and record the exact collected count, the passed count, and every skip.
    *   Write the plan. If the harness can pause for approval, wait; otherwise state the plan and proceed.

2.  **Execute & Verify:**
    *   For each test, mutate the behaviour it names, run only that test, and record red or green. Restore the mutation immediately.
    *   Group the survivors by which tell they exhibit; the grouping is usually a small number of repeated patterns rather than unrelated mistakes.
    *   Rewrite the salvageable ones against the requirement, not the implementation. Delete the rest.
    *   Re-run each rewritten test under the same mutation and confirm it now goes red.
    *   **Verify you left nothing broken:** run the full suite, confirm it is green, and confirm `git diff` shows no leftover mutation.

3.  **Test & Review:**
    *   Report the numbers plainly: tests examined, tests that could not fail, rewritten, deleted, and the coverage change including its sign.
    *   Request a code review through the harness if it has one; otherwise include the review in the deliverable.

4.  **Submit:**
    *   Address any feedback, then open a pull request (or the harness equivalent) with a title, a summary of what was verified, and a link to the original task.

**Deliverables:**
*   A table of every agent-authored test with the mutation used against it and whether it caught it.
*   The list of tests deleted, each with the reason it could not be made meaningful.
*   The before and after collected-test counts and the coverage change, with the direction stated rather than explained away.
*   Any defect found because a test became meaningful and then failed, reported and left failing.
*   A note of every skip added by agent work, with its stated reason and whether that reason still holds.
