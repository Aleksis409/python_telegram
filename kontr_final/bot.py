# задача 4
# !pip install aiogram==2.25.1
# bot_url = http://t.me/RoboCarTestBot

# pip install openai==0.28

# импорт библиотек
import aiogram
import logging
import asyncio
import openai
import copy
import base64

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware 

# импорт телеграм токена из файла config.py
from config_bot import TELEGRAM_TOKEN

# Максимальная длина сообщения
max_context_length = 500

# Максимальное количество использованных токенов
max_token_usage = 500

# импорт телеграм токена из файла config.py
from config_bot import API_KEY

openai.api_key = base64.b64decode(API_KEY).decode()
model = "gpt-3.5-turbo"

chat_history = {}
init_bot_role = [{"role": "system", "content": "Ты поэт, зарифмуй, преобразуй и верни сообщения пользователя как стих. Сохраняй смысл сообщения. Не превышай объем сообщения"}]


#  bot.py - запуск телеграм бота,  polly_bot_handlers.py - инициализация телеграм бота    
def get_bot_response(user_id: int, telegram_prompt: str) -> tuple[str, int]: 
    """ метод возвращает ответ чата GPT и общее кол-во токенов, которые были использованы моделью для обработки запроса"""
    
    global chat_history
    global init_bot_role
    
    # проверка - новый user или нет
    if user_id not in chat_history:                             
        chat_history[user_id] = copy.deepcopy(init_bot_role)
    
    chat_history[user_id].append({"role": "user", "content": telegram_prompt})
    response = openai.ChatCompletion.create(
        model = model,
        messages = chat_history[user_id],
        temperature = 0.5
    )
    bot_response = response['choices'][0]['message']['content']
    total_tokens = response['usage']['total_tokens'] 

    chat_history[user_id].append({"role": "assistant", "content": bot_response})

    print(f"You: {telegram_prompt}")
    print(f"Bot: {bot_response}")
    # print(f"chat_history: {chat_history}")
    
    return bot_response, total_tokens
  
    
def clear_chat_histoty(user_id: int) -> None:
    """Очистка истории чата для конкретного пользователя"""
    global chat_history
    global init_bot_role
    chat_history[user_id] = copy.deepcopy(init_bot_role)


# Загрузка данных из файла users.csv, если он существует, иначе создание нового DataFrame
import pandas as pd
try:
    users_df = pd.read_csv('users.csv')
except FileNotFoundError:
    users_df = pd.DataFrame(columns=['user_id', 'tokens', 'context', 'token_capacity', 'context_capacity'])
    users_df.to_csv('users.csv', index=False)


# Функция регистрации пользователя
def user_reg(user_id):
    global users_df
     # Добавляем нового пользователя
    new_user_df = pd.DataFrame({'user_id': [user_id], 'tokens': [0], 'context': [''], 'token_capacity': [max_token_usage], 'context_capacity': [max_context_length]})
    users_df = pd.concat([users_df, new_user_df], ignore_index=True)


# Функция обновления информации о пользователе
def update_user_info(user_id, tokens=0, context=''):
    """ Функция обновления информации о пользователе"""
    # Обновляем информацию о пользователе
    idx = users_df.index[users_df['user_id'] == user_id].tolist()[0]  # получаем индекс строки пользователя user_id
    users_df.at[idx, 'tokens'] += tokens
    users_df.at[idx, 'context'] += context     
    

# Функция сохранения данных в файл users.csv
def save_user_data():
    """ Функция сохранения данных в файл users.csv """
    global users_df
    users_df.to_csv('users.csv', index=False)


def limit_checking(user_id, context_length):
    """ Функция проверки превышения лимита токенов и лимита контекста сообщения"""
    global users_df
    idx = users_df.index[users_df['user_id'] == user_id].tolist()[0]          # получаем индекс строки пользователя user_id
    full_context_length = len(users_df.at[idx, 'context']) + context_length   # вычисляем полную длину контекста 
    tokens = users_df.at[idx, 'tokens']

    if  tokens > users_df.at[idx, 'token_capacity']:                          # проверяем кол-во токенов 
        print(f'tokens = {tokens}')
        answer = "У вас закончились токены!"                                  # превышен лимит токенов
    
    elif full_context_length > users_df.at[idx, 'context_capacity']:          # проверяем контекст
        print(f'context_length = {full_context_length}')
        answer = "Превышен лимит длины контекста! Произведите очистку"        # превышен лимит длины контекста
    else: return None
    return answer


def get_tokens(user_id):
    """Функция обнуления счетчика токенов"""
    idx = users_df.index[users_df['user_id'] == user_id].tolist()[0]          # получаем индекс строки пользователя user_id
    users_df.at[idx, 'tokens'] = 0   


def clean_context(user_id):
    """Функция чистки контекста беседы"""
    idx = users_df.index[users_df['user_id'] == user_id].tolist()[0]          # получаем индекс строки пользователя user_id
    users_df.at[idx, 'context'] = ""    


# инициализация бота
bot=Bot(token = base64.b64decode(TELEGRAM_TOKEN).decode())  
dp=Dispatcher(bot)


# Обработчик команды /tokens
@dp.message_handler(commands=['tokens'])
async def clean_tokens(message: types.Message):
    user_id = message.from_user.id                                             # получаем id пользователя

    if user_id in users_df['user_id'].values:                                  # пользователь зарегистрирован
        get_tokens(user_id)                                                    # обнуление счетчика токенов          
        bot_answer = ("Счетчик  токенов обнулен")        
    else:
        bot_answer = ("Необходимо зарегистрироваться!")                        # пользователь не зарегистрирован
    await message.answer(bot_answer)


# задача 4 
# Обработчик команды /clean
@dp.message_handler(commands=['clean'])
async def context_clean(message: types.Message):
    user_id = message.from_user.id                                             # получаем id пользователя

    if user_id in users_df['user_id'].values:                                  # пользователь зарегистрирован
        clean_context(user_id)                                                 # очистка контекста беседы    
        clear_chat_histoty(user_id)                                            # очистка истории чата GPT 
        bot_answer = ("Контекст беседы очищен!!!") 
             
    else:
        bot_answer = ("Необходимо зарегистрироваться!")                        # пользователь не зарегистрирован
    await message.answer(bot_answer)


# задача 2 - добавляется обработчик команды /start и регистрация пользователя
# Обработчик команды /start, регистрация пользователя
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id                                             # получаем id пользователя
    
    if user_id in users_df['user_id'].values:
        bot_answer = (f"И снова здравствуйте, {message.from_user.username}!")  # уже зарегистрирован    
    else:
        user_reg(user_id)                                                      # регистрация пользователя
        bot_answer = (f"Привет, {message.from_user.username}!")                # новый пользователь            
    await message.answer(bot_answer)


# Обработчик сообщений    
@dp.message_handler()
async def respond (message:types.Message):
    user_id = message.from_user.id                                             # получаем id пользователя  

    if user_id in users_df['user_id'].values:                                  # пользователь зарегистрирован
        checking_result = limit_checking(user_id, len(message.text))  
        if checking_result is None:                                            # проверка лимита токенов и лимита контекста сообщения 
            bot_response, tokens = get_bot_response(user_id, message.text)     # Получаем текущий chat_history пользователя
            context = f" You: {message.text} Bot: {bot_response}"              # Добавляем текущий контекст к существующему
            update_user_info(user_id, tokens, context)                         # Обновляем информацию о пользователе
            save_user_data()                                                   # сохраняем данные в базу                   

            await message.answer(bot_response)                                 # возвращаем ответ Chat GPT
        else:
            await message.answer(checking_result)

    else:                                                                      # пользователь не зарегистрирован
        await message.answer("Необходимо зарегистрироваться!") 

    
        print(f"users_df = ${users_df}")


if __name__ == "__main__":
    from aiogram import executor 

    #Запуск бота 
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, loop=loop, skip_updates=True)
















