from sqlalchemy import Connection, inspect, text
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

import bot.database.models  # noqa: F401  # регистрирует модели в metadata
from bot.database.base import Base

_engine: AsyncEngine | None = None
session_factory: async_sessionmaker[AsyncSession] | None = None


def _ensure_patient_columns(connection: Connection) -> None:
    columns = {column["name"] for column in inspect(connection).get_columns("patients")}
    for name, data_type in {"language": "VARCHAR(2)", "branch": "VARCHAR(32)"}.items():
        if name not in columns:
            connection.execute(text(f"ALTER TABLE patients ADD COLUMN {name} {data_type}"))


async def init_database(database_url: str) -> None:
    global _engine, session_factory
    _engine = create_async_engine(database_url)
    session_factory = async_sessionmaker(_engine, expire_on_commit=False)

    # Подходит для начальной разработки; позже заменим на миграции Alembic.
    async with _engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
        await connection.run_sync(_ensure_patient_columns)


async def close_database() -> None:
    global _engine, session_factory
    if _engine is not None:
        await _engine.dispose()
        _engine = None
        session_factory = None
