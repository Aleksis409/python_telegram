# задача 2
def get_number_of_ways(n):
    # Инициализируем множество для хранения комбинаций прыжков
    ways = set()
    
    # Рекурсивная функция для подсчета способов
    def counting_the_number_of_ways(curr, path):
        if curr == n:                               # Если достигли школы, добавляем комбинацию в множество
            ways.add(tuple(sorted(path)))           # Сортируем прыжки перед добавлением в множество
            return
        if curr > n:                                # Если превысили расстояние до школы, выходим из рекурсии
            return
        
        # Рекурсивные вызовы для всех возможных прыжков
        counting_the_number_of_ways(curr + 1, path + [1])
        counting_the_number_of_ways(curr + 2, path + [2])
        counting_the_number_of_ways(curr + 3, path + [3])

    counting_the_number_of_ways(0, [])              # Начинаем с дома
    return len(ways)                                # Возвращаем количество уникальных комбинаций

def main():
    n = int(input())
    print(get_number_of_ways(n))

if __name__ == "__main__":
    main()







