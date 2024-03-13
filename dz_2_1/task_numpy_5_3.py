import numpy as np

# Создание массива с числами от 15 до 105 с шагом 2
array = np.arange(15, 106, 2)

# Нахождение среднего значения
average_value = np.mean(array)

print("Массив:", array)
print("\n Среднее значение:", average_value)