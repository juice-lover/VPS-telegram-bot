import asyncio
import logging
from dotenv import load_dotenv
import os
import sys

import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command, CommandObject
from aiogram.types import LabeledPrice

from modules import functions, keyboard

load_dotenv()


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token=os.getenv("BOT_TOKEN"))

# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user_name = message.from_user.first_name # имя аккаунта telegram
    telegram_id = message.from_user.id # telegram id аккаунта

    # вызываем нашу функцию ответственную за логику
    await functions.start_function(message, bot, user_name, telegram_id)


@dp.message(F.text == "Инструменты")
async def tools_btn(message: types.Message):
    keyboard_btn = await keyboard.create_tools_btn_menu()  # Ожидаем результат асинхронной функции
    await message.answer("Выберите инструмент:", reply_markup=keyboard_btn)


@dp.message(F.text == "Кабинет")
async def cabinet_btn(message: types.Message):
    telegram_id = message.from_user.id  # telegram id аккаунта
    # вызываем нашу функцию ответственную за логику
    await functions.cabinet_function(message, bot, telegram_id)


@dp.message(Command("stars_10"))
@dp.message(Command("stars_50"))
@dp.message(Command("stars_100"))
async def stars_pay_command(message: types.Message, command: CommandObject):

    # Словарь с ценами в звёздах для каждой команды
    star_prices = {
        10: 15,  # 10 кредитов = 15 звёзд
        50: 70,  # 50 кредитов = 70 звёзд
        100: 150,  # 100 кредитов = 150 звёзд
    }

    # Вытаскиваем число из текста команды
    amount = int(command.command.split("_")[1])

    # Получаем цену из словаря
    if amount in star_prices:
        price = star_prices[amount]
    else:
        await message.answer("Цена для этой команды не найдена.")
        return

    # Для платежей в Telegram Stars список цен
    prices = [LabeledPrice(label="XTR", amount=price)]  # Цена в копейках

    # Отправка инвойса
    await message.answer_invoice(
        title=f"Пополнение баланса на {amount} кредитов",
        description=f"Будет пополнено: {amount} кредитов\n"
                    f"Назначение: Покупка кредитов в боте",
        prices=prices,
        provider_token="",  # Поставь свой токен провайдера, если он есть
        payload=f"{amount}_stars",  # Payload может содержать информацию, которую ты хочешь передать
        currency="XTR"
    )



async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())