from pathlib import Path

from sqlalchemy import text

from bot.database import session as database_session
from bot.database.patients import get_branch, get_language, set_branch, set_language
from bot.i18n import Branch, Language


async def test_language_is_saved_and_loaded(tmp_path: Path) -> None:
    database_url = f"sqlite+aiosqlite:///{tmp_path / 'patients.db'}"
    await database_session.init_database(database_url)
    try:
        await set_language(123, Language.EN)
        assert await get_language(123) == Language.EN

        await set_language(123, Language.HY)
        assert await get_language(123) == Language.HY

        await set_branch(123, Branch.SECOND)
        assert await get_branch(123) == Branch.SECOND
    finally:
        await database_session.close_database()


async def test_existing_database_gets_language_column(tmp_path: Path) -> None:
    database_url = f"sqlite+aiosqlite:///{tmp_path / 'legacy.db'}"
    await database_session.init_database(database_url)
    assert database_session._engine is not None
    async with database_session._engine.begin() as connection:
        await connection.execute(text("ALTER TABLE patients DROP COLUMN language"))
    await database_session.close_database()

    await database_session.init_database(database_url)
    try:
        await set_language(456, Language.EN)
        assert await get_language(456) == Language.EN
    finally:
        await database_session.close_database()
