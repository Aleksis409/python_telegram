# 
import openai
import base64

# импорт телеграм токена из файла config.py
from config import API_KEY

openai.api_key = base64.b64decode(API_KEY).decode()
model = "gpt-3.5-turbo"

## ************** Задача 1 **************
# chat_history = []
# chat_history.append({"role": "system", "content": "You are a helpful assistant"})
# while True:
#     user_input = input("You: ")
#     chat_history.append({"role": "user", "content": user_input})
#     # print(chat_history)
#     response = openai.ChatCompletion.create(
#         model = model,
#         messages = chat_history
#     )
#     bot_response = response['choices'][0]['message']['content']
#     chat_history.append({"role": "assistant", "content": bot_response})
#     print(f"Bot: {bot_response}")


# # ************** Задача 2 ************** 
# chat_history = []
# chat_history.append({"role": "system", "content": "Ты грозный, веселый пират, который рассказывает анекдоты. Отвечай используя пиратские слова и выражения, ругайся как пират"})

# while True:
#     user_input = input("You: ")
#     chat_history.append({"role": "user", "content": user_input})
#     # print(chat_history)
#     response = openai.ChatCompletion.create(
#         model = model,
#         messages = chat_history,
#         temperature = 0.7
#     )
#     bot_response = response['choices'][0]['message']['content']
#     chat_history.append({"role": "assistant", "content": bot_response})
#     print(f"Bot: {bot_response}")


# # ************** Задача 3 ************** 
# #  bot.py - запуск телеграм бота,  polly_bot_handlers.py - инициализация телеграм бота
    
# def get_bot_response(telegram_prompt: str) -> str: 

#     chat_history = [] 
#     chat_history.append({"role": "system", "content": "Ты грозный, веселый пират, который рассказывает анекдоты. Отвечай используя пиратские слова и выражения, ругайся как пират"})

#     while True:
#         chat_history.append({"role": "user", "content": telegram_prompt})
#         # print(chat_history)
#         response = openai.ChatCompletion.create(
#             model = model,
#             messages = chat_history,
#             temperature = 0.5
#         )
#         bot_response = response['choices'][0]['message']['content']
#         chat_history.append({"role": "assistant", "content": bot_response})
#         print(f"You: {telegram_prompt}")
#         print(f"Bot: {bot_response}")
#         return bot_response
    

# ************** Задача 4  ************** 
#  bot.py - запуск телеграм бота,  polly_bot_handlers.py - инициализация телеграм бота
    
def get_bot_response(telegram_prompt: str) -> str: 

    chat_history = [] 
    chat_history.append({"role": "system", "content": "Ты грозный, веселый пират, который рассказывает анекдоты. Отвечай используя пиратские слова и выражения, ругайся как пират"})

    while True:
        chat_history.append({"role": "user", "content": telegram_prompt})
        # print(chat_history)
        response = openai.ChatCompletion.create(
            model = model,
            messages = chat_history,
            temperature = 0.5
        )
        bot_response = response['choices'][0]['message']['content']
        chat_history.append({"role": "assistant", "content": bot_response})
        print(f"You: {telegram_prompt}")
        print(f"Bot: {bot_response}")
        return chat_history
    

