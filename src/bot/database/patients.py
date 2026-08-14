from sqlalchemy import select

from bot.database import session as database_session
from bot.database.models import Patient
from bot.i18n import Branch, Language


async def get_language(telegram_id: int) -> Language | None:
    if database_session.session_factory is None:
        return None
    async with database_session.session_factory() as session:
        patient = await session.scalar(select(Patient).where(Patient.telegram_id == telegram_id))
        if patient is None or patient.language is None:
            return None
        try:
            return Language(patient.language)
        except ValueError:
            return None


async def set_language(telegram_id: int, language: Language) -> None:
    if database_session.session_factory is None:
        return
    async with database_session.session_factory() as session:
        patient = await session.scalar(select(Patient).where(Patient.telegram_id == telegram_id))
        if patient is None:
            patient = Patient(telegram_id=telegram_id, language=language.value)
            session.add(patient)
        else:
            patient.language = language.value
        await session.commit()


async def get_branch(telegram_id: int) -> Branch | None:
    if database_session.session_factory is None:
        return None
    async with database_session.session_factory() as session:
        patient = await session.scalar(select(Patient).where(Patient.telegram_id == telegram_id))
        if patient is None or patient.branch is None:
            return None
        try:
            return Branch(patient.branch)
        except ValueError:
            return None


async def set_branch(telegram_id: int, branch: Branch) -> None:
    if database_session.session_factory is None:
        return
    async with database_session.session_factory() as session:
        patient = await session.scalar(select(Patient).where(Patient.telegram_id == telegram_id))
        if patient is None:
            patient = Patient(telegram_id=telegram_id, branch=branch.value)
            session.add(patient)
        else:
            patient.branch = branch.value
        await session.commit()
