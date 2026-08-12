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


async def init_database(database_url: str) -> None:
    global _engine, session_factory
    _engine = create_async_engine(database_url)
    session_factory = async_sessionmaker(_engine, expire_on_commit=False)

    # Подходит для начальной разработки; позже заменим на миграции Alembic.
    async with _engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


async def close_database() -> None:
    global _engine
    if _engine is not None:
        await _engine.dispose()
        _engine = None
