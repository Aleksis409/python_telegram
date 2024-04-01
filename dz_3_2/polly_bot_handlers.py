# "Aiogram" - это фреймворк для создания ботов Telegram
# "logging" - это стандартный модуль Python, используемый для регистрации сообщений в приложении

# # *********** Задача 3 ***********
# import aiogram
# import logging
# import base64

# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.contrib.middlewares.logging import LoggingMiddleware 

# # импорт телеграм токена из файла config.py
# from config import TELEGRAM_TOKEN
# from gpt_handlers import get_bot_response

# # инициализация бота
# bot=Bot(token = base64.b64decode(TELEGRAM_TOKEN).decode())  
# dp=Dispatcher(bot)

# @dp.message_handler()
# async def start (message:types.Message):
#     bot_response = get_bot_response(message.text)
#     await message.answer(bot_response)


# *********** Задача 4 ***********
import aiogram
import logging
import base64

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware 

# импорт телеграм токена из файла config.py
from config import TELEGRAM_TOKEN
from gpt_handlers import get_bot_response

# Словарь для хранения контекста для каждого пользователя
user_context = {}

# инициализация бота
bot=Bot(token = base64.b64decode(TELEGRAM_TOKEN).decode())  
dp=Dispatcher(bot)

@dp.message_handler()
async def start (message:types.Message):
    # id нового пользователя
    user_id = message.from_user.id

    if user_id not in user_context:
        # Создание контекста для нового пользователя
        user_context[user_id] = []

    # Получаем текущий chat_history пользователя
    chat_history = get_bot_response(message.text)

    # Обновление chat_history пользователя
    user_context[user_id] = chat_history

    # Перебираем элементы истории чата в обратном порядке чтобы найти последний ответ бота
    for mess in reversed(chat_history):
        # Проверяем, является ли роль сообщения "assistant" (помощником)
        if mess["role"] == "assistant":
            # Получаем текст ответа
            bot_response = mess["content"]
            # Выходим из цикла, так как мы нашли последний ответ бота
            break

    # print(f"user_context = {user_context}")
    await message.answer(bot_response)

