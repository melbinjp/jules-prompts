# Expected report for setup-succeeds-while-failing

- swallowed-install: `pip install -r requirements.txt || true`. The package in requirements.txt does not exist. The script continues.
- blocking-server: `python -m http.server 8000` is a long-running process. A setup script must exit.
- no-set-e: there is no `set -e`. Failures after the `|| true` would also be silent.

defect_id: swallowed-install
defect_id: blocking-server
defect_id: no-set-e
