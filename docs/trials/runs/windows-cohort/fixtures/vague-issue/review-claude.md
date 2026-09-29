# Review: vague-issue

| defect id | verdict | where the report says it | reason |
|---|---|---|---|
| unscoped-issue | identified | "ISSUE.md is only 'the login is broken / please fix'. The project has no tests, docs or history" | Notes no repro, expected behaviour; lists open questions including what the reporter saw. Environment not explicitly mentioned. |
| three-readings | identified | "Usernames are case-sensitive ... Lockout after one failure ... Empty password accepted" | All three located in login.py, each reproduced, with observed outputs that match the code. |
| no-fix | identified | "Nothing was fixed ... I made no change to login.py" | Produced repro.py and failing tests instead of a patch. |

Totals: 3 identified, 0 partial, 0 missed

False claims: none. Reading 2 "partly reproduced" (a correct login still returns True after a failure) is accurate to the code.
