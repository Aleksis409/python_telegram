# задача 2-1
# ввод количества грибов n
n = int(input())
if n <= 0:
    print("Количество грибов не может быть меньше либо рано нулю")
    exit()
# ввод номера гриба k
k = int(input())
if (k <= 0) or (k >= n):
  print("Номер гриба не может быть меньше либо ранен нулю или больше количества грибов")
  exit()
k = k - 1 # корректировка номера гриба в соответствие с нумерацией списка с 0

error_message =  "введено количество грибов меньше или больше " + str(n) 
# ввод грибов Чижика
chigik_mushrooms = list(map(int, input().split()))
if len(chigik_mushrooms) != n:
  print(error_message)
  exit()

# ввод грибов Пыжика
pygik_mushrooms = list(map(int, input().split()))
if len(pygik_mushrooms) != n:
  print(error_message)
  exit()
  
# ввод грибов Ксении
ksenya_mushrooms = list(map(int, input().split()))
if len(ksenya_mushrooms) != n:
  print(error_message)
  exit()

# сортировка грибов по возрастанию
chigik_mushrooms.sort()
pygik_mushrooms.sort()
ksenya_mushrooms.sort()

# выбор победителя
if chigik_mushrooms[k] < pygik_mushrooms[k] > ksenya_mushrooms[k]:
  winner = "Пыжик"
elif pygik_mushrooms[k] < chigik_mushrooms[k] > ksenya_mushrooms[k]: 
  winner = "Чижик"
elif pygik_mushrooms[k] < ksenya_mushrooms[k] > chigik_mushrooms[k]:
  winner = "Ксения"
else:
  winner = "Ничья"

print(winner)
