---
layout: default
title: Prompts Guide
permalink: /prompts-guide/
---
# Jules Prompt Library Guide

This repository contains a curated library of pre-made, machine-readable task prompts that help an AI software engineer like Jules turn user intent into well-scoped, verifiable work. This guide explains the purpose of each prompt and provides a recommended workflow for using them together.

## Prompt Library

### [`template_master_prompt.md`]({% link _prompts/template_master_prompt.md %})
This is the master template used to create and standardize all other prompts. It is not intended for direct use but serves as a "golden copy" for prompt engineering.

---

### [`task_generate_prompt_from_description.md`]({% link _prompts/task_generate_prompt_from_description.md %})
**Purpose:** To generate a new, high-quality prompt from a user's description.

This prompt guides the AI to act as a prompt engineer, taking a high-level description of a task and generating a complete, well-structured prompt that follows the standards of this library.

**When to use it:**
*   When you have an idea for a new prompt but want the AI to help you write it.
*   To quickly create new prompts that are consistent with the existing ones in the library.

---

### [`task_repair_setup_script.md`]({% link _prompts/task_repair_setup_script.md %})
**Purpose:** To diagnose and repair the environment setup script so agent tasks stop failing before any code is written.

Jules' own FAQ names *"broken setup scripts or vague prompts"* as the common causes of a failed task, and notes that long-running processes such as dev servers or watch scripts are not supported in setup scripts. Because the environment is snapshotted once the script succeeds and reused for later tasks, a defect here is paid for by every future task rather than once. This prompt guides the AI to reproduce the failure from cold, rebuild the script from the sequence CI proves works, and verify the two things that stay invisible when a run goes well: that the script actually fails when an install fails, and that nothing in it blocks.

**When to use it:**
*   Before any other prompt in this library, on a repository an agent has not worked in before.
*   When tasks fail during setup, or fail with errors about a tool that was supposed to be installed.

---

### [`task_scope_a_vague_issue.md`]({% link _prompts/task_scope_a_vague_issue.md %})
**Purpose:** To turn an underspecified bug report into a reproducible, testable task before any fix is attempted.

The other half of what Jules' FAQ names as the common causes of a failed task. The failure is quiet rather than loud: given "the login is broken", an agent does not stop and ask, it guesses what broken means and builds on the guess, so the work looks complete and fixes something nobody reported. This prompt produces a minimal reproduction, a failing test that is checked to fail for the reported reason, and an explicit list of every ambiguity in the original issue with the reading taken for each. It deliberately produces no fix.

**When to use it:**
*   Before handing a thin bug report to an agent, especially one written by someone who is not the maintainer.
*   When a previous agent attempt "fixed" something that was not what was reported.

---

### [`task_audit_repo.md`]({% link _prompts/task_audit_repo.md %})
**Purpose:** To conduct a comprehensive, evidence-based audit of a repository or live website.

This prompt guides the AI to produce a detailed report on the project's current state, including its features, architecture, dependencies, security vulnerabilities, and performance metrics. It is a discovery-focused prompt and does not make any changes to the codebase.

**When to use it:**
*   When you are new to a project and need to understand how it works.
*   Before starting a major refactoring or migration project.
*   As a periodic health check for a project.

---

### [`task_build_api_frontend.md`]({% link _prompts/task_build_api_frontend.md %})
**Purpose:** To build a modern, functional frontend for an application based on its backend API.

This prompt guides the AI to read an existing backend, from a live endpoint, its API documentation, or its source, and build a frontend that actually matches it. It is aimed at the common case where a frontend is missing, outdated, or has drifted away from the API it is supposed to call.

**When to use it:**
*   When a working backend has no usable interface in front of it.
*   When the frontend and the API have diverged and the interface needs rebuilding against what the API really exposes.

---

### [`task_analyze_and_improve_ui_ux.md`]({% link _prompts/task_analyze_and_improve_ui_ux.md %})
**Purpose:** To analyze and improve the frontend UI/UX of a repository.

This prompt guides the AI to conduct a comprehensive analysis of the target website's UI/UX and produce a report with concrete suggestions for improvement. The suggestions should cover usability, visual design, and overall user experience.

**When to use it:**
*   When you want to improve the user experience of your website.
*   Before starting a major redesign of your website.
*   When you want to get a fresh perspective on your website's UI/UX.

---

### [`task_harden_repo_initial.md`]({% link _prompts/task_harden_repo_initial.md %})
**Purpose:** To perform a one-time, comprehensive hardening and baselining pass on a new or unmaintained repository.

This prompt guides the AI to set up a solid foundation for future development. It involves creating a CI/CD pipeline, adding linters, formatters, and smoke tests, establishing performance and accessibility baselines, and creating essential operational documentation.

**When to use it:**
*   On a brand new repository to set it up with best practices from the start.
*   On an existing repository that lacks modern CI/CD and testing infrastructure.

---

### [`task_harden_repo_iterative.md`]({% link _prompts/task_harden_repo_iterative.md %})
**Purpose:** To perform ongoing, iterative improvements to a repository that has already been hardened.

This prompt guides the AI to act as a senior developer or product steward, focusing on fixing instabilities, improving test coverage, and making small, high-impact feature enhancements. It uses a comprehensive "Verification Matrix" to ensure that all changes are safe and reliable.

**When to use it:**
*   For regular maintenance and improvement of a mature project.
*   To fix flaky tests and improve the reliability of the CI/CD pipeline.

---

### [`task_fix_and_refine.md`]({% link _prompts/task_fix_and_refine.md %})
**Purpose:** To transform a prototype or demo-quality project into a production-grade application.

This prompt guides the AI to identify the project's intended purpose, fix bugs, refactor suboptimal code, and improve reliability, maintainability, and robustness. It follows a "Test, Fix, Refine" workflow to ensure that all changes are covered by tests.

**When to use it:**
*   When you have a working prototype that needs to be made more robust.
*   To address technical debt and improve the overall quality of a codebase.

---


### [`task_build_from_plan.md`]({% link _prompts/task_build_from_plan.md %})
**Purpose:** To analyze a repository's blueprint/plan and current state, and iteratively implement the next logical steps to build a robust, production-grade system.

This prompt guides the AI to act as a lead developer, taking a project plan and executing it while using web research to make informed technical decisions and improvements.

**When to use it:**
*   When a project has a clear planning document but needs implementation.
*   To continue work on a partially completed project that has a defined roadmap.

---

### [`task_review_an_agent_pr.md`]({% link _prompts/task_review_an_agent_pr.md %})
**Purpose:** To review a pull request an agent wrote, against the failure modes agents actually have.

Agent-written pull requests fail differently from human ones, so a review habit built on human mistakes misses them. The danger named by practitioners is not that the code is bad but that it reads as finished: correct style, sensible names, a confident description, and tests that pass because they assert what the code does rather than what it should do. This prompt checks each claim the pull request makes about itself, and its central move is to break the code a new test covers and confirm the test goes red, because a test that passes against both the fixed and the broken version is not evidence of anything.

**When to use it:**
*   Before merging any pull request written by an agent, including your own.
*   When a change looks complete and you cannot say precisely which requirement each part of it satisfies.

---

### [`task_isolate_tests_from_services.md`]({% link _prompts/task_isolate_tests_from_services.md %})
**Purpose:** To make a test suite runnable in an agent's sandbox by removing its dependence on services it cannot start.

A suite that assumes a database, a broker or a live third-party API does not fail clearly inside an agent's environment. It fails partway through with a connection error, which the agent then reports as unrelated to its own changes before carrying on, so the work looks reviewed and was never tested. This prompt isolates the suite at the seams the project already has, and verifies the isolation twice over: by pointing the services at a dead port and re-running, and by reconciling the collected test count before and after so nothing has quietly stopped running.

**When to use it:**
*   When agent tasks fail with connection errors, or when an agent reports test failures as unrelated.
*   Before handing a repository to an agent for the first time, alongside `task_repair_setup_script.md`.

---

### [`task_security_review_agent_code.md`]({% link _prompts/task_security_review_agent_code.md %})
**Purpose:** To review a change an agent wrote for the security defects agents specifically introduce.

An agent asked to fix a failure finds the shortest route to the failure stopping, and that route is often to remove the thing that was objecting. The result is not a subtle logic flaw, it is a check that no longer checks, and it survives review because the diff looks like work: a scanner was added, an error was handled, a dependency was installed. This prompt targets that class directly, and its central move is to prove every check the change introduced can actually turn the build red by making it find something.

**When to use it:**
*   On any agent-written change that touches CI, dependencies, authentication, or anything handling input.
*   Alongside `task_review_an_agent_pr.md`, which covers whether the change does what it claims; this one covers what it costs.

---

### [`task_update_dependencies.md`]({% link _prompts/task_update_dependencies.md %})
**Purpose:** To update a project's dependencies to their latest compatible versions.

This prompt guides the AI to safely update dependencies while ensuring that all tests pass and the project remains stable. It follows an incremental approach and emphasizes the importance of reading changelogs to avoid breaking changes.

**When to use it:**
*   To keep a project's dependencies up-to-date and secure.
*   As a regular maintenance task to avoid falling too far behind on dependency versions.

---

### [`task_curate_repo.md`]({% link _prompts/task_curate_repo.md %})
**Purpose:** To analyze an unknown repository, make safe, reversible improvements, and provide a clear report.

This prompt is designed for situations where the content and structure of a repository are unknown or sensitive. It guides the AI to act as a careful curator, prioritizing safety and reversibility above all else. It makes only a small number of safe changes, such as adding a README or creating a metadata manifest.

**When to use it:**
*   When you encounter a repository with no documentation and need to understand its contents.
*   For bulk curation or triage of a large number of repositories.

---

### [`task_qa_an_agents_tests.md`]({% link _prompts/task_qa_an_agents_tests.md %})
**Purpose:** To find the tests an agent wrote that pass because they were written from the implementation, and cannot fail.

An agent asked to add tests will add tests, and they will pass. A test written while looking at the implementation asserts what the code does, and a test that asserts what the code does can never catch the code doing the wrong thing. The failure has no symptom: coverage rises, the suite is fast, the pull request reads as careful work, and the number of real regressions caught is zero. This prompt answers the question by mutation rather than by reading, breaking the behaviour each test names and recording whether it went red, then fixing or deleting the ones that did not.

**When to use it:**
*   After any agent-authored pull request that added or changed tests.
*   When coverage is high and regressions still reach production, which is the signature of this defect.

---

### [`task_fix_a_bug_test_first.md`]({% link _prompts/task_fix_a_bug_test_first.md %})
**Purpose:** To fix a reported bug in the only order that produces evidence the fix worked.

A fix written before its test is indistinguishable from a coincidence: the symptom stops, and nobody, including the author, can say whether the cause was removed or merely hidden. The quieter failure is a test that is written first, fails, and fails for the wrong reason, so a red tick from an import error gets spent as proof it never earned. This prompt requires the failing output to be read and checked against the report before any production code is touched, and it verifies afterwards that removing the fix turns the test red again.

**When to use it:**
*   For any bug that is already reproducible. If the report is vague, run `task_scope_a_vague_issue.md` first; it produces exactly the failing test this one begins with.
*   When a previous fix did not hold and nobody can tell whether it ever worked.

---

### [`task_repair_a_green_pipeline.md`]({% link _prompts/task_repair_a_green_pipeline.md %})
**Purpose:** To find the CI steps that pass because they are not running what they claim.

A red pipeline gets fixed within the hour because it blocks someone. A green one that checks nothing is never looked at, and it removes the habit of checking, because everyone now believes the check is happening. The causes are mechanical and none of them look like a bug: a test command matching no files exits 0, a pipe reports the exit code of `tee` rather than the check, a `paths:` filter stops matching so the job never runs. The common shape is that absence looks exactly like success. This prompt establishes step by step that each job can still fail, by introducing the defect it exists to catch, and makes each step print its coverage so a future empty run is visible.

**When to use it:**
*   On any pipeline that has been green for a long time, especially one that has never been red.
*   Before trusting CI as evidence in a review, and before adding new checks to it.

---

### [`task_verify_a_migration.md`]({% link _prompts/task_verify_a_migration.md %})
**Purpose:** To find what a database migration does at production row counts, on the production engine, and on the way back down.

Almost every migration is verified the same way: run it forward, once, on a development database, and if it exits 0 that is the whole test. Every property that can cause an outage is invisible under exactly those conditions. A backfill over forty million rows completes in three milliseconds over the twelve in dev. Adding a non-null column is instant on an empty table and rewrites the whole thing on a full one. A unique constraint applies cleanly to data that happens to contain no duplicates, and production is where the duplicates live. The rollback is worse, because it is usually fiction: the reverse half exists because the framework generated a slot for it and in most repositories it has never been executed once. This prompt measures on the production engine at real row counts, records the lock each statement takes rather than only the total runtime, runs the reverse half and diffs the schema to prove it restores what it claims, and establishes which of the application code and the schema can safely ship first.

**When to use it:**
*   Before any migration that touches a table with real data in it, which is most of them.
*   When the rollback has never been run, which is the normal case and is worth checking rather than assuming.

---

### [`task_prove_the_docs.md`]({% link _prompts/task_prove_the_docs.md %})
**Purpose:** To find the claims in the documentation that were true when they were written and are not true now.

Documentation does not fail loudly. Every sentence was true the day it was written, and nothing since has told anybody which ones stopped being true: there is no red tick for a stale document and no coverage report with a gap in it. The damage concentrates at the front door, because a quickstart is the first thing a new user runs and the last thing anyone with a working checkout re-runs, so it is at once the most important instructions in the repository and the least tested. There is a second failure worth knowing about before handing this task to an agent: asked to write documentation, it will read the names and the comments and produce fluent prose restating the same intent that was already wrong, now in a second place and sounding authoritative. This prompt extracts every checkable claim as its own line, gives each one a verdict and a piece of evidence by running it, and reruns the quickstart from a clean environment where the missing step is finally visible.

**When to use it:**
*   Before a release, and before pointing anyone new at the README.
*   After any rename of a flag, a default or a path, which are the claims that rot fastest.
*   Whenever a new user reports that the getting-started guide did not work for them, which is the symptom this exists to remove.

## Recommended Workflow

The prompts in this library are designed to be complementary and can be used together in a logical sequence. Here is a recommended workflow for taking a new or unmaintained project toward a more maintainable, verifiable state:

1.  **Repair the environment setup script.**
    *   **Prompt:** `task_repair_setup_script.md`
    *   **Goal:** To make the repository reliably usable by an agent at all.
    *   **Outcome:** Dependencies install from cold and the test suite runs to completion, so every later step has a working baseline instead of an assumed one.

2.  **Audit the repository.**
    *   **Prompt:** `task_audit_repo.md`
    *   **Goal:** To get a deep understanding of the project's current state.
    *   **Outcome:** A comprehensive audit report that will inform the next steps.

3.  **Harden the repository.**
    *   **Prompt:** `task_harden_repo_initial.md`
    *   **Goal:** To set up a modern CI/CD pipeline and testing infrastructure.
    *   **Outcome:** A repository with automated checks for quality, performance, and accessibility.

4.  **Fix and refine the codebase.**
    *   **Prompt:** `task_fix_and_refine.md`
    *   **Goal:** To address any bugs or architectural issues found in the audit.
    *   **Outcome:** A robust, reliable, and well-documented codebase.

5.  **Perform ongoing maintenance.**
    *   **Prompts:** `task_harden_repo_iterative.md` and `task_update_dependencies.md`
    *   **Goal:** To keep the project in a good state over time.
    *   **Outcome:** A project that is continuously improved and kept up-to-date.
