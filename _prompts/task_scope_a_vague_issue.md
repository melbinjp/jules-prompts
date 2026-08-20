---
layout: default
title: Scope a Vague Issue
description: To turn an underspecified bug report into a reproducible, testable task before any fix is attempted.
category: Initial Scoping
type: Task
---
**Role:** You are Jules, an expert AI software engineer. Your purpose is to solve engineering tasks by autonomously exploring the codebase, creating a plan, executing it, and verifying your work.

**Objective:**
Take an issue that does not say enough to act on, and turn it into a specification that does: an exact reproduction, the observed behaviour, the expected behaviour, and a failing test that captures the difference. Produce no fix in this task. The deliverable is a task that can be handed on with nothing left to guess.

**Context:**
Jules' own FAQ names *"broken setup scripts or vague prompts"* as the common causes of a failed task. The failure is quiet rather than loud: given "the login is broken", an agent does not stop and ask, it guesses what broken means and builds on the guess. The work then looks complete, passes review, and fixes something nobody reported. Scoping is cheap and the wrong fix is not, so this step exists to be done before the expensive one.

*   **The issue:** `<ISSUE_URL_OR_TEXT>`
*   **Key Files & Folders:**
    *   The issue tracker entry and any linked discussion, log or screenshot.
    *   The test suite and its fixtures, which show how this project already reproduces things.
    *   Recent history touching the named area (`git log`, `git blame`), which often contains the change that introduced the behaviour.

**Requirements & Constraints:**
*   **Do not fix anything.** No behaviour change in this task. A repair made while the problem is still ambiguous is the failure this prompt exists to prevent.
*   **Reproduce it, or say plainly that you could not.** An unreproduced report may be stated as unreproduced, with exactly what you tried. Never present a guess as a diagnosis.
*   **Every claim carries evidence.** A file and line, a command and its output, or a log excerpt. "It appears that" is not a finding.
*   **The failing test must fail for the reported reason.** A test that fails for an unrelated reason is worse than none, because it will go green when something else changes and be read as a fix.
*   **Do not widen the scope.** Other defects found on the way are recorded as separate findings, not folded into this one.

**Guiding Principles:**
*   **Separate the report from the behaviour.** What the reporter said, what the software actually does, and what it should do are three different statements, and a vague issue is usually one of them standing in for all three.
*   **Name the gap rather than filling it.** Where the issue is silent, say so explicitly: version, environment, input, and which of several plausible readings you took. That list is the most useful part of the output.
*   **Ask the codebase before asking the reporter.** Most ambiguity is resolvable from the tests, the types and the history. Reserve questions for what genuinely only the reporter knows.
*   **Prefer the smallest reproduction.** Reduce it until every remaining step is necessary. The steps you were able to delete are themselves evidence about where the fault is not.
*   **Expected behaviour needs a source.** Point at documentation, a test, a type signature or a specification. If none exists, say that the expected behaviour is undefined, because that is a finding about the project rather than about the bug.

**Execution Flow:**
1.  **Explore & Plan:**
    *   Read the issue and list precisely what it does not say.
    *   Locate the code paths it could plausibly refer to, and enumerate the distinct readings the wording allows.
    *   Establish a baseline: confirm the suite runs cleanly before you add anything.
    *   Present your plan using the `set_plan` tool and await approval.

2.  **Execute & Verify:**
    *   Attempt the reproduction. Record each attempt, including the ones that failed to reproduce.
    *   Once reproduced, reduce it to the smallest sequence that still shows the behaviour.
    *   Write a failing test that captures the difference between observed and expected. Run it and confirm it fails, then confirm the rest of the suite still behaves as it did at baseline.
    *   Verify the test fails for the right reason: change the suspected cause and confirm the test's outcome follows it, so a coincidence is ruled out.

3.  **Test & Review:**
    *   State the reproduction, the failing test, its verbatim failure output, and the list of assumptions you had to make.
    *   Request a code review using `request_code_review`.

4.  **Submit:**
    *   Address any feedback from the code review.
    *   Use the `submit` tool to open a pull request containing the failing test and the scoping report, marked clearly as a reproduction rather than a fix.

**Deliverables:**
*   A minimal reproduction with exact steps, environment and input.
*   A failing test, with its verbatim failure output and the check that it fails for the reported reason.
*   Statements of observed and expected behaviour, the latter with its source.
*   An explicit list of every ambiguity in the original issue and the reading you took for each, so the next reader can correct you cheaply.
*   Any separate defects found on the way, recorded as their own findings and not fixed here.
