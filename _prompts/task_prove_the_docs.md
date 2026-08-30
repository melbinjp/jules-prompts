---
layout: default
title: Prove the Documentation Against the Code
description: To find the claims in the docs that were true when written and are not true now, by executing each one rather than reading it.
category: Maintenance
type: Task
---
**Role:** You are a coding agent. Explore the codebase, plan, execute, and verify. These instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names.

**Objective:**
Take the project's documentation, extract every claim in it that could be checked, and check each one against the code by running it. Report each claim as verified, false, or unverifiable, with the evidence. Fix the false ones and make the unverifiable ones checkable or remove them.

**Context:**
Documentation does not fail loudly. Every sentence in a README was true on the day it was written, and nothing since has told anybody which ones stopped being true. There is no red tick for a stale document, no test that goes from green to red when a flag is renamed, and no coverage report with a gap in it. The rot is invisible by construction, which is why it is always worse than the team expects.

The specific damage is at the front door. A quickstart is the first thing a new user runs and the least often re-run by anyone who already has the project working, so it is simultaneously the most important instructions in the repository and the least tested. It usually fails on a clean machine for reasons nobody can see on their own, because their environment has been carrying the missing step for a year.

**There is a second failure here and it is the reason to be careful about who writes documentation.** Asked to "write the docs", an agent will read the function names, the comments and the type hints, and produce fluent prose describing what the code was *meant* to do. That is not documentation, it is a restatement of the same intent that was already wrong, now in a second place and sounding authoritative. The output is longer, reads better, and is exactly as false. Prose confidence is not evidence, and the only defence is to execute the claim.

The tells are mechanical: a documented flag that no longer appears in the argument parser; a default value stated in prose and set differently in code; a docstring promising an exception the function stopped raising; example output pasted from an older version; a supported-versions table nobody updated when CI dropped one; a link to a file that has moved. Every one of these is checkable in seconds and none of them is visible by reading the document alone.

*   **Key Files & Folders:**
    *   `README.md` and anything it links to, the quickstart or getting-started guide, and the installation instructions.
    *   Docstrings and module headers, especially on public entry points and anything the README names.
    *   Any `docs/` tree, tutorials, and example code, including examples embedded in the README.
    *   Configuration reference: flags, environment variables, defaults, and the code that actually reads them.

**Requirements & Constraints:**
*   **Every claim gets a verdict and a piece of evidence.** Verified means you ran it or pointed at the line that proves it. False means you ran it and it did something else. Unverifiable means it cannot be checked as written, which is a finding about the sentence rather than about the code.
*   **Run the quickstart from cold.** A fresh container or a clean virtual environment, following the document literally, typing nothing that is not written down. The missing step is invisible from a working machine, and that is the whole point of doing it this way.
*   **Do not rewrite documentation you have not checked.** Improving the prose of a false claim makes it more convincing and no more true, and it hides the change in a large diff. Fix what is false; leave the rest alone.
*   **Do not delete a claim because it is inconvenient to verify.** Mark it unverifiable, say why, and either make it checkable or propose removing it in the report. Quietly dropping the hard ones turns a documentation audit into a documentation trim.
*   **A generated example must be produced by running the code**, not written to look like the output. If you cannot run it, the example does not go in.
*   **Report the count, including the denominator.** Claims examined, verified, false, unverifiable. A report that names three fixed claims without saying how many were looked at cannot be told apart from one that stopped after three.

**Guiding Principles:**
*   **Execute, do not read.** The entire method is that a claim which can be run is worth more than a claim that reads well. Where a sentence resists this, that resistance is the finding.
*   **Suspect every number and every name.** Version numbers, ports, paths, flag names, defaults, timings, supported platforms and counts are the claims that rot fastest, because they are true of one moment and are written as though permanent.
*   **Intent verbs mark the sentences to check first.** "Should", "will", "is designed to", "automatically" and "simply" almost always describe what somebody meant rather than what happens. "Simply" in particular is usually load-bearing for a step that is not simple.
*   **Check the links, because it costs nothing.** Every relative path, every anchor, every external URL. A dead link in a README is the cheapest possible signal that nobody has read the file recently, and it is one loop to find.
*   **A code block is a promise.** Anything a reader could paste is a claim that pasting it works. Run each one in order, from the state the document says the reader is in, not from your working directory with the project already set up.
*   **When the code and the document disagree, the document is not automatically wrong.** Sometimes the document records the intended behaviour and the code has drifted, and then you have found a bug rather than a typo. Report which one you think it is and why, and do not silently change the documentation to match a defect.

**Execution Flow:**
1.  **Explore & Plan:**
    *   Build the claim list first: read every document and extract each checkable statement as its own line, with the file and line it came from.
    *   Group them by how they will be checked: run this command, read this line of code, follow this link.
    *   Write the plan. If the harness can pause for approval, wait; otherwise state the plan and proceed.

2.  **Execute & Verify:**
    *   Set up a clean environment and run the installation and quickstart exactly as written, recording every deviation you had to make.
    *   Work through the claim list, recording the verdict and the evidence for each one.
    *   Fix the false claims against what the code actually does. Where the code looks wrong rather than the document, leave the document and report the defect.
    *   Regenerate any example output by running it.
    *   **Verify you did not break anything:** run the full test suite, and run the quickstart once more from cold against your corrected version to confirm it now works end to end.

3.  **Test & Review:**
    *   Report the claim table in full, with the denominator.
    *   Request a code review through the harness if it has one; otherwise include the review in the deliverable.

4.  **Submit:**
    *   Address any feedback, then open a pull request (or the harness equivalent) with a title, a summary of what was verified, and a link to the original task.

**Deliverables:**
*   A table of every claim examined, with its source location, verdict, and the command or line that settles it.
*   The counts: examined, verified, false, unverifiable.
*   A transcript of the quickstart run from a clean environment, including every step you had to take that the document does not mention.
*   Any place where the code appears to be wrong rather than the document, reported as a defect and left unfixed unless it was in scope.
*   The list of claims that could not be checked as written, each with the reason and a suggestion for making it checkable.
