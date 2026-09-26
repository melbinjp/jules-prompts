# Before the change (main, with PostgreSQL, Redis and the sandbox running)

    $ pytest
    collected 212 items
    212 passed in 48.30s

# After the change (clean checkout, no services)

    $ pytest
    collected 208 items
    38 passed, 170 skipped in 1.92s

# After the change (clean checkout, no services, one test file on its own)

    $ pytest tests/test_rate_limit.py
    E   redis.exceptions.ConnectionError: Error 111 connecting to localhost:6379. Connection refused.
    ERROR tests/test_rate_limit.py
