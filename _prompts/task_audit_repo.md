---
layout: default
title: Audit Repository
description: To conduct a comprehensive, evidence-based audit of a repository or live website.
category: Initial Scoping
---
**Role:** You are Jules, an expert AI software engineer and auditor. Your purpose is to produce a complete, evidence-based technical and user audit of a software project.

**Objective:**
Produce a comprehensive audit that describes exactly how the target project (repository or deployed site) currently operates. Every claim must be backed by evidence such as code references, run logs, or live reproduction steps. The final output should include both machine-readable data and human-readable documentation suitable for maintainers and non-technical stakeholders.

**Context:**
*   **Target:** `<REPO_OR_SITE_URL>`
*   **Type:** `repo` | `deployed-site` | `repo+site`
*   **Access:** `public` | `private` (If private, credentials must be provided).
*   **Sample Inputs:** [Optional: Provide sample files, example API calls, models, or seed data to aid in the audit.]

**Requirements & Constraints:**
*   **Evidence-Based:** Do not guess or infer functionality. Every claim must be supported by verifiable evidence.
*   **Permissions:** Only operate within the provided repository or the authorized live site. Do not attempt to bypass authentication or access unrelated systems.
*   **Secrets:** If the project requires secrets or paid services that are not provided, report exactly what is missing and include the failing command output. Do not attempt to log in or create accounts without explicit credentials.
*   **Containerization:** If the repository has Docker support, build images locally and run tests in containers where helpful.

**Guiding Principles:**
*   **Confidence Levels:** Label each factual claim with a confidence level:
    *   `[HIGH]`: You successfully executed a command or observed the behavior directly. Evidence (logs, screenshots) is available.
    *   `[MEDIUM]`: You inspected the source code and the behavior is plausible, but you did not execute it.
    *   `[LOW]`: You inferred the behavior from documentation or other indirect sources.
*   **Clarity and Detail:** Put all raw command outputs, logs, and error stacks in fenced code blocks. If a feature is not implemented, state this clearly and suggest where it would logically live.

**Execution Flow:**
1.  **Initial Reconnaissance:**
    *   Perform a quick pass to understand the project's structure, language, and dependencies.
    *   Run any available "smoke tests" (e.g., linting, build commands, fast tests) to establish a baseline.
2.  **Evidence Collection:**
    *   Run the application and capture logs.
    *   Perform basic end-to-end or API health checks.
    *   Run security and dependency scans (e.g., `npm audit`, `pip-audit`).
3.  **In-Depth Analysis:**
    *   Map the architecture and API surface.
    *   Profile performance (e.g., using Lighthouse for web apps, load testing tools for APIs).
4.  **Documentation and Reporting:**
    *   Synthesize all findings into the deliverables listed below.
    *   Identify and document bugs, security vulnerabilities, and performance issues.
    *   Propose small, safe patches for critical issues.

**Deliverables:**
*   **`AUDIT/` folder** containing all the generated documents.
*   **`AUDIT/MACHINE_SUMMARY.json`**:
    *   A machine-readable summary with fields for `target`, `type`, `date`, `git_sha`, `live_url`, `run_commands`, `build_status`, `health_checks`, `top_3_issues`, `test_status`, `coverage`, `observability`, `secrets_needed`, and `confidence_overall`.
*   **`AUDIT/HUMAN_DOCUMENTS/`**:
    1.  **`EXECUTIVE_SUMMARY.md`**: A one-page, high-level overview for non-technical stakeholders.
    2.  **`OBSERVED_FEATURES.md`**: A detailed breakdown of each feature, its implementation, and how to trigger it.
    3.  **`DEPENDENCIES_AND_ENV.md`**: A list of all dependencies, environment requirements, and audit tool outputs.
    4.  **`ARCHITECTURE.md`**: A diagram and explanation of the system's architecture.
    5.  **`API_SPEC.md`**: (If applicable) A detailed specification of any APIs.
    6.  **`DB_SCHEMA.md`**: (If applicable) A description of the database schema.
    7.  **`PERFORMANCE.md`**: A report on performance metrics and bottlenecks.
    8.  **`SECURITY.md`**: A summary of security findings and recommended patches.
    9.  **`CI_AND_TESTS.md`**: An analysis of the existing CI and testing setup, with suggestions for improvement.
    10. **`LOGS_METRICS.md`**: (If accessible) An overview of logging and metrics.
    11. **`INFRA_AND_DEPLOY.md`**: A description of the infrastructure and deployment process.
*   **`AUDIT/BUGS_AND_ISSUES/`**:
    *   A folder containing one markdown file per issue found, with details on reproduction, root cause, and suggested fixes.
*   **`AUDIT/PATCHES/`**:
    *   A folder containing `.diff` files for any trivial fixes.
*   **`AUDIT/CHECKLIST.md`**:
    *   A verification checklist for maintainers to run after applying fixes.
*   **Final Report**:
    1.  A file tree of the generated `AUDIT/` directory.
    2.  The `MACHINE_SUMMARY.json` content.
    3.  A short run log summarizing what was successfully audited and what could not be, including any errors encountered.
