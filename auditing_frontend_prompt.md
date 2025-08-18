TARGET (replace): <REPO_OR_SITE_URL>
TYPE: repo | deployed-site
ACCESS: public | private (if private, attach credentials or point to PR with token)
SAMPLE_ASSETS: <optional sample model / sample pages / example inputs>

Goal
Produce a complete, evidence-based technical and user document describing exactly how the target site or repository currently operates. Do not guess — every claim must be backed by code references, logs, or live reproduction steps.

Deliverables (produce as separate files and a short machine-readable JSON summary):

A) MACHINE_SUMMARY.json
 - short fields: {target, type, date, git_sha (if repo), live_url (if site), run_commands[], build_status, top_3_issues[], confidence_overall}

B) HUMAN DOCUMENTS (separate files)
 1. EXECUTIVE_SUMMARY.md (1 page)
    - user-facing: what it does and how to open/use it
    - top-3 prioritized next steps
    - confidence labels per sentence [HIGH|MEDIUM|LOW]

 2. OBSERVED_FEATURES.md
    - For each feature:
      * Feature name
      * Implementation location: file path(s), function/class names,  <=25 lines of core code snippet
      * How to trigger (exact commands, URLs, sample files)
      * Observed behavior (step-by-step), expected behaviour, and evidence (screenshots, console logs)
      * Confidence label

 3. DEPENDENCIES_AND_ENV.md
    - package.json / requirements / gemfile + exact versions
    - Node / Python / Browser targets from files or CI
    - `npm audit` or equivalent output (paste raw)
    - Exact build & run commands that succeed on a fresh clone (or full error logs if they fail)

 4. ARCHITECTURE.md
    - textual architecture diagram (entry points, rendering pipeline, asset loaders, UI, API)
    - file map listing which folders implement renderer, controls, loaders, UI, state
    - runtime assumptions (WebGL1/2, WASM etc.)

 5. BUGS_AND_ISSUES/ (folder)
    - One .md per issue with:
      * Title, severity, reproduction (exact commands + sample files), expected vs actual, root-cause (file + line), suggested patch (diff or snippet), tests to add, confidence

 6. PERFORMANCE.md
    - Measured metrics (FPS, load time, memory) on one desktop and one mobile profile OR exact reason measurement couldn't run
    - Bottleneck analysis and suggestions (LOD, lazy-load, texture compression)

 7. SECURITY.md
    - Third-party assets, CDN usage, potential XSS/unsafe-eval points, recommended dependency upgrades (exact `npm`/`yarn` commands)

 8. CI_AND_TESTS.md
    - Suggested GitHub Actions workflow snippet
    - Minimal automated smoke test (Playwright/Puppeteer script) that loads a sample page/model, asserts canvas rendering and no console errors

 9. PATCHES/ (folder)
    - .diff files for trivial fixes
    - PR templates and recommended branch names

 10. CHECKLIST.md
    - Verification checklist the maintainer should run after each fix (exact commands + DOM/assertions + sample files)

Output formatting rules
 - Put raw command outputs, logs, and error stacks in fenced blocks.
 - For any step you actually ran, add evidence: `screenshots/` files, or `logs/` files and mark those in MACHINE_SUMMARY.json.
 - For every factual claim, include a confidence label: [HIGH] (I ran it / saw logs), [MEDIUM] (I inspected code + plausible run), [LOW] (inferred from docs only).
 - If a feature is not implemented say "NOT IMPLEMENTED" and point to where it would logically live and how to implement it (file + short code sketch).

Permissions & constraints
 - Only operate inside the provided repo or live site. Do not attempt accounts or external systems without explicit credentials.
 - If build/run requires secrets or paid services that are not provided, report precisely what is missing and include the failing command output.

When finished, return:
 1) The file/folder list (tree) with clickable attachments for logs/screenshots (or paste inline).
 2) MACHINE_SUMMARY.json
 3) A short run log summarizing what you could and could not reproduce and why.

End.
