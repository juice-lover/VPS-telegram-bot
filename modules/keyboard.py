# делаем нужные импорты
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import (
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


# создаем клавиатуру для пользователя
kb_menu = [
    [
        KeyboardButton(text="Инструменты"),
        KeyboardButton(text="Кабинет")
    ],
    [
        KeyboardButton(text="Информация")
    ]
]

keyboard_menu = ReplyKeyboardMarkup(
    keyboard=kb_menu,
    resize_keyboard=True,
    input_field_placeholder="Выберите нужный вам раздел бота:"
)


async def create_tools_btn_menu():
    buttons = [
        [
            InlineKeyboardButton(text="Сделать уникальной", callback_data="uniqueness") # запятая
            #InlineKeyboardButton(text="Удалить фон", callback_data="remove_background"),
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard

