import asyncio
import logging
from dotenv import load_dotenv
import os
import sys

import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command, CommandObject
from aiogram.types import LabeledPrice, PreCheckoutQuery
from aiogram.exceptions import TelegramBadRequest

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


@dp.pre_checkout_query()
async def on_pre_checkout_query(
    pre_checkout_query: PreCheckoutQuery,
):
    await pre_checkout_query.answer(ok=True)


@dp.message(F.successful_payment)
async def on_successful_payment(message: types.Message):
    telegram_id = message.from_user.id  # telegram id аккаунта
    sticker_key = "CAACAgIAAxkBAAENLipnPhlg7fcgRxM-LtHZx4ue-puabgACAQcAAkb7rASX2-SMiGVeMDYE"
    await bot.send_sticker(chat_id=telegram_id, sticker=sticker_key)
    await message.answer(f"Спасибо за покупку!\n\n"
                         f"Ваш хеш транзакции: {message.successful_payment.telegram_payment_charge_id}\n\n"
                         f"Пожалуйста, сохраните хеш транзакции. Он понадобится в случае возврата средств.\n\n"
                         f"Приятного использования нашего бота!",
                         message_effect_id="5104841245755180586")


@dp.message(Command("refund"))
async def cmd_refund(message: types.Message, command: CommandObject):
    transaction_id = command.args
    if transaction_id is None:
        await message.answer(
            "тут как правильно ввести комманду"
        )
        return

    try:
        telegram_id = message.from_user.id  # telegram id аккаунта

        await bot.refund_star_payment(user_id=telegram_id, telegram_payment_charge_id=transaction_id)
        await message.answer("Возврат произведён успешно. Потраченные звёзды уже вернулись на ваш счёт в Telegram.", message_effect_id="5104841245755180586")

    except TelegramBadRequest as error:

        if "CHARGE_NOT_FOUND" in error.message:
            text = "Такой код покупки не найден. Пожалуйста, проверьте вводимые данные и повторите ещё раз."
        elif "CHARGE_ALREADY_REFUNDED" in error.message:
            text = "За эту покупку уже ранее был произведён возврат средств."
        else:
            # При всех остальных ошибках – такой же текст,
            # как и в первом случае
            text = "Такой код покупки не найден. Пожалуйста, проверьте вводимые данные и повторите ещё раз."

        await message.answer(text)
        return


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())