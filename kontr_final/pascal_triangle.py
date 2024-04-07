def generate_pascal_triangle(n: int):
    # задача 1
    """Функция генерирует треугольник Паскаля"""
    triangle = []
    for i in range(n):
        level = [1]                                              # первый элемент уровня всегда 1
        if i > 0:
            prev_level = triangle[i - 1]
            for j in range(1, i):
                level.append(prev_level[j - 1] + prev_level[j])  # добавляем элемент = сумме двух чисел над текущим
            level.append(1)                                      # последний элемент всегда 1
        triangle.append(level)                                   # добавляем уровень в треугольник
    return triangle

def main():
    n = int(input())
    pascal_triangle = generate_pascal_triangle(n)
    # for level in pascal_triangle:                              # печать треугольника Паскаля
    #     print(level)
    print(pascal_triangle)

if __name__ == "__main__":
    main()
