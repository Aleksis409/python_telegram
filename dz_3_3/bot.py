# !pip install aiogram==2.25.1
# bot_url = http://t.me/RoboCarTestBot

# pip install openai==0.28

# импорт библиотек
import aiogram
import logging
import asyncio

if __name__ == "__main__":
    from aiogram import executor 
    from polly_bot_handlers import dp

    #Запуск бота 
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, loop=loop, skip_updates=True)
















