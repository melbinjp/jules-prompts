---
layout: default
title: Repair the Environment Setup Script
description: To diagnose and repair the setup script so agent tasks stop failing before any code is written.
category: Initial Scoping
type: Task
---
**Role:** You are a coding agent. Explore the codebase, plan, execute, and verify. These instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names.

**Objective:**
Make this repository reliably usable by an asynchronous coding agent, by producing a setup script that installs everything the test suite needs and then exits. The measure of success is not that the script looks correct; it is that a clean environment can install, build and run the tests using only the script, with no step that a human would have to supply from memory.

**Context:**
This is a task about the environment, not about the product code. Asynchronous and sandboxed coding agents fail most often before any product code is touched: the setup script is broken, or the prompt is too vague to act on. Long-running processes such as a dev server or a file watcher do not belong in setup: the script must install, verify, and exit. Many harnesses snapshot a successful setup and reuse it, so a defect here is not paid for once. It is paid for by every future task.

*   **Key Files & Folders:**
    *   The existing setup or bootstrap script, if there is one (e.g. `AGENTS.md`, `setup.sh`, `scripts/setup`, `Makefile`, `.devcontainer/`).
    *   Package manifests and lock files (e.g. `package.json`, `requirements.txt`, `pyproject.toml`, `go.mod`, `Cargo.toml`).
    *   CI workflow files (e.g. `.github/workflows/`), which usually encode the only steps known to work from cold.
    *   Test configuration, and any `docker-compose.yml` or fixture that starts a service.

**Requirements & Constraints:**
*   **No long-running processes.** Nothing in the setup script may block: no dev server, no file watcher, no `tail -f`, no foreground daemon. If the test suite genuinely needs a background service, start it detached, poll until it is actually accepting connections, and fail loudly with its log if it never does. A fixed sleep is not a readiness check.
*   **Exit codes must be true.** A setup step that fails must fail the script. Do not end lines with `|| true` and do not swallow an installer's exit code to make the run look green. A setup script that cannot fail is the same defect as a test that cannot fail.
*   **No interactive prompts.** Every command must run unattended. Pass the non-interactive flag the tool provides rather than piping `yes` into it.
*   **No secrets, and no assumption of network credentials.** If a dependency needs a token, detect its absence and say so in one clear line; never embed one.
*   **Keep it lightweight.** Install what the tests need. Do not install a full toolchain to run one linter.

**Guiding Principles:**
*   **Reproduce the failure before repairing it.** Find out what actually breaks from cold rather than reading the script and forming an opinion. A script that reads correctly and fails on execution is the specific thing this task exists to catch.
*   **The CI workflow is your best evidence.** If CI passes, it contains a sequence that provably works on a clean machine. Start from that, not from the README, which is usually older.
*   **Prefer the lock file.** Install from the lock file where one exists, so the environment is the one the tests were written against.
*   **Separate install from verify.** Installing dependencies and running the suite are different phases with different failure meanings. Keep them distinct so a failure says which one it was.
*   **Say what is missing, do not paper over it.** If a test genuinely requires a service that cannot run here, report that plainly as a finding. Silently skipping those tests turns a red suite green and hides the very problem the next agent will hit.

**Execution Flow:**
1.  **Explore & Plan:**
    *   Determine the language, package manager, test runner and build tool from the manifests actually present.
    *   Read the CI workflow and extract the exact install, build and test commands it uses.
    *   Identify every external dependency the suite touches: databases, message queues, browsers, model endpoints, network fixtures.
    *   Establish the baseline: run the existing setup, if any, and record precisely where it fails, with the command and its output.
    *   Write the plan. If the harness can pause for approval, wait; otherwise state the plan and proceed.

2.  **Execute & Verify:**
    *   Write or repair the setup script so it installs dependencies and exits cleanly.
    *   Run it. Then run the test suite using only what the script installed.
    *   Repeat until the suite runs to completion. "Runs to completion" means the runner reported results; it does not require every test to pass, and you must not edit tests to make them pass in this task.
    *   Deliberately verify the two failure modes that are invisible when things go well: confirm the script exits non-zero when a required install is made to fail, and confirm no command in it blocks.

3.  **Test & Review:**
    *   State the evidence: the commands run, their exit codes, and the final test-runner summary line verbatim.
    *   Request a code review through the harness if it has one; otherwise include the review in the deliverable.

4.  **Submit:**
    *   Address any feedback from the code review.
    *   Open a pull request (or the harness equivalent) with a title, a summary of what was verified, and a link to the original task.

**Deliverables:**
*   A setup script that installs dependencies and exits, with no blocking process and no swallowed exit code.
*   A short `AGENTS.md` section, or an update to an existing one, giving the install command, the test command and any environment variable the suite needs.
*   A report containing: the baseline failure with its verbatim output, each change and the reason for it, the final test-runner summary line, and an explicit list of anything that still cannot run in this environment and why.
