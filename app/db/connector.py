import psycopg
from contextlib import contextmanager
from config import settings


@contextmanager
def get_cursor():
    with psycopg.connect(settings.dsn) as conn:
        with conn.cursor() as cur:
            yield cur
        conn.commit()
