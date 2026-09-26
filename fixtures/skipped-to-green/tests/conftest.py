import os

import psycopg
import pytest


def db_available():
    try:
        psycopg.connect(os.environ.get("DATABASE_URL", "postgresql://localhost/ledgerly"), connect_timeout=1).close()
        return True
    except psycopg.OperationalError:
        return False


if not db_available():
    pytest.skip("database not available", allow_module_level=True)
