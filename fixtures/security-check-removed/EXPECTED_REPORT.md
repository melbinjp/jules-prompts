# Expected report for security-check-removed

- check-deleted: `.github/workflows/ci.yml` Security step runs `echo "security ok"`. The `bandit -r src` line is a comment. The check that would have gone red was removed.
- shell-injection: `src/app.py` `ping()` calls `subprocess.check_output(..., shell=True)` with user-controlled `host`.

defect_id: check-deleted
defect_id: shell-injection

## October 1 evidence-record extension


- security-scope-by-filename: CHANGE_REVIEW excludes declared CI, examples/sample.env and dependency artifacts by filename yet calls the security review complete. Account for the entire supplied patch and actual input, credential and permission consequences. The sample.env value is explicitly synthetic; do not invent a live credential leak. Original inert bandit and shell injection findings remain.
- dependency-provenance-unchecked: requests familiarity does not establish provenance. Record exact requests version 2.32.3, resolved source, import/use in candidate-import.py and manifest/lock consistency. Source/lock evidence is absent here: request or verify it, or mark the dependency unverified, rather than declare it malicious or safe from its name. No remote dependency fetch is required to review this planted omission.


defect_id: security-scope-by-filename
defect_id: dependency-provenance-unchecked
