from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from bot.keyboards.main_menu import main_menu_keyboard

router = Router(name="common")


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(
        "Здравствуйте! Я виртуальный помощник стоматологической клиники Implantum. "
        "Чем могу помочь?",
        reply_markup=main_menu_keyboard(),
    )


@router.message(Command("help"))
@router.message(F.text == "ℹ️ Помощь")
async def help_handler(message: Message) -> None:
    await message.answer(
        "Я помогу записаться на приём и узнать информацию о клинике. "
        "Выберите нужный пункт в меню."
    )

