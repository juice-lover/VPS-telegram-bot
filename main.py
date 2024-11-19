import asyncio
import logging
from dotenv import load_dotenv
import os
import sys

import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from modules import functions

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


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())