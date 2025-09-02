---
layout: default
---
# Jules — Environment setup & AGENTS.md

> A clear, practical guide for repository owners to prepare environments so Jules (and other agents) run reliably. Drop this file at the root of a repo or add as a documentation page on jules-prompts.wecanuseai.com.

---

## Goal

Make it trivial for Jules to: clone your repo, install dependencies, run tests, and produce safe, reviewable changes. This document explains **when** to provide environment configuration, **what** to include, and **how** to validate it.

## Quick facts (what Jules does)

* Jules runs each task inside a secure, short-lived Ubuntu VM where it clones your repository, installs dependencies and runs commands you provide. Use AGENTS.md + a repository setup script to make Jules deterministic and fast.

## When you should add an environment setup

Add explicit setup instructions when your repo is non-trivial to build or test locally, for example:

* Monorepos or workspaces (pnpm/turbo/lerna)
* Native builds with long install steps (C/C++, Rust with large toolchains)
* Private registries or custom package registries
* Projects requiring specific SDKs, compilers, or system packages
* Repos that require multiple setup steps (db, migrations, prebuild steps)

If your project is simple (single `npm install && npm test`), Jules will often auto-detect — but an explicit script still helps reliability.

## Where Jules looks for guidance

1.  `AGENTS.md` (root) — a predictable, agent-focused markdown file describing build/test commands, conventions, and special notes. Jules will automatically read it if present.
2.  `README.md` — Jules will use it for hints when `AGENTS.md` isn’t available.
3.  Repository Configuration in the Jules UI (Codebase → Configuration → Initial Setup) — paste the setup script/commands there and use **Run and Snapshot** to validate.

## What to put in AGENTS.md (recommended structure)

Use Markdown. Keep it concise and machine-friendly with explicit commands.

Suggested sections:

*   **Dev environment / quickstart** (one-liner to start dev mode)
*   **Build & test commands** (exact commands Jules should run; prefer non-interactive CLI)
*   **Install / setup commands** (list or script path)
*   **Tooling / versions** (node, python, rust versions you expect)
*   **CI checklist** (what must succeed before a PR can be merged)
*   **Coding style / linting expectations**
*   **Security notes** (what not to run, secrets guidance)
*   **Contact / maintainers** (if Jules needs clarification)

Minimal example (put in `AGENTS.md`):

```markdown
# AGENTS.md

## Dev environment tips
- Install: `npm ci`
- Build: `npm run build`
- Test: `npm test -- --runInBand`

## Notes
- Use Node 18.x for local development
- Do not commit `.env` files; tests use mocked credentials
```

## Add a setup script (recommended)

Put the commands needed to install dependencies and run tests into the Jules repo Configuration -> Initial Setup box (or provide a script file in repo and reference it). Example steps you can paste:

*   Open the Jules UI → select the repository → **Configuration** → **Initial Setup**.
*   In *Initial Setup*, enter the shell commands Jules should run to prepare the environment.
*   Click **Run and Snapshot** to run the script and capture a reproducible environment snapshot.

Why the snapshot matters: when successful, Jules will save an environment snapshot and re-use it for later tasks for faster, more reliable runs.

## Example setup scripts (copy-paste and adapt)

### Node / JavaScript (recommended: use lockfile-aware install)

```bash
# repo root: setup_jules.sh
set -euo pipefail
echo "--- environment checks ---"
node -v
npm -v || pnpm -v || yarn -v

# install dependencies
npm ci
# run lint and tests
npm run lint --if-present || true
npm test --if-present
```

### Python (venv + requirements)

```bash
set -euo pipefail
python -V
python -m venv .venv
. .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
# run tests
pytest -q
```

### Go

```bash
set -euo pipefail
go version
# ensure module cache and build
go mod download
go test ./...
```

### Rust

```bash
set -euo pipefail
rustup --version || true
rustc --version
cargo build --all --release
cargo test --all
```

### Java / Maven

```bash
set -euo pipefail
java -version
mvn -v
mvn -B -DskipTests=false test
```

## Validation & Run-and-Snapshot checklist

*   Make the script **idempotent** and **fast** where possible.
*   Print version checks (`node -v`, `python -V`) so validation shows which runtime was used.
*   Keep output non-interactive (pass `--yes` / `-y` flags as needed).
*   Use `set -euo pipefail` for bash scripts so failures are visible.
*   Click **Run and Snapshot** in Jules: fix any failing steps and iterate until successful.

## Handling secrets safely

*   **Do not commit secrets** to the repo. Jules documentation and community discussions explicitly warn against committing tokens or secret files.
*   If your task needs secrets (API keys), prefer external secret stores or CI-style secrets injected at runtime. Jules does not recommend committing tokens; specific secret-injection mechanisms are not documented publicly — contact Jules support or use a secure secret manager and document retrieval logic in `AGENTS.md` (e.g., "use project secret manager X to fetch credentials during CI").

## Troubleshooting common environment issues

*   **Dependency mismatch**: pin versions in `package.json`, `requirements.txt`, or toolchain config.
*   **Long setup times**: create a snapshot after validating; Jules will reuse snapshots to speed up subsequent runs.
*   **Failing tests locally but OK in CI**: print environment variables and runtime versions to compare.
*   **Missing system packages**: add `apt-get install` lines in setup script (be explicit and minimal).

If a task fails due to environment setup, Jules will report logs and an error page you can use to debug. Use the error logs to iterate on the setup script.

## Best practices & advanced tips

*   Prefer lockfile installs (`npm ci`, `pip-compile`/`pip install -r`, `go mod download`) for reproducibility.
*   Keep install steps minimal and only what tests need (avoid installing heavy optional tools unless required).
*   For monorepos, add package-level `AGENTS.md` files so Jules can find package-specific steps.
*   Add a `verify-environment.sh` script that runs quick sanity checks (versions, lints, smoke tests) and call it from the Jules configuration to make validation easier.
*   If your build needs private packages, document the exact auth method in `AGENTS.md` (do not include the secret itself).

## What to add to the jules-prompts site README/page

*   A concise note pointing users to the repo root `AGENTS.md` and to the Jules repo **Configuration → Initial Setup** where they can paste their setup script.
*   Include the sample scripts from this file and a short checklist (Run & Snapshot; idempotent; print versions; avoid secrets).

---

## Where I pulled authoritative guidance

This guide follows official Jules docs and the AGENTS.md recommendation. Keep your AGENTS.md small and explicit — agents read it first.
