import pandas as pd
import os
import matplotlib.pyplot as plt

# Получение пути к текущему скрипту
script_path = os.path.dirname(os.path.realpath(__file__))

# Изменение текущей директории на директорию скрипта
os.chdir(script_path)

# путь к файлу animals.csv
file_path = './animals.csv'


# **************** задание 1 *********************
# Открытие датасета с индексацией по колонке 'name'
df = pd.read_csv(file_path, index_col='name')

# Вывод первых нескольких строк DataFrame для проверки
print(df.head())

# Вывод всех строк DataFrame 
# print(df)


# ***************** задание 2 ********************
# Вывод цены крокодила в зоомагазине
crocodile_price = df.loc['crocodile', 'shop_price']

print(f"\nЦена крокодила в зоомагазине: ${crocodile_price}")


# ***************** задание 3 ********************
# Расчет средней цены всех животных
average_price = df['shop_price'].mean()

print(f"\nСредняя цена всех животных: ${average_price:.2f}")


# ***************** задание 4 ********************
# Нахождение максимального показателя IQ
max_iq_score = df['iq_score'].max()

# Выбор всех животных с максимальным IQ
animals_with_max_iq = df[df['iq_score'] == max_iq_score].index.tolist()

print(f"\nЖивотные с наибольшим показателем IQ ({animals_with_max_iq}):")


# ***************** задание 5 ********************
# Выбор строк с животными коричневого цвета
brown_animals = df[df['color'] == 'brown']

# Нахождение минимальной стоимости среди этих животных
min_price_brown_animals = brown_animals['shop_price'].min()

# Выбор только столбца 'name' для животных коричневого цвета с минимальной стоимостью
animals_with_min_price_and_brown_color = brown_animals[brown_animals['shop_price'] == min_price_brown_animals].index.tolist()

print(f"\nИмена животных коричневого цвета с наименьшей стоимостью ({animals_with_min_price_and_brown_color}):")


# *************** задание 6 ********************
# Рассчитываем среднее IQ для каждой среды обитания
average_iq_by_habitat = df.groupby('habitat')['iq_score'].mean()

print("\nСреднее IQ для каждой среды обитания:")
print(str(average_iq_by_habitat.to_string()))


# *************** задание 7 ********************
# Загрузка новой таблицы с ростом животных
heights_df = pd.read_csv('./height.csv')

# Объединение таблиц по именам животных
df = pd.merge(df, heights_df, on='name')

# Вывод результата
print("\n")
print(df)


# *************** задание 8 ********************
# Фильтрация только летающих животных
flying_animals = df[df['habitat'] == 'air']

# Вывод числовых данных гистограммы роста всех летающих животных
""" Количество записей (count): количество непустых значений в столбце.
    Среднее значение (mean): среднее арифметическое всех значений в столбце.
    Стандартное отклонение (std): мера разброса значений относительно среднего значения.
    Минимальное значение (min): наименьшее значение в столбце.
    (25%): значение, ниже которого попадает 25% данных.
    Медиана (50%): значение, разделяющее набор данных на две равные части.
    (75%): значение, ниже которого попадает 75% данных.
    Максимальное значение (max): наибольшее значение в столбце."""

print("\nГистогграмма роста всех летающих животных:")
print(str(flying_animals['height'].describe().to_string()))   
flying_animals['height'].hist()
plt.show()