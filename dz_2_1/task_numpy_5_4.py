import numpy as np

# Создание массива
array_1 = np.array([2, 5, 3, 6, 8, 11, 13])

# Умножение всех элементов на 5
array_2 = array_1 * 5

# Возведение в степень 0.25
array_3 = np.power(array_2, 0.25)

# Нахождение медианы
mediane = np.median(array_3)

print("Исходный массив:", array_1)
print("Массив умноженный на 5:", array_2)
print("Массив возведенный в степень 0.25:", array_3)
print("Медиана:", mediane)