# "Aiogram" - это фреймворк для создания ботов Telegram
# "logging" - это стандартный модуль Python, используемый для регистрации сообщений в приложении
import aiogram
import logging
import base64

# импортируем модуль для работы с регулярными выражениями (Regular Expressions). 
import re

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware 

# импорт телеграм токена из файла config.py
from config import TELEGRAM_TOKEN

# инициализация бота
bot=Bot(token = base64.b64decode(TELEGRAM_TOKEN).decode())  
dp=Dispatcher(bot)

# # *************** задача 2 **************
# @dp.message_handler()
# async def start (message:types.Message):
#     await message.answer("\"" + message.text + "\" - that’s what she said.")


# # *************** задача 3 **************
# @dp.message_handler()
# async def start (message:types.Message):
#     print(message.from_user)
#     await message.answer(message.text + ", " + message.from_user.username + "! You're language_code is " + message.from_user.language_code)


# # *************** задача 4 **************
# # вариант, если сообщение содержит Hi или Hello, или What’s up
#
# @dp.message_handler(regexp=re.compile(r'\b(Hi|Hello|What’s up)\b', re.IGNORECASE))  
# async def say_hi(message:types.Message):
#     await message.answer("Hey, " + message.from_user.username + "!")

# @dp.message_handler()
# async def start (message:types.Message):
#     await message.answer("You said: " + message.text)


# # *************** задача 4 ************** 
# # вариант, если сообщение состоит только из Hi или Hello, или What’s up
#
# # Компилируем паттерн
# pattern = re.compile(r'\b(Hi|Hello|What’s up)\b', re.IGNORECASE)
#
# @dp.message_handler()  
# async def say_hi(message:types.Message):
#     # проверяем на соответствие паттерну
#     if pattern.fullmatch(message.text):
#         await message.answer("Hey, " + message.from_user.username + "!")
#     else:
#         await message.answer("You said: " + message.text)


# # *************** задача 5 **************
# Паттерн для поиска чисел и операторов ("+", "-", "/", "*") с пробелами или без между ними
# '\s*' - соответствует нулю или более пробелам,  '\d+' - соответствует одной или более цифрам
pattern = re.compile(r'\s*(\d+)\s*([+-/*])\s*(\d+)\s*')

@dp.message_handler()  
async def calc(message:types.Message):
    # Инициализируем переменную result
    result = None
    # проверяем на соответствие паттерну    
    if pattern.fullmatch(message.text):
        matches = pattern.findall(message.text)
        # Перебираем найденные соответствия
        for match in matches:
            num1 = int(match[0])  # Первое число
            operator = match[1]   # Оператор
            num2 = int(match[2])  # Второе число
            
            # Выполняем математическую операцию
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    await message.answer("Ошибка: деление на ноль")
                    return
                result = num1 / num2
        await message.answer(message.text + " = " + str(result))
    else:
        await message.answer("Введите математическое выражение из двух целых чисел и операции +, -, *, / - между ними")
