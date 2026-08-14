from aiogram import F, Router
from aiogram.types import Message

from bot.database.patients import get_language
from bot.i18n import Language, t

router = Router(name="appointment")


@router.message(F.text.in_([t("appointment", language) for language in Language]))
async def appointment_handler(message: Message) -> None:
    if message.from_user is None:
        return
    language = await get_language(message.from_user.id) or Language.RU
    await message.answer(t("appointment_soon", language))
