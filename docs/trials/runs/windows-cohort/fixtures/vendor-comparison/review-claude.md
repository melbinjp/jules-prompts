# Review: vendor-comparison

| defect id | verdict | where the report says it | reason |
|---|---|---|---|
| criteria-not-from-measures | partial | "scored popularity and developer experience, which serve none of the project's success measures" | Popularity/DX from no measure is found and "$60 limit" is used, but it does not say cost was only a 30% weight instead of a hard limit, nor that M2 (stable links) was not a criterion; M1 not named. |
| missing-options | partial | "It compared only two options"; "Not evaluated: serving straight from the NAS" | Two-option flaw and NAS noted (NAS used as second copy in D0004), but doing nothing and the combined masters-on-NAS/host-for-serving option are not identified as omitted options. |
| egress-arithmetic | identified | "entered transfer as 5 GB instead of 5,000 GB, so it showed $23.45 ... $473.00 a month" | Correct error and corrected figure, computed in Docker. |
| vendor-claim-only | identified | "Its evidence was CloudA's own marketing page" | Correct; file why-cloud-a not named but source is clear. |
| unrepresentative-test | partial | "a 2 MB upload from the office" | Names the test but does not explain that it tests upload while the use is listeners downloading 60 MB shows. |
| door-misclassified | identified | "Marked as a reversible choice, but CloudA's standard tier has no custom domain, so every feed and blog link would be stuck on CloudA's hostname" | Correct reason (URL lock-in); also handles it in D0004 via a station-controlled domain. Missing approver/revisit-condition detail is minor ("had no approver" is mentioned). |

Totals: 3 identified, 3 partial, 0 missed

False claims: none found. The control D0002 is left accepted and its counts reproduced, which is correct. The "$473 a month" and CloudB "$55" figures match the fixture's expected numbers.
