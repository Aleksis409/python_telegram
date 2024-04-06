# 
import openai
import base64
import copy

# импорт телеграм токена из файла config.py
from config import API_KEY

openai.api_key = base64.b64decode(API_KEY).decode()
model = "gpt-3.5-turbo"

chat_history = {}
init_bot_role = [{"role": "system", "content": "Ты грозный, веселый пират, который рассказывает анекдоты. Отвечай используя пиратские слова и выражения, ругайся как пират"}]

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
    print(f"chat_history: {chat_history}")
    
    return bot_response, total_tokens
    
def clear_chat_histoty(user_id: int) -> None:
    """Очистка истории чата для конкретного пользователя"""
    global chat_history
    global init_bot_role
    chat_history[user_id] = copy.deepcopy(init_bot_role)   # оператор = создает ссылку на объект, а не его копию. 
                                                           # Поэтому присвоение init_bot_role переменной chat_history[user_id] с помощью =, 
                                                           # делает их обе ссылающимися на один и тот же объект. Необходимо через copy.deepcopy(init_bot_role)
                                                           # при этом создается копия объекта

