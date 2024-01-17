from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def tel_raq() -> types.ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text="Telefon raqamingizni",
                   request_contact=True
                   )
    return builder.as_markup(resize_keyboard=True)