TARGET: <REPO_OR_SITE_URL>            # REQUIRED - repo URL or deployed site root URL
TYPE: repo | deployed-site | repo+site
ACCESS: public | private             # If private, attach credentials or point to PR with token
SAMPLE_INPUTS: <optional sample files, example API calls, model(s), seed data>

GOAL
Produce a complete, evidence-based technical + user audit that describes exactly how the target (site or repo) currently operates. Do not guess. Every claim must be backed by code references, run logs, or live reproduction steps. Produce machine-readable outputs plus human documents suitable for maintainers and non-technical stakeholders.

REQUIREMENTS / DELIVERABLES (produce each as separate files in repo under `AUDIT/` or return inline):

A) MACHINE_SUMMARY.json
- fields (all present even if null):
  {
    "target": "<TARGET>",
    "type": "repo|deployed-site|both",
    "date": "YYYY-MM-DD",
    "git_sha": "<commit>" (if repo),
    "live_url": "<if site>",
    "run_commands": ["exact shell commands used"],
    "build_status": "success|failed",
    "health_checks": {"http_root":200, "health_endpoint":200, ...},
    "top_3_issues": ["short strings"],
    "test_status": {"unit": "pass|fail", "integration": "pass|fail", "e2e": "pass|fail"},
    "coverage": "<% or null>",
    "observability": {"has_logs":true, "has_metrics":true, "monitoring": "prometheus|sentry|none"},
    "secrets_needed": ["ENV_VAR_1","DB_URL",...],
    "confidence_overall": "[HIGH|MEDIUM|LOW]"
  }

B) HUMAN DOCUMENTS (separate files)
 1. EXECUTIVE_SUMMARY.md (1 page)
    - Short user-facing description: what it does and how to use it.
    - Top-3 prioritized next steps.
    - Per-sentence confidence label [HIGH|MEDIUM|LOW].

 2. OBSERVED_FEATURES.md
    - For each *feature / capability* (frontend widget, API endpoint, CLI command, worker job, model):
      * Feature name (short)
      * Implementation location: file path(s), function/class names, <=25 lines of core code snippet.
      * How to trigger: exact steps, commands, example HTTP request (curl), or file inputs.
      * Observed behavior (step-by-step), expected behavior, and evidence (logs, console output, HTTP response).
      * Confidence label.

 3. DEPENDENCIES_AND_ENV.md
    - package.json / requirements.txt / Pipfile / Gemfile with exact versions.
    - Runtime targets (Node / Python / Java / Docker, OS, Browser targets noted).
    - Raw outputs from `npm audit`, `pip-audit`, `mvn dependency:tree`, or similar.
    - Exact build & run commands that succeed on a fresh clone (or full error logs if they fail).
    - Container image names/tags if present.

 4. ARCHITECTURE.md
    - Textual architecture diagram (entry points, components, data flows).
    - For backend: diagram of API surface, workers/cron jobs, DBs, caches, message brokers.
    - For infra: IaC mapping (Cloud formation/Terraform paths).
    - File map: which folders/files implement APIs, UI, jobs, models, infra.
    - Runtime assumptions and requirements (e.g., requires DB migrations run first).

 5. API_SPEC.md (if repo exposes HTTP/RPC API)
    - List all endpoints with method, path, auth type, expected payloads, sample requests/responses, status codes.
    - Where implemented (file + function), related tests, and example `curl` calls used to validate.

 6. DB_SCHEMA.md (if applicable)
    - Current DB type, connection string placeholder, migration tool and migration status.
    - Schema summary (tables/collections, primary keys, indices) with file/line refs to migrations or ORM models.
    - Data retention, size estimates, and known costly queries (if available).

 7. BUGS_AND_ISSUES/ (folder)
    - One `.md` per issue found:
      * Title, severity (critical/high/medium/low)
      * Reproduction steps (exact commands, sample data)
      * Expected vs actual
      * Root-cause hypothesis (file + line)
      * Suggested patch (diff or code snippet)
      * Tests to add (unit/integration/e2e)
      * Confidence label

 8. PERFORMANCE.md
    - Measured metrics when possible: response latency (p95), throughput, memory usage, CPU, FPS (for frontends), load times.
    - Test harness commands and tool versions (e.g., `hey`, `wrk`, Chrome Lighthouse).
    - Bottlenecks and suggestions (caching, DB indices, LOD, lazy loading).

 9. SECURITY.md
    - Third-party dependencies and CDN usage, SRI presence.
    - Auth models, secret handling, cookie security, CSP suggestions.
    - Potential injection/XSS/CSRF/SSRF/privilege escalation points with file refs.
    - Exact `npm`/`yarn`/`pip` commands to upgrade or patch offending libraries.

10. CI_AND_TESTS.md
    - CI workflow snippet (GitHub Actions) for build/test/lint/deploy.
    - Minimal automated smoke tests (unit, integration, e2e) and a Playwright/Puppeteer script (for web) or HTTP health-check scripts (for APIs).
    - Commands used to run tests and their raw outputs.

11. LOGS_METRICS.md (if accessible)
    - How to access logs and metrics locally or remotely.
    - Recent error samples and stack traces (redact secrets).
    - Observability gaps and recommended metrics/traces to add.

12. INFRA_AND_DEPLOY.md
    - Deployment steps, expected environment variables, cloud resources, container push commands.
    - Rollback instructions and maintenance windows.
    - IaC files and where to run them.

13. PATCHES/ (folder)
    - .diff files for trivial fixes and PR-ready patch files.
    - PR templates and recommended branch names.

14. CHECKLIST.md
    - Final verification checklist to run after each fix (exact shell commands, HTTP checks, and expected outputs/DOM assertions).

OUTPUT FORMAT RULES
 - Put raw command outputs, logs, and error stacks in fenced code blocks.
 - For everything actually run, provide artifacts (screenshots/logs) and mark them in MACHINE_SUMMARY.json with paths.
 - Label each factual claim with confidence: [HIGH] ran it / saw logs, [MEDIUM] inspected code + plausible run, [LOW] inferred from docs only.
 - If a feature is NOT IMPLEMENTED say so and indicate where it would logically live and include a code sketch.
 - If private secrets, 3rd-party services, or paid resources are required and not provided, list them under `secrets_needed` with exact env var names and sample values (redacted).
 - When dealing with backend services, do not attempt login/account creation without explicit credentials. Instead, describe required credentials and the exact commands to provide them.

PERMISSIONS & CONSTRAINTS
 - Only operate inside the provided repo or the public/authorized live site. Do not attempt to bypass auth or access unrelated accounts.
 - If a run requires secrets or paid services that are not provided, report precisely what is missing and paste failing command outputs.
 - If the repo has Docker support, build images locally and run tests in containers where helpful.

WHEN FINISHED, RETURN:
 1) The generated file/folder list (tree) and attachments for logs/screenshots (or paste inline).
 2) MACHINE_SUMMARY.json
 3) A short run log summarizing what was run, what could not be run, and why (exact errors).

ADDITIONAL GUIDANCE / TASK ORDER (recommended)
 1. Minimal smoke: run lint/build/test to establish baseline (quick win).
 2. Evidence collection: capture logs, run basic end-to-end or API health checks.
 3. Security & dependency scan (npm/pip audit).
 4. Architecture & API mapping.
 5. Performance profiling (load tests or Lighthouse).
 6. Patches & small PRs for critical/security/perf fixes.
 7. Larger refactors only after tests and CI are in place.
 8. For major infra changes, create feature branch and include runbook + rollback instructions.

CONFIDENCE RULES
 - Use [HIGH] only if you executed the step and have raw logs.
 - Use [MEDIUM] if you inspected code or static files.
 - Use [LOW] for claims derived only from README or docs.

END.
