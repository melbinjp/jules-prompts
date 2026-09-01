---
description: To review a change an agent wrote for the security defects agents specifically introduce.
---

# Security Review of Agent-Written Code

**Role:** You are a coding agent. Explore the codebase, plan, execute, and verify. These instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names.

**Objective:**
Review a change written by an agent for security defects, and report each with the evidence that establishes it. This is not a general audit of the project. It targets the specific ways a change goes wrong when it was produced by something optimising for a green build.

**Context:**
An agent asked to fix a failure will find the shortest route to the failure stopping. That route is often to remove the thing that was objecting. The defect this produces is not a subtle logic flaw, it is a check that no longer checks, and it is invisible in review because the diff looks like work: a scanner was added, an error was handled, a dependency was installed.

*   **The change:** `<PR_URL_OR_DIFF_RANGE>`
*   **Key Files & Folders:**
    *   The diff, and CI configuration touched by it.
    *   Dependency manifests and lock files.
    *   Test fixtures, example configuration and documentation added by the change, which is where invented credentials land.

**Requirements & Constraints:**
*   **Report, do not repair**, unless a fix is one line and you say plainly that you made it. A security finding someone else has to re-derive from a patch is worth less than the finding.
*   **Every finding carries a file, a line and why it matters.** "Potential vulnerability" is not a finding.
*   **Rate by what an attacker gains**, not by how alarming the pattern looks. A hardcoded key in a test fixture for a local mock is not the same as one in a deployment manifest, and saying so is part of the job.
*   **State what you did not examine.** A review that silently skipped the vendored directory reads identically to one that cleared it.

**Guiding Principles:**
*   **A check that cannot fail is the defect, not the absence of a check.** A scanner added with `continue-on-error`, a step whose exit code is discarded with `|| true`, an audit whose output is only uploaded as an artifact: each looks like security work and gates nothing. Confirm every check introduced can actually turn the build red, by making it find something.
*   **Look for the verification that was switched off to make a request succeed.** `verify=False`, `rejectUnauthorized: false`, `--no-check-certificate`, `NODE_TLS_REJECT_UNAUTHORIZED=0`, a pinned certificate removed. These appear when something hit a TLS error and the error stopped.
*   **Credentials in anything the change created.** Agents invent plausible values for examples, fixtures and documentation. Treat every key-shaped string as real until you have established it is not, and check whether it reached the history rather than only the working tree.
*   **Ask where each new dependency came from.** A package that made an error go away may be a typosquat of the one intended, unmaintained, or pulled from a different registry. Check the name character by character against the import it satisfies, and check the lock file changed consistently with the manifest.
*   **Permissions only ever widen by accident.** A workflow moved to `permissions: write-all`, a token given more scope, a mode changed to 777, a bucket or security group opened. Compare against what the change actually needs.
*   **A swallowed exception around an authorisation path is an authorisation bypass.** Read every new `try`/`except`, `catch`, and `if err != nil` that continues, and ask what happens to the request when it fires.
*   **Injection returns wherever a string was built.** A query, a shell command, a path or an HTML fragment assembled by concatenation or formatting is the same defect regardless of how modern the surrounding code looks.

**Execution Flow:**
1.  **Explore & Plan:**
    *   Read the diff in full and list every file it touches, grouping them into code, configuration, CI, dependencies and fixtures.
    *   Identify which parts of the change are on a path that handles input, credentials or permissions.
    *   Write the plan. If the harness can pause for approval, wait; otherwise state the plan and proceed.

2.  **Execute & Verify:**
    *   Walk each principle above against the diff, recording a file and line for every hit.
    *   **Prove each new check can fail.** Introduce the thing it is supposed to catch, run it, and confirm a non-zero exit. Restore afterwards.
    *   For every new dependency, record the exact name, version and resolved source, and compare the name against the module actually imported.
    *   For every credential-shaped string, determine whether it is live, and whether it exists in the git history as well as the tree.
    *   Run whatever scanners the project already has, and report their output verbatim rather than summarised.

3.  **Test & Review:**
    *   Write the findings, ordered by what an attacker gains, each with file, line, evidence and the smallest fix.
    *   Request a code review through the harness if it has one; otherwise include the review in the deliverable.

4.  **Submit:**
    *   Post the review, or open a pull request if you were asked to, carrying the review as a document.

**Deliverables:**
*   A findings list ordered by impact: file, line, what an attacker gains, and the smallest change that closes it.
*   For every check the change introduced, the result of deliberately making it find something, so a check that cannot fail is caught rather than counted.
*   A table of new dependencies: name, version, resolved source, and the import it satisfies.
*   Every credential-shaped string found, and whether it is live and whether it is in the history.
*   An explicit list of what you did not examine and why.
