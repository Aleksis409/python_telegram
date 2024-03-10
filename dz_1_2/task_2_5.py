# задача 2-5
# ввод количества отправленных контрольных n
n = int(input())

# Создаем словарь содержащий данные по студентам
data_dict = {}

# ввод данных
for i in range(n):
    input_str = input()
    
    # Разбиваем введенную строку на отдельные числа
    numbers = [int(x) for x in input_str.split()]

    if len(numbers) == 4:
        # Создаем кортеж координат из первых трех чисел
        coordinates = tuple(numbers[:3])

        # Создаем множество контрольных из четвертого числа
        control_number = {numbers[3]}

        # Заполняем словарь
        if coordinates in data_dict:
            controls = data_dict[coordinates]
            data_dict[coordinates] = controls.union(control_number)
        else:
            data_dict[coordinates] = control_number
    else:
        print("Введено не достаточно данных < 4 чисел")

# вывод данных
for key in data_dict:
    print(*key, *data_dict[key]) 