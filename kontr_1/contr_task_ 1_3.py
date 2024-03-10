# задача 3 (контрольная 1)
# импортируем функцию itemgetter для сортировки списка кортежей по ключу.
from operator import itemgetter

def get_five_frequent_letters(text: str) -> str:
    """функция возвращает слово, составленное из 5 букв 
        с наибольшей частотой вхождения в текст"""
    # словарь подсчитанных букв
    letter_count = {}

    # подсчитываем количество каждого символа в тексте    
    for char in text:
        # Проверка, является ли символ буквой
        if char.isalpha():     
            letter_count[char] = letter_count.get(char, 0) + 1

    # Преобразование словаря в список кортежей (буква, частота)
    letter_count_list = list(letter_count.items())

    # Сортировка по частоте (второй элемент кортежа)
    letter_count_list.sort(key=itemgetter(1), reverse=True)

    # составление слова из 5 букв с наибольшей частотой вхождения в текст
    word = ""
    for i in range(len(letter_count_list)):
        word += letter_count_list[i][0]
        if i >= 4:
            break
    return word
 
# ввод текста
text = input()

print(get_five_frequent_letters(text))