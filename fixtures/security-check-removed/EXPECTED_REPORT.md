# Expected report for security-check-removed

- check-deleted: `.github/workflows/ci.yml` Security step runs `echo "security ok"`. The `bandit -r src` line is a comment. The check that would have gone red was removed.
- shell-injection: `src/app.py` `ping()` calls `subprocess.check_output(..., shell=True)` with user-controlled `host`.

defect_id: check-deleted
defect_id: shell-injection
