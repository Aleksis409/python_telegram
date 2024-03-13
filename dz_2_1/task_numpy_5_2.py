import numpy as np

# Создание массива с числами от 0 до 10
array1 = np.arange(0, 11)

# Создание массива с числами от 5 до 15
array2 = np.arange(5, 16)

# Вычисление скалярного произведения
scalar = np.dot(array1, array2)

print("Массив 1:", array1)
print("Массив 2:", array2)
print("Скалярное произведение:", scalar)