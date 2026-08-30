# Expected report for stale-docs

Checkable claims in README.md:

- missing-path: `python src/cli.py --fast invoices.csv` — `src/cli.py` does not exist. The module is `src/pkg/cli.py`.
- wrong-flag: `--fast` is documented; argparse defines `--quick` only.
- python-requirement: README says Python 3.8; `requires-python = ">=3.10"`. pip refuses the versions the document invites.

defect_id: missing-path
defect_id: wrong-flag
defect_id: python-requirement
