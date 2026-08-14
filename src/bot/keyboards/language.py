from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.i18n import LANGUAGE_NAMES, Language


def language_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=LANGUAGE_NAMES[language], callback_data=f"language:{language.value}"
                )
            ]
            for language in Language
        ]
    )
