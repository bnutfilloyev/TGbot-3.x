from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def remove_kb():
    return ReplyKeyboardRemove()


def contact_kb():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📞 Telefon raqamni yuborish", request_contact=True)],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Telefon raqamingizni kiriting yoki tugmani bosing",
    )
    return keyboard


def main_menu_kb():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📍 Manzillarimiz"),
                KeyboardButton(text="📞 Aloqa"),
            ],
            [
                KeyboardButton(text="📝 Fikr bildirish"),
            ]
        ],
        resize_keyboard=True,
        input_field_placeholder=None,
    )
    return keyboard
