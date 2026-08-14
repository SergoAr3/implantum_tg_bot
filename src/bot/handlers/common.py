from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message

from bot.database.patients import get_branch, get_language, set_branch, set_language
from bot.i18n import Branch, Language, branch_name, t
from bot.keyboards.branch import branch_keyboard
from bot.keyboards.language import language_keyboard
from bot.keyboards.main_menu import main_menu_keyboard

router = Router(name="common")


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    if message.from_user is None:
        return
    language = await get_language(message.from_user.id)
    if language is None:
        await message.answer(
            t("welcome_choose_language", Language.RU),
            reply_markup=language_keyboard(),
        )
        return
    if await get_branch(message.from_user.id) is None:
        await message.answer(t("choose_branch", language), reply_markup=branch_keyboard(language))
        return
    await message.answer(t("greeting", language), reply_markup=main_menu_keyboard(language))


@router.callback_query(F.data.startswith("language:"))
async def language_callback(callback: CallbackQuery) -> None:
    callback_message = callback.message
    if callback.data is None or not isinstance(callback_message, Message):
        await callback.answer()
        return
    language = Language(callback.data.split(":", 1)[1])
    is_first_language_selection = await get_language(callback.from_user.id) is None
    await set_language(callback.from_user.id, language)
    await callback_message.edit_reply_markup(reply_markup=None)
    if is_first_language_selection:
        await callback_message.answer(
            t("choose_branch", language),
            reply_markup=branch_keyboard(language),
        )
    else:
        await callback_message.answer(
            t("language_changed_greeting", language),
            reply_markup=main_menu_keyboard(language),
        )
    await callback.answer()


@router.callback_query(F.data.startswith("branch:"))
async def branch_callback(callback: CallbackQuery) -> None:
    callback_message = callback.message
    if callback.data is None or not isinstance(callback_message, Message):
        await callback.answer()
        return
    branch = Branch(callback.data.split(":", 1)[1])
    language = await get_language(callback.from_user.id) or Language.RU
    await set_branch(callback.from_user.id, branch)
    await callback_message.edit_reply_markup(reply_markup=None)
    await callback_message.answer(
        t("branch_selected", language).format(branch=branch_name(branch, language)),
        reply_markup=main_menu_keyboard(language),
    )
    await callback.answer()


@router.message(F.text.in_([t("change_language", language) for language in Language]))
async def change_language_handler(message: Message) -> None:
    if message.from_user is None:
        return
    current_language = await get_language(message.from_user.id) or Language.RU
    await message.answer(
        t("choose_language", current_language),
        reply_markup=language_keyboard(),
    )


@router.message(F.text.in_([t("change_branch", language) for language in Language]))
async def change_branch_handler(message: Message) -> None:
    if message.from_user is None:
        return
    language = await get_language(message.from_user.id) or Language.RU
    await message.answer(t("choose_branch", language), reply_markup=branch_keyboard(language))


@router.message(Command("help"))
@router.message(F.text.in_([t("help_button", language) for language in Language]))
async def help_handler(message: Message) -> None:
    if message.from_user is None:
        return
    language = await get_language(message.from_user.id) or Language.RU
    await message.answer(t("help", language))
