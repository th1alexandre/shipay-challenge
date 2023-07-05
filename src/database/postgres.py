import os

import psycopg
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def _connect_pg(
    user: str, password: str, host: str, port: int, database: str, **kwargs
):
    try:
        return psycopg.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            dbname=database,
            **kwargs,
        )
    except Exception as e:
        raise Exception(f"Error connecting to PostgreSQL: {e}")


def conn_postgres(engine: Engine = None, **kwargs):
    try:
        if engine:
            return engine.connect()

        user = os.getenv("POSTGRES_USER", "postgres")
        password = os.getenv("POSTGRES_PASSWORD", "postgres")
        host = os.getenv("POSTGRES_HOST", "postgres")
        port = os.getenv("POSTGRES_PORT", 5432)
        database = os.getenv("POSTGRES_DB", "flask")

        return _connect_pg(
            user=user,
            password=password,
            host=host,
            port=int(port),
            database=database,
            **kwargs,
        )
    except Exception as e:
        raise Exception(f"Error connecting to PostgreSQL: {e}")


def engine_postgres(pool_size=None, max_overflow=None, **kwargs):
    try:
        user = os.getenv("POSTGRES_USER", "postgres")
        password = os.getenv("POSTGRES_PASSWORD", "postgres")
        host = os.getenv("POSTGRES_HOST", "postgres")
        port = os.getenv("POSTGRES_PORT", 5432)
        database = os.getenv("POSTGRES_DB", "flask")

        # configure this and others .env args as needed
        if not pool_size:
            pool_size = os.getenv("POSTGRES_POOL_SIZE", 5)
        if not max_overflow:
            max_overflow = os.getenv("POSTGRES_MAX_OVERFLOW", 10)

        url = f"postgresql+psycopg://{user}:{password}@{host}:{port}/{database}"

        return create_engine(
            url, pool_size=pool_size, max_overflow=max_overflow, **kwargs
        )
    except Exception as e:
        raise Exception(f"Error while creating PG engine: {e}")
