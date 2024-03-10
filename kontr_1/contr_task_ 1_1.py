# задача 1 (контрольная 1)
def get_squares_sum(arr: list[int]) -> int:
    """функция возвращает сумму квадратов целых чисел"""

    sum = 0
    for i in arr:
        sum += i**2
    return sum
    
# #  проверка
# print(int(get_squares_sum([0, 1, 2, 3])))
# print(int(get_squares_sum([4, 4])))
# print(int(get_squares_sum([-1, -2])))