# chore: bump all dependencies

Ran `npm update --latest` and committed the result. All tests pass in CI.

    $ npm update --latest
    added 4 packages, changed 63 packages, audited 412 packages in 11s
    + report-kit@4.0.0
      └─ pdf-weave@2.1.0 (AGPL-3.0-only)

Kept lodash on 4.17.15 because the newer one broke `tests/merge.test.js`.
