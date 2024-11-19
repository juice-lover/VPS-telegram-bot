# делаем нужные импорты
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