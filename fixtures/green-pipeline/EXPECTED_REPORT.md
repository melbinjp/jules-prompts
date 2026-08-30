# Expected report for green-pipeline

The workflow is green because it does not run.

- paths-never-match: `on.pull_request.paths` is `legacy/**`. There is no legacy/ directory. The job does not run on a normal pull request.
- wrong-test-dir: the test step is `python -m pytest test/`. Tests live in `tests/`. A matching-nothing pytest run is not a passing suite.
- pipe-to-tee: `| tee pytest.log` means the step's exit code is tee's, not pytest's.
- continue-on-error: the security job is `exit 1` under `continue-on-error: true`.

`src/app.py` add(1,1) returns 3. `tests/test_app.py` would catch it. That is evidence the pipeline is not a check.

defect_id: paths-never-match
defect_id: wrong-test-dir
defect_id: pipe-to-tee
defect_id: continue-on-error
