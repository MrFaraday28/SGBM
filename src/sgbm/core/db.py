"""Acceso a PostgreSQL. Solo los repositorios importan este módulo."""

from collections.abc import Iterator
from contextlib import contextmanager

from psycopg import Connection
from psycopg.rows import dict_row
from psycopg_pool import ConnectionPool

from sgbm.config import DB

_pool: ConnectionPool | None = None


def _obtener_pool() -> ConnectionPool:
    global _pool
    if _pool is None:
        _pool = ConnectionPool(DB.dsn, min_size=1, max_size=4, kwargs={"row_factory": dict_row})
    return _pool


@contextmanager
def conexion() -> Iterator[Connection]:
    """Entrega una conexión con transacción: commit al salir, rollback si hay excepción."""
    with _obtener_pool().connection() as conn:
        yield conn


def cerrar() -> None:
    global _pool
    if _pool is not None:
        _pool.close()
        _pool = None
