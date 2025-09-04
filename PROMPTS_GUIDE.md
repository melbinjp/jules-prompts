---
layout: default
---
# Jules Prompt Library Guide

This repository contains a curated library of pre-made, machine-readable task prompts that empower an AI software engineer like Jules to turn user intent into production-grade work. This guide explains the purpose of each prompt and provides a recommended workflow for using them together.

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

### [`task_audit_repo.md`]({% link _prompts/task_audit_repo.md %})
**Purpose:** To conduct a comprehensive, evidence-based audit of a repository or live website.

This prompt guides the AI to produce a detailed report on the project's current state, including its features, architecture, dependencies, security vulnerabilities, and performance metrics. It is a discovery-focused prompt and does not make any changes to the codebase.

**When to use it:**
*   When you are new to a project and need to understand how it works.
*   Before starting a major refactoring or migration project.
*   As a periodic health check for a project.

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


### [`task_build_from_plan.md`]({% link _prompts/task_build_from_plan.md%})
**Purpose:** To analyze a repository's blueprint/plan and current state, and iteratively implement the next logical steps to build a robust, production-grade system.

This prompt guides the AI to act as a lead developer, taking a project plan and executing it while using web research to make informed technical decisions and improvements.

**When to use it:**
*   When a project has a clear planning document but needs implementation.
*   To continue work on a partially completed project that has a defined roadmap.

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

## Recommended Workflow

The prompts in this library are designed to be complementary and can be used together in a logical sequence. Here is a recommended workflow for taking a new or unmaintained project to a production-ready state:

1.  **Audit the repository.**
    *   **Prompt:** `task_audit_repo.md`
    *   **Goal:** To get a deep understanding of the project's current state.
    *   **Outcome:** A comprehensive audit report that will inform the next steps.

2.  **Harden the repository.**
    *   **Prompt:** `task_harden_repo_initial.md`
    *   **Goal:** To set up a modern CI/CD pipeline and testing infrastructure.
    *   **Outcome:** A repository with automated checks for quality, performance, and accessibility.

3.  **Fix and refine the codebase.**
    *   **Prompt:** `task_fix_and_refine.md`
    *   **Goal:** To address any bugs or architectural issues found in the audit.
    *   **Outcome:** A robust, reliable, and well-documented codebase.

4.  **Perform ongoing maintenance.**
    *   **Prompts:** `task_harden_repo_iterative.md` and `task_update_dependencies.md`
    *   **Goal:** To keep the project in a good state over time.
    *   **Outcome:** A project that is continuously improved and kept up-to-date.
