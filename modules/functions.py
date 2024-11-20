from modules import keyboard


async def start_function(message, bot, user_name, telegram_id):

    # отправляем приветственный стикер
    sticker_key = "CAACAgIAAxkBAAENLBJnPJn0v1C0yIDI1j7_gxtNzVy_QgACBAcAAkb7rARD2NYo4qk9gzYE"
    await bot.send_sticker(telegram_id, sticker_key)

    # текст, который будет отправлен пользователю
    send_message_text = (f"👋 {user_name} Привет! Рад видеть тебя!\n\n"
                         f"Этот бот поможет сделать твоё фото лучше:\n\n"
                         f"📈 Улучшает качество изображений.\n\n"
                         f"✨ Убирает лишний фон и делает фото уникальным для соцсетей.\n\n"
                         f"🔧 Предлагает другие полезные функции для работы с изображениями.\n\n"
                         f"Если будут вопросы, всегда можно заглянуть в раздел помощи!")


    await message.answer(send_message_text, reply_markup=keyboard.keyboard_menu)


async def cabinet_function(message, bot, telegram_id):

    # отправляем стикер
    sticker_key = "CAACAgIAAxkBAAENLg1nPgnFVwt83aRc80_3NdjzyiB0FAAC7QYAAkb7rASusnq3cIRG2zYE"
    await bot.send_sticker(chat_id=telegram_id, sticker=sticker_key)

    # текст, который будет отправлен пользователю
    send_message_text = (f"Ваш кабинет\n\n"
                         f"Telegram ID: {telegram_id}\n"
                         f"Баланс кредитов: *\n\n"
                         f"Пополнить с помощью звёзд:\n\n"
                         f"10 кредитов на баланс\n"
                         f"Команда: /stars_10\n"
                         f"Цена: 15 звёзд\n\n"
                         f"50 кредитов на баланс\n"
                         f"Команда: /stars_50\n"
                         f"Цена: 70 звёзд\n\n"
                         f"100 кредитов на баланс\n"
                         f"Команда: /stars_100\n"
                         f"Цена: 150 звёзд\n\n"
                         f"Другие способы оплаты:")

    await message.answer(send_message_text)