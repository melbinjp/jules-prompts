import contextlib
import os

import psycopg


@contextlib.contextmanager
def connection():
    with psycopg.connect(os.environ["DATABASE_URL"]) as db:
        yield db
