---
description: 'To establish that a test added alongside a fix actually detects the defect, by putting the defect back and watching the test go red. Category: Maintenance.'
---

# Prove the Fix by Making It Fail

**Role:** You are a coding agent. Explore the codebase, plan, execute, and verify. These instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names.

**Objective:**
Take a change that claims to fix something and ships a test for it. Put the original defect back, one at a time, and confirm the test goes red for the stated reason. Report any test that stayed green, because that test is not evidence of anything.

**Context:**
A fix arrives as two things: a change to the code, and a test said to cover it. The suite passes, so the pair looks proven. It is not. A passing suite tells you the test agrees with the code as written. It does not tell you the test would have noticed the code being wrong, and those are different claims.

A test that cannot fail is the same defect as a pipeline that is green without checking anything, moved down a level. It costs the same thing: everybody now believes the case is covered, so nobody looks again.

The ways a test passes without testing are ordinary:

*   It asserts on a value the code under test never influences, so the assertion holds whatever the code does.
*   It mocks the unit it is meant to be exercising, and ends up asserting that the mock was configured.
*   It reconstructs the expected value using the same expression the implementation uses, so both are wrong together.
*   It calls the code inside a `try` with a bare `except`, or asserts `not None` on something that is never None.
*   It exercises a path the fix did not change, because the fixture does not reach the branch in question.
*   It fails for the wrong reason: an import error, a missing file, a typo in a fixture name. Red is not the same as red for the stated reason.

**Method:**

1.  **Find the pairs.** For the change under review, list every defect it claims to fix and the test said to cover each one. A claimed fix with no test is a finding on its own; report it and move on rather than writing one, unless asked.

2.  **Establish the baseline.** Run the suite unmodified and record that it passes. If it is already failing, stop and report that first: nothing below means anything on top of a red suite.

3.  **Reintroduce one defect.** Change the source, not the test, to reinstate the original behaviour as precisely as you can. Prefer the smallest edit that restores the defect: an inverted condition, a removed guard, a restored off-by-one. Do not delete the function, which fails for the wrong reason.

4.  **Run only the test that should catch it.** Record whether it fails, and read the failure. It must fail on the assertion about the behaviour, not on a collection error, an import error, or a fixture that no longer loads. A test that goes red because the file will not import has told you nothing.

5.  **Restore the source exactly.** Use version control, not memory. Confirm the suite is green again before the next one, or every later result is measured against a tree you no longer understand.

6.  **Repeat for each defect,** one at a time. Two at once cannot tell you which test caught what.

7.  **Report.** For each pair: the defect, the edit that reinstated it, whether the test went red, and the first line of the failure. Then state plainly which tests are evidence and which are decoration.

**Constraints:**

*   Change the source to reinstate a defect. Never weaken the test to make it fail, which proves the opposite of what is being asked.
*   One defect at a time.
*   Every edit is reverted before the next. The tree at the end must equal the tree at the start; show that it does.
*   If a mutation cannot be made without rewriting the fix entirely, say so and describe what you would have changed. An honest inability is a result.
*   Do not report a test as proven if it failed for a reason other than the behaviour under test. Say which reason it failed for.

**Definition of Done:**
Every claimed fix has been paired with its test, each defect has been reinstated and reverted, and the report says for each one whether the test detected it and on what line it failed. The working tree is identical to how it started. Any test that stayed green is named as not yet evidence, without being quietly rewritten to pass this exercise.
