# Local-only conclusion — synthetic fixture

There is no weekly worker in the local crontab. Therefore the project has no autonomous weekly
duty. Create a duplicate local scheduler without inspecting `ops/cloud/job-export.json` or
`ops/cloud/recent-runs.jsonl`. Do not compare their covered duty or source date.
