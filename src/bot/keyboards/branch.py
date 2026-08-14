from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.i18n import Branch, Language, branch_name


def branch_keyboard(language: Language) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=branch_name(branch, language),
                    callback_data=f"branch:{branch.value}",
                )
            ]
            for branch in Branch
        ]
    )
