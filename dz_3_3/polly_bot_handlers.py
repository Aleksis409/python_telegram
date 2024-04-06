import aiogram
import logging
import base64

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware 

# импорт телеграм токена из файла config.py
from config import TELEGRAM_TOKEN
from gpt_handlers import get_bot_response
from gpt_handlers import clear_chat_histoty

# Максимальная длина сообщения
max_context_length = 500

# Максимальное количество использованных токенов
max_token_usage = 500


# Загрузка данных из файла users.csv, если он существует, иначе создание нового DataFrame
import pandas as pd
try:
    users_df = pd.read_csv('users.csv')
except FileNotFoundError:
    users_df = pd.DataFrame(columns=['user_id', 'tokens', 'context', 'token_capacity', 'context_capacity'])
    ## регистрация тестового пользователя
    # new_user_df = pd.DataFrame({'user_id': [1111], 'tokens': [1], 'context': ["AAA"]})
    # users_df = pd.concat([users_df, new_user_df], ignore_index=True)
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
    # print(f"tokens = {users_df.at[idx, 'tokens']}")  
    # print(f"context_len = {len(users_df.at[idx, 'context'])}")
    

# Функция сохранения данных в файл users.csv
def save_user_data():
    """ Функция сохранения данных в файл users.csv """
    global users_df
    users_df.to_csv('users.csv', index=False)


# задача 3
def limit_checking(user_id, context_length):
    """ Функция проверки превышения лимита токенов и лимита контекста сообщения"""
    global users_df
    idx = users_df.index[users_df['user_id'] == user_id].tolist()[0]          # получаем индекс строки пользователя user_id
    full_context_length = len(users_df.at[idx, 'context']) + context_length   # вычисляем полную длину контекста 
    tokens = users_df.at[idx, 'tokens']

    if  tokens > users_df.at[idx, 'token_capacity']:                          # проверяем кол-во токенов 
        print(f'tokens = {tokens}')
        answer = "Аррр, у вас закончились токены!"                            # превышен лимит токенов
    
    elif full_context_length > users_df.at[idx, 'context_capacity']:          # проверяем контекст
        print(f'context_length = {full_context_length}')
        answer = "Аррр, мы слишком разговорились... Дайте передохнуть!"       # превышен лимит длины контекста
    else: return None

    return answer


# задача 4
def get_tokens(user_id):
    """Функция обнуления счетчика токенов"""
    idx = users_df.index[users_df['user_id'] == user_id].tolist()[0]          # получаем индекс строки пользователя user_id
    users_df.at[idx, 'tokens'] = 0   


# задача 4
def clean_context(user_id):
    """Функция чистки контекста беседы"""
    idx = users_df.index[users_df['user_id'] == user_id].tolist()[0]          # получаем индекс строки пользователя user_id
    users_df.at[idx, 'context'] = ""    


# инициализация бота
bot=Bot(token = base64.b64decode(TELEGRAM_TOKEN).decode())  
dp=Dispatcher(bot)


# задача 4 
# Обработчик команды /tokens
@dp.message_handler(commands=['tokens'])
async def clean_tokens(message: types.Message):
    user_id = message.from_user.id                                                  # получаем id пользователя

    if user_id in users_df['user_id'].values:                                       # пользователь зарегистрирован
        get_tokens(user_id)                                                         # обнуление счетчика токенов          
        bot_answer = ("Аррр, так то лучше. Теперь мы можем продолжить говорить!!!")        
    else:
        bot_answer = ("Аррр. Нужно сначала зарегистрироваться!")                    # пользователь не зарегистрирован
    await message.answer(bot_answer)


# задача 4 
# Обработчик команды /clean
@dp.message_handler(commands=['clean'])
async def context_clean(message: types.Message):
    user_id = message.from_user.id                                                  # получаем id пользователя

    if user_id in users_df['user_id'].values:                                       # пользователь зарегистрирован
        clean_context(user_id)                                                      # очистка контекста беседы    
        clear_chat_histoty(user_id)                                                 # очистка истории чата GPT 
        bot_answer = ("Аррр, все забыл, но решительно готов продолжать беседу!!!") 
             
    else:
        bot_answer = ("Аррр. Нужно сначала зарегистрироваться!")                    # пользователь не зарегистрирован
    await message.answer(bot_answer)


# задача 2 - добавляется обработчик команды /start и регистрация пользователя
# Обработчик команды /start, регистрация пользователя
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id                                           # получаем id пользователя
    
    if user_id in users_df['user_id'].values:
        bot_answer = (f"И снова здравствуй, {message.from_user.username}!")  # уже зарегистрирован    
    else:
        user_reg(user_id)                                                    # регистрация пользователя
        bot_answer = (f"Привет, {message.from_user.username}!")              # новый пользователь            
    await message.answer(bot_answer)


# Обработчик сообщений    
@dp.message_handler()
async def respond (message:types.Message):
    user_id = message.from_user.id                                          # получаем id пользователя  

    if user_id in users_df['user_id'].values:                               # пользователь зарегистрирован
        checking_result = limit_checking(user_id, len(message.text))  
        if checking_result is None:                                         # проверка лимита токенов и лимита контекста сообщения 
            bot_response, tokens = get_bot_response(user_id, message.text)  # Получаем текущий chat_history пользователя
            context = f" You: {message.text} Bot: {bot_response}"           # Добавляем текущий контекст к существующему
            update_user_info(user_id, tokens, context)                      # Обновляем информацию о пользователе
            save_user_data()                                                # сохраняем данные в базу                   

            await message.answer(bot_response)                              # возвращаем ответ Chat GPT
        else:
            await message.answer(checking_result)

    else:                                                                   # пользователь не зарегистрирован
        await message.answer("Аррр. Нужно сначала зарегистрироваться!") 

    
        print(f"users_df = ${users_df}")
