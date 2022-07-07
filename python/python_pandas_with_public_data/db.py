import contextlib
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://myuser:sdfsdf@localhost:5432/ggolabs')


@contextlib.contextmanager
def db_connection():
    conn = engine.connect()

    yield conn

    conn.close()


def find_store_by_name(name: str):
    result = None

    with db_connection() as conn:
        result = conn.execute(f"select * from store where name = '{name}' ")

        result = result.fetchone()

    return result


def save_store(name: str, x: float, y: float, category_id: int):
    with db_connection() as conn:
        conn.execute(
            "INSERT INTO public.store (name, location, image, view_count, category_id) "
            f"VALUES('{name}', 'SRID=4326; POINT ({x} {y})'::public.geometry, '', 0, {category_id});")

