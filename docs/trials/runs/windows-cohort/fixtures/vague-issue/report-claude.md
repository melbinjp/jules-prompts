Nothing was fixed, because I don't know what the reporter meant by "broken". I scoped the issue instead, as the conductor prescribes for a vague issue. Everything ran in Docker and I made no change to login.py.

ISSUE.md is only "the login is broken / please fix". The project has no tests, docs or history, so nothing says what the login should do. The only hint is a comment in login.py listing three possible meanings of "broken". I reproduced all three (repro.py):

1. Usernames are case-sensitive: `ada` with the right password raises RuntimeError("locked") instead of returning False. Reproduced.
2. Lockout after one failure, never reset: any failed attempt raises "locked" instead of returning False and the counter is never reset. Nobody is actually locked out: a correct login still returns True afterwards. Partly reproduced.
3. Empty password accepted for a known user: `Ada` with an empty password returns True. Reproduced. This is a real security defect under any plausible spec and the first candidate for the fix.

I wrote test_login_readings.py: a baseline test plus one test per reading. Run: baseline passes, readings 1 and 2 error with RuntimeError: locked, reading 3 fails with True is not false. The expected behaviour in tests 1 and 2 is my assumption; test 3 is the least ambiguous. Full scoping record in SCOPING.md. I left readings 1 and 2 unfixed because they change behaviour callers may rely on and the owner wasn't available.

Questions for the owner (assumption made): what did the reporter actually see? (unknown, all three recorded); should usernames be case-insensitive? (weakly yes); what should a wrong password do and what lockout policy applies? (returns False, no policy invented); should an empty password be rejected? (yes); does anything else depend on the exception? (unknown).

Counts: 3 readings reproduced (1 only partly), 3 tests failing as intended, 1 baseline test verified, 0 fixes made, 5 open questions.
