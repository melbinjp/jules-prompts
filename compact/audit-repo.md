# Audit Repository: short form

To conduct a comprehensive, evidence-based audit of a repository or live website.

For small or local models with a short context. The full skill, with the reasons and methods behind each rule, is `skills/audit-repo/SKILL.md`; use it whenever the context allows. Works in any harness, needs no hosted service, and sends nothing beyond the project's confidentiality rules.

Fill in: `<REPO_OR_SITE_URL>`

## Objective

Produce a comprehensive audit that describes exactly how the target project (repository or deployed site) currently operates. Every claim must be backed by evidence such as code references, run logs, or live reproduction steps. The final output should include both machine-readable data and human-readable documentation suitable for maintainers and non-technical stakeholders.

## Rules

- Evidence-Based: Do not guess or infer functionality.
- Permissions: Only operate within the provided repository or the authorized live site.
- Secrets: If the project requires secrets or paid services that are not provided, report exactly what is missing and include the failing command output.
- Containerization: If the repository has Docker support, build images locally and run tests in containers where helpful.

## Steps

1. Initial Reconnaissance:
2. Evidence Collection:
3. In-Depth Analysis:
4. Documentation and Reporting:

## Deliver

- `AUDIT/` folder containing all the generated documents.
- `AUDIT/MACHINE_SUMMARY.json`:
- `AUDIT/HUMAN_DOCUMENTS/`:
- `AUDIT/BUGS_AND_ISSUES/`:
- `AUDIT/PATCHES/`:
- `AUDIT/CHECKLIST.md`:
- Final Report:
