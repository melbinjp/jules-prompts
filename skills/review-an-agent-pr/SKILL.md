---
name: review-an-agent-pr
description: 'To review a pull request an agent wrote, against the failure modes agents
  actually have. Category: Maintenance.'
license: MIT
metadata:
  prompt_slug: task_review_an_agent_pr
  source: _prompts/task_review_an_agent_pr.md
  title: Review an Agent-Written Pull Request
  category: Maintenance
---

# Review an Agent-Written Pull Request

**Role:** You are a coding agent. Explore the codebase, plan, execute, and verify. These instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names.

**Objective:**
Review a pull request that was written by an agent, and decide whether it does what it claims. Produce a verdict with evidence for each claim the pull request makes about itself. Do not fix anything in this task unless the fix is trivial and you say so explicitly.

**Context:**
Agent-written pull requests fail differently from human ones, and a review habit built on human mistakes will miss them. A human who does not understand a requirement usually writes something visibly wrong or asks. An agent writes something plausible: correct style, sensible names, a confident description, and tests that pass because they assert what the code does rather than what it should do. The reported danger is not that the code is bad, it is that it reads as finished.

*   **The pull request:** `<PR_URL_OR_NUMBER>`
*   **Key Files & Folders:**
    *   The diff itself, and the issue or task the pull request claims to close.
    *   The tests it adds or changes, which is where the specific failures below concentrate.
    *   CI configuration, so you can tell which checks actually gate the merge.

**Requirements & Constraints:**
*   **Every claim in the description gets checked or marked unchecked.** A pull request body is a set of assertions. Treat each as a claim to verify, not as a summary to read.
*   **Run it. Reading is not reviewing.** A diff that reads correctly and fails on execution is the exact case this prompt exists for.
*   **Do not widen the scope.** Problems found that the pull request did not introduce are recorded separately, not fixed here.
*   **Say what you could not check**, and why. An unverified claim reported as unverified is useful; an unverified claim reported as fine is the failure being reviewed.

**Guiding Principles:**
*   **Check that a new test can fail.** Break the code it covers, on purpose, and confirm the test goes red. A test that passes against both the fixed and the broken code is not evidence of anything, and this is the single commonest defect in agent-written changes.
*   **Ask what the test asserts, not whether it passes.** Tests written from an implementation assert what the code happens to do. Compare each assertion against the ISSUE, not against the diff.
*   **Look for the requirement that was quietly dropped.** Agents satisfy the part of a request they understood. Read the original issue line by line and tick off each requirement against the diff. What is missing will not announce itself.
*   **Distrust deleted or weakened assertions.** A change that makes a failing test pass by editing the test, loosening a matcher, adding a skip, or widening a tolerance is the fix being faked. Every such edit needs a stated reason.
*   **Treat a suppressed error as a finding.** New `try`/`except` around the changed path, a swallowed non-zero exit, a `continue-on-error`, or a log line where a raise used to be, are all ways for a change to look successful while doing nothing.
*   **Confirm the CI check that is supposed to catch this actually runs on this pull request.** A gate that is skipped by path filter or made advisory is not a gate.

**Execution Flow:**
1.  **Explore & Plan:**
    *   Read the linked issue and list its requirements as discrete, checkable items.
    *   Read the diff and note which files it touches and which it does not.
    *   Write the plan. If the harness can pause for approval, wait; otherwise state the plan and proceed.

2.  **Execute & Verify:**
    *   Establish a baseline: check out the base commit and run the suite, so you know what was already failing.
    *   Check out the pull request and run the suite again. Compare, and account for every difference.
    *   For each test the pull request adds: break the code under it and confirm the test fails. Restore.
    *   Walk your requirement list and mark each one met, partly met, or not addressed, with a file and line for each.
    *   Exercise the change by hand if it has an interface: run the command, call the endpoint, load the page.

3.  **Test & Review:**
    *   Write the verdict: what the pull request claims, what you verified, what you could not, and what you found.
    *   Request a code review through the harness if it has one; otherwise include the review in the deliverable.

4.  **Submit:**
    *   Post the review. If you were asked to open a pull request with the review as a document, do that.

**Deliverables:**
*   A per-requirement table: requirement, met or not, and the file and line that settles it.
*   For every added test, the result of deliberately breaking the code it covers.
*   A list of weakened or deleted assertions, skips, widened tolerances and suppressed errors, each with the reason given for it or a note that none was given.
*   An explicit list of what you could not verify and why.
*   A single sentence at the top saying whether the change does what it says.
