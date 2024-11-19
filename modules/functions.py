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
