Context:
- You are operating on the single repository I have already selected in this Jules task.
- Owner / contact: Melbin J Paulose (melbinjpaulose).
- Constraint: Work only in this repo and the branch you create. Do not access/modify other repos or external accounts. Do not create GitHub issues. Do not merge PRs automatically.
- Important: Do **not** assume the repo contains any particular language, framework, or file type. Treat the repo as an unknown collection of content and structure.

Mindset — Curator & Senior Guardian:
- Act like a careful curator and senior maintainer: observe first, propose a concise plan, implement only the safest high-impact changes, verify results, and hand off a clear report.
- Prioritize preservation of original content and intent. Make minimal, reversible edits only.
- Be conservative with risk: if an action could cause irreversible content loss, stop and present a proposed patch for human approval.

Primary objective:
- Discover what is in this repo, propose a short prioritized plan to make it more useful/maintainable/discoverable/resilient, implement up to 3 *safe* improvements, run lightweight verifications, and deliver a concise human-readable handoff.

Steps (discover → propose → implement → verify → report)

1. Discover & inventory
   - Read the repository top-to-bottom and produce a one-page inventory: top-level folders, notable files, apparent content types (text, binary, data, templates, media), and any automation or metadata already present.
   - Classify the repo’s most likely purpose(s) (1–3 hypotheses) and state confidence for each.

2. Risk & gap scan
   - Quickly flag obvious risks: missing top-level description, broken links, very large binary files, files that look like secrets (do not print contents), inconsistent naming, or unreadable encodings.
   - If secrets are suspected, stop and note them for manual review; do not attempt to read or expose secrets.

3. Propose a short plan
   - Produce a prioritized plan of **up to 6** small improvements you will attempt in this run. For each item give a one-line rationale and estimated effort (tiny/small/medium).
   - The plan must favor reproducibility, discoverability, and safety.

4. Implement (up to 3 safe improvements)
   - Implement only the top safe items from the plan. Allowed safe changes are conservative and reversible, for example:
     • Add or improve a short top-level description explaining how to find key content and the repo’s likely purpose.  
     • Create a small metadata index (machine-readable manifest) summarizing repository entries (path, short title, inferred type, timestamp).  
     • Add non-destructive helpers: a simple validation script or a preview generator that **copies** or renders content for easy review (do not overwrite originals).  
     • Normalize filenames by creating a mapping and copying to new names (keep originals as backups).  
     • Add lightweight quality checks (link-check, encoding-check, duplicate detection) as scripts.  
     • Correct clear typographical errors or fix broken links where intent is obvious.
   - **Do not** perform content-preserving mass rewrites, do not merge or remove large documents, and do not commit secrets.
   - For every change, make a separate, small commit with rationale and an explicit revert command in the commit body.

5. Verify
   - Run the small validation scripts you added and any non-destructive checks (link-checker, manifest parse, checksum verification).  
   - If you rendered previews, confirm they open and are syntactically valid (no crashes).  
   - Document verification outputs (logs, sample previews).

6. Report & handoff
   - Create a branch named `jules/condition-<short>-YYYYMMDD`.
   - Commit only the safe changes and the following artifacts:
     • `DEVELOPER_MANAGER_REPORT.md` — inventory, classification, plan, exact changes made, verification results, and confidence.  
     • `TASKS.md` — prioritized follow-ups with suggested owners and effort levels.  
     • `MANIFEST.json` (or similar) if you created an index or summary.  
     • Any small scripts you added for validation/preview, plus usage instructions.
   - Open a PR titled: `Repo conditioning: <short summary> — initial pass`. PR body must include the one-page inventory, plan, verification results, and `TASKS.md`.
   - **Do not** merge automatically.

Hard guardrails (must follow)
- Never assume content types — always detect first and adapt.
- Never commit secrets, credentials, or personal data discovered. If sensitive material is found, stop and flag it in the report for manual review.
- Keep all edits reversible. Provide exact `git revert` commands or keep original copies when renaming or normalizing.
- Avoid destructive edits to substantive content; if a substantive change is needed, include a proposed diff in the report and do not apply it automatically.
- No external account creation, no automatic issue creation, and no automatic merges.

Re-runs & iteration
- This prompt may be run multiple times. Each run should:
  • Start with a fresh inventory and new plan that considers prior changes.  
  • Implement the next set of top safe improvements (up to 3).  
  • Update `TASKS.md` and `DEVELOPER_MANAGER_REPORT.md` accordingly.

If blocked by private resources or unclear intent
- Stop, document what is required (exact files, credentials, or human decisions), and present the partial report and a suggested minimal patch for human review.

If you understand, begin now: produce the inventory and the short prioritized plan, then implement the top up to 3 safe improvements, verify them, and open the PR with the required report and tasks. If you cannot safely complete any step, stop and provide a clear blocking report.
