from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from bot.i18n import Language, t


def main_menu_keyboard(language: Language = Language.RU) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=t("appointment", language))],
            [KeyboardButton(text=t("help_button", language))],
            [KeyboardButton(text=t("change_branch", language))],
            [KeyboardButton(text=t("change_language", language))],
        ],
        resize_keyboard=True,
        input_field_placeholder=t("menu_placeholder", language),
    )
