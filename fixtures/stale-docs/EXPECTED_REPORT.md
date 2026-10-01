# Expected report for stale-docs

Checkable claims in README.md:

- missing-path: `python src/cli.py --fast invoices.csv`: `src/cli.py` does not exist. The module is `src/pkg/cli.py`.
- wrong-flag: `--fast` is documented; argparse defines `--quick` only.
- python-requirement: README says Python 3.8; `requires-python = ">=3.10"`. pip refuses the versions the document invites.

defect_id: missing-path
defect_id: wrong-flag
defect_id: python-requirement

## October 1 evidence-record extension


- unverifiable-claim-no-remedy: PUBLIC_COPY's fastest-at-every-workload promise needs concrete measurable wording and representative verification conditions, a verification plan or an authorised removal proposal. Do not call it true, merely polish it or silently delete an accepted requirement. Keep unresolved material claims and their concrete remedy visible.
- repeated-claims-no-authority: POLICY.md says seven days; public and confirmation copies say thirty. Agreement between copies does not verify authority or execution. Reconcile their material retention promise against the accepted policy and its current implementation, update all affected surfaces within authority, and mark actual expiry unverified until observed. Keep implementation details out of public prose unless the reader needs them.


defect_id: unverifiable-claim-no-remedy
defect_id: repeated-claims-no-authority
