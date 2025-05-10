import psycopg
from contextlib import contextmanager
from app.config.config import settings


@contextmanager
def get_cursor():
    with psycopg.connect(settings.dsn) as conn:
        with conn.cursor() as cur:
            yield cur
        conn.commit()
