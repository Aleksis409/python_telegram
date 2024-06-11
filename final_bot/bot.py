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
from time import time

# Максимальная длина сообщения
max_context_length = 2000
# Максимальное количество использованных токенов
max_token_usage = 2000

# импорт телеграм токена из файла config.py
from config_bot import TELEGRAM_TOKEN

# импорт телеграм токена из файла config.py
from config_bot import API_KEY

openai.api_key = base64.b64decode(API_KEY).decode()
model = "gpt-3.5-turbo"
chat_history = {}                                                                     # история диалога с ChatGPT
init_bot_role = [{"role": "system", "content": "Ты интелелектуальный помощник."}]     # роль для ChatGPT
logging.info(f'init_bot_role = : {init_bot_role}')                                    # добавляем в лог info


# настройка логирования
# настройка основных параметров журнала логов
logging.basicConfig(level=logging.INFO,             
                    filename='my_bot.log',
                    encoding='utf-8',
                    filemode="w", 
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")

logging.getLogger('aiogram').setLevel(logging.ERROR) # логирование aiogram только ошибок


# получение и обработка ответ чата GPT
def get_bot_response(user_id: int, telegram_prompt: str) -> tuple[str, int]: 
    """ метод возвращает ответ чата GPT и общее кол-во токенов, которые были использованы моделью для обработки запроса"""
    global chat_history
    global init_bot_role
    
    # проверка - новый user или нет
    if user_id not in chat_history:                             
        chat_history[user_id] = copy.deepcopy(init_bot_role)
    
    chat_history[user_id].append({"role": "user", "content": telegram_prompt})        # добавляем запрос пользователя user_id из telegram в историю чата 
    try:
        response = openai.ChatCompletion.create(
            model = model,
            messages = chat_history[user_id],
            temperature = 0.5
        )          
        bot_response = response['choices'][0]['message']['content']                   # формируем ответ чата GPT
        total_tokens = response['usage']['total_tokens']                              # кол-во токенов
        chat_history[user_id].append({"role": "assistant", "content": bot_response})  # добавляем ответ чата GPT в историю чата для пользователя user_id
        print(f"You: {telegram_prompt}")                                              # печать диалога в консоль
        print(f"Bot: {bot_response}")                                                 # печать диалога в консоль
        logging.info(f'Bot for {user_id}: {bot_response}')                            # добавляем в лог info
        logging.info(f'tokens user {user_id}: {total_tokens}')                        # добавляем в лог info        
        return bot_response, total_tokens
    
    except Exception:
        logging.error('Сервер openAPI не доступен')                                   # добавляем в лог error
        return "Сервер openAPI не доступен, попробуйте позже", 0       


# Загрузка данных из файла БД - users.csv, если он существует, иначе создание нового DataFrame
import pandas as pd
try:
    users_df = pd.read_csv('users.csv')
except FileNotFoundError:
    users_df = pd.DataFrame(columns=['user_id', 'tokens', 'context', 'token_capacity', 'context_capacity', 'last_request_time', 'token_clear_time'])
    users_df.to_csv('users.csv', index=False)


# Функция регистрации пользователя
def user_reg(user_id):
    global users_df
     # Добавляем нового пользователя
    new_user_df = pd.DataFrame({'user_id': [user_id],
                                'tokens': [0],
                                'context': [''], 
                                'token_capacity': [max_token_usage],
                                'context_capacity': [max_context_length], 
                                'last_request_time': [0.0], 
                                'token_clear_time': [int(time())]})
    users_df = pd.concat([users_df, new_user_df], ignore_index=True)
    
    
# Функция сохранения данных в файл users.csv
def save_user_data():
    """ Функция сохранения данных в файл users.csv """
    global users_df
    users_df.to_csv('users.csv', index=False)                                 # записываем данные в файл
    logging.info(f'данные сохранены в файл users.csv')                        # добавляем в лог info


# Функция обновления информации о пользователе
def update_user_info(user_id, tokens=0, context=''):
    """ Функция обновления информации о пользователе"""
    # Обновляем информацию о пользователе
    idx = users_df.index[users_df['user_id'] == user_id].tolist()[0]          # получаем индекс строки пользователя user_id
    users_df.at[idx, 'tokens'] += tokens                                      # увеличиваем количество использованных токенов
    users_df.at[idx, 'context'] += context                                    # увеличиваем величину контекста беседы
    users_df.at[idx, 'last_request_time'] = int(time())                       # запоминаем время последнего запроса
    
 
 # Функция очистки истории чата   
def clear_chat_histoty(user_id: int) -> None:
    """Очистка истории чата для конкретного пользователя"""
    global chat_history
    global init_bot_role
    chat_history[user_id] = copy.deepcopy(init_bot_role)                      # очищаем историю чата - остается только роль для ChatGPT  


def limit_checking(user_id, context_length):
    """ Функция проверки превышения лимита токенов и лимита контекста беседы"""
    global users_df
    idx = users_df.index[users_df['user_id'] == user_id].tolist()[0]          # получаем индекс строки пользователя user_id
    full_context_length = len(users_df.at[idx, 'context']) + context_length   # вычисляем полную длину контекста 
    tokens = users_df.at[idx, 'tokens']
    logging.info(f'full_context_length user {user_id}: {full_context_length}') # добавляем в лог info

    if  tokens > users_df.at[idx, 'token_capacity']:                          # проверяем кол-во токенов 
        print(f'tokens = {tokens}')
        answer = "У вас закончились токены!"                                  # превышен лимит токенов
        logging.warning(f'предупреждение: user {user_id}: {answer}')          # добавляем в лог warning
    
    elif full_context_length > users_df.at[idx, 'context_capacity']:          # проверяем размер контекста        
        answer = "Превышен лимит длины контекста! Произведите очистку"        # превышен лимит длины контекста
        logging.warning(f'предупреждение: user {user_id}: {answer}')          # добавляем в лог warning
    else: return None
    return answer


def get_tokens(user_id):
    """Функция обнуления счетчика токенов"""
    global users_df
    idx = users_df.index[users_df['user_id'] == user_id].tolist()[0]          # получаем индекс строки пользователя user_id
    users_df.at[idx, 'tokens'] = 0   
    logging.info(f'user {user_id} обнуление счетчика токенов')                # добавляем в лог info
    

def clean_context(user_id):
    global users_df
    """Функция очистки контекста беседы"""
    idx = users_df.index[users_df['user_id'] == user_id].tolist()[0]          # получаем индекс строки пользователя user_id
    users_df.at[idx, 'context'] = ""    
    logging.info(f'user {user_id} чистка контекста беседы')                   # добавляем в лог info
    

# инициализация бота
bot=Bot(token = base64.b64decode(TELEGRAM_TOKEN).decode())  
dp=Dispatcher(bot)


# Обработчик команды /tokens
@dp.message_handler(commands=['tokens'])
async def clean_tokens(message: types.Message):
    global users_df
    user_id = message.from_user.id                                             # получаем id пользователя
    logging.info(f'сообщение от user {user_id}: {message.text}')               # добавляем в лог info      

    if user_id in users_df['user_id'].values:                                  # пользователь зарегистрирован
        idx = users_df.index[users_df['user_id'] == user_id].tolist()[0]       # получаем индекс строки пользователя user_id
        
        if int(time()) - users_df.at[idx, 'token_clear_time'] > 300:           # ограничение обнуления счетчика токенов - 1 раз в 5 мин
            get_tokens(user_id)                                                # обнуление счетчика токенов    
            users_df.at[idx, 'token_clear_time'] = int(time())                 # запоминаем время обнуления счетчика токенов
            bot_answer = ("Счетчик токенов обнулен") 
            logging.info(f'user {user_id}: {bot_answer} - {int(time())}')      # добавляем в лог info     
        else:
            bot_answer = ("Получение новых токенов не ранее чем через 5 мин")  
    else:
        bot_answer = ("Необходимо зарегистрироваться!")                        # пользователь не зарегистрирован
    await message.answer(bot_answer)


# Обработчик команды /clean
@dp.message_handler(commands=['clean'])
async def context_clean(message: types.Message):
    global users_df
    user_id = message.from_user.id                                             # получаем id пользователя
    logging.info(f'сообщение от {user_id}: {message.text}')                    # добавляем в лог info

    if user_id in users_df['user_id'].values:                                  # пользователь зарегистрирован
        clean_context(user_id)                                                 # очистка контекста беседы   
        save_user_data()                                                       # обновление файла users.csv
        clear_chat_histoty(user_id)                                            # очистка истории чата GPT 
        bot_answer = ("Контекст беседы очищен!!!") 
             
    else:
        bot_answer = ("Необходимо зарегистрироваться!")                        # пользователь не зарегистрирован
    await message.answer(bot_answer)


# Обработчик команды /start, регистрация пользователя
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    global users_df
    user_id = message.from_user.id                                             # получаем id пользователя    
    logging.info(f'сообщение от user {user_id}: {message.text}')               # добавляем в лог info
    
    if user_id in users_df['user_id'].values:
        bot_answer = (f"И снова здравствуйте, {message.from_user.username}!")  # уже зарегистрирован    
    else:
        user_reg(user_id)                                                      # регистрация пользователя
        bot_answer = (f"Привет, {message.from_user.username}!")                # новый пользователь 
        logging.info(f'регистрация пользователя {user_id}')                    # добавляем в лог info          
    await message.answer(bot_answer)


# Обработчик сообщений telegram бота 
@dp.message_handler()
async def respond (message:types.Message):
    global users_df
    user_id = message.from_user.id                                             # получаем id пользователя      
    logging.info(f'сообщение от user {user_id}: {message.text}')               # добавляем в лог info

    if user_id in users_df['user_id'].values:                                  # пользователь зарегистрирован
        idx = users_df.index[users_df['user_id'] == user_id].tolist()[0]       # получаем индекс строки пользователя user_id
        
        if time() - users_df.at[idx, 'last_request_time'] < 1:                 # ограничение количества запросов
            await message.answer("Не так быстро! Можно сделать только 1 запрос в 1 секунду!")
        else:
            checking_result = limit_checking(user_id, len(message.text))  
            if checking_result is None:                                        # проверка лимита токенов и лимита контекста сообщения 
                bot_response, tokens = get_bot_response(user_id, message.text) # Получаем текущий chat_history пользователя
                context = f" You: {message.text} Bot: {bot_response}"          # Добавляем текущий контекст к существующему
                update_user_info(user_id, tokens, context)                     # Обновляем информацию о пользователе
                save_user_data()                                               # сохраняем данные в базу                   

                await message.answer(bot_response)                             # возвращаем ответ Chat GPT
            else:
                await message.answer(checking_result)

    else:                                                                      # пользователь не зарегистрирован
        await message.answer("Необходимо зарегистрироваться!") 



if __name__ == "__main__":
    from aiogram import executor 

    #Запуск telegram бота 
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, loop=loop, skip_updates=True)
















