# задача 2-2
# ввод количества ежей n
n = int(input())

coordinates_list = list ()
# ввод координат
for i in range(n):
  coordinate = tuple(map(int, input().split()))
  coordinates_list.append(coordinate)

print(coordinates_list)
