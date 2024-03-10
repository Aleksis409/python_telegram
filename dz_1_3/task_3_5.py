from typing import Callable

# декоратор
def fib_cache(func:Callable) -> Callable:
    """ функция декоратор для хеширования значения n-го числа фибоначи в словаре """
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return wrapper


@fib_cache
def fib(n: int) -> int:
    """ функция вычисления n-го числа фибоначи"""
    if n == 0:
        return 0
    if n == 1:
        return 1    
    return fib(n-1) + fib(n-2)

# ввод количества чисел n, которые надо вычислить3
n = int(input())
#  ввод порядковых номеров чисел в последовательности чисел Фибоначчи
list_num = list()
for i in range(n):
    num = int(input())
    if num >= 1:
        list_num.append(num)
    else:
        print("Ошибка, Число меньше 1")

# вычисление чисел Фибоначчи с соответствующем номером
for i in range(len(list_num)):
    print(fib(list_num[i] - 1))

