Context:
- You are operating on the single repository I already selected in this Jules task.
- Owner/contact: Melbin J Paulose (melbinjpaulose).
- Constraint: Work only inside this repo and the branch you create. Do not access/modify other repos or external accounts. Do not create GitHub issues. Do not merge PRs automatically.

Goal (one sentence):
Perform a one-time, comprehensive hardening & baseline pass so this HTML/CSS/JS frontend (and any co-located backend) becomes a production-ready, testable, and documented repository suitable for iterative maintenance.

Adaptive behavior (detect & act):
1. Detect whether this repo contains:
   - Frontend-only (static site / SPA): presence of `index.html`, `package.json` with build scripts, typical frontend dirs.
   - Backend present (Python/Node/etc. + server entrypoint): presence of `pyproject.toml`/`requirements.txt`/`app.js`/`server.js`/`Dockerfile`/`docker-compose.yml`.
2. Adjust workflow:
   - If backend **exists in same repo**: start it during verification (prefer `docker-compose up --build` if present; else use documented start command). Use ephemeral local DB containers for integration tests where needed. Do not use production credentials.
   - If backend **is separate**: do not change it. Validate public health endpoints and provide instructions / CI hooks for full E2E that will run later when the other repo is available.

Deliverables (what to add & open as PRs):
- A branch: `jules/site-hardening-1` (create it in this task).
- `.github/workflows/ci.yml` that:
  - Builds the site (npm build / npm ci or python packaging as appropriate).
  - Runs linters & formatters.
  - Runs unit tests, type checks, and coverage reports.
  - Runs smoke tests (fast checks) and integration tests (only if backend runs here or via local containers).
  - Runs accessibility audits (axe-core) on the main page(s) if HTML present.
  - Runs Lighthouse CI (mobile+desktop) and records baseline reports.
  - Uploads build artifact and uses `actions/upload-pages-artifact` + `actions/deploy-pages` (if GH Pages) — but **do not** deploy automatically; deployment must be gated.
  - If any job requires secrets not present in Jules environment, fail with a clear message and create/update `.github/SECRET_TEMPLATE.md`.
- `.github/OPERATIONS.md` describing how CI works, how to run smoke tests locally, how to run backend locally (start commands), and rollback instructions.
- `.github/SECRET_TEMPLATE.md` listing any required secrets and how to set them in GitHub Actions.
- `PERFORMANCE_BASELINE.md` with attached Lighthouse outputs or a path to reports and short interpretation.
- `TEST_FINALIZATION.md` template for the second-phase verification process (content-only, no secrets).
- `TASKS.md` with prioritized follow-ups (security, accessibility, performance improvements).
- Optional: a minimal `Dockerfile` and `docker-compose.yml` if not present and it is safe to add (only when this will help run integration tests locally).

Initial checks & smoke tests to add:
- Root loads (HTTP 200) after build.
- `/health` (or equivalent) returns OK JSON.
- Main nav and primary CTA are reachable.
- External links referenced on primary pages return 200 or are clearly marked as external.
- If backend present: a simple contract/health check for any API endpoints used by the frontend.

CI behavior & gating:
- CI must **not** deploy to production automatically. Add gates: tests, accessibility, and Lighthouse budgets must pass for any deploy job to run.
- If a required secret is missing, CI should fail fast and print `.github/SECRET_TEMPLATE.md` instructions in logs.

Branch / PR behavior:
- Create branch `jules/site-hardening-1` and commit the above changes.
- Run the CI jobs (trigger GitHub Actions or emulate them). If tests that do not require unavailable secrets pass, open PR titled: `Site hardening: CI, baseline, docs`. In the PR body include:
  - Short inventory of repo (frontend-only / frontend+backend), what was added, and how to run locally.
  - Lighthouse baseline summary, axe summary, and smoke test results.
  - `TASKS.md` with follow-ups.
  - Statement: “This is an initial hardening pass. Further verification/finalization should use the verification prompt; proceed only after review.”
- Do **not** merge automatically.

Backend handling rules (explicit):
- If a backend exists in-repo:
  - Attempt to start it in the task environment for integration tests using `docker-compose` or the repo start script. If it needs environment variables/secrets, **do not** use production values — instead:
    - Use safe local mocks (e.g., local sqlite, test containers) OR
    - Fail with a clear message and add required values to `.github/SECRET_TEMPLATE.md`.
  - Add lightweight integration tests that validate major API contracts used by the frontend.
- If backend is external/separate:
  - Validate endpoints reachable (health checks) but do not change external systems or secrets.
  - Document how a full E2E verification should be run when backend and frontend are both available (link to runbook + required secrets).

Acceptance criteria for this initial pass:
- Branch `jules/site-hardening-1` created with CI workflow, docs, and baseline artifacts.  
- CI runs triggered: jobs that can run without unavailable secrets have executed and passed (unit tests / linters / smoke).  
- Lighthouse and axe baseline produced if buildable in this environment — else note constraints in PR.  
- PR created with inventory, baseline, TASKS.md, and clear next steps for full verification.

If puzzles or missing pieces block CI (e.g., private API keys), do not invent or commit secrets — fail clearly, attach `.github/SECRET_TEMPLATE.md` and add precise instructions in the PR for what the reviewer must supply to complete verification.

If you understand, create branch `jules/site-hardening-1`, implement the CI and docs described, run the jobs you can, attach baseline artifacts or document constraints, and open the PR `Site hardening: CI, baseline, docs`. Do not merge automatically.
