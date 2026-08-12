from aiogram import F, Router
from aiogram.types import Message

router = Router(name="appointment")


@router.message(F.text == "🦷 Записаться на приём")
async def appointment_handler(message: Message) -> None:
    await message.answer(
        "Сценарий записи на приём скоро будет доступен. "
        "Здесь мы добавим выбор услуги, врача, даты и времени."
    )

