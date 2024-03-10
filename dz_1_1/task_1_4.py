# задача 4
apple_cal = 52
banana_cal = 89
tomato_cal = 24
number_of_calories = 0
cal = 0

number_of_meals = input()

for i in range(int(number_of_meals)):
  product = input()
  quantity = input()

  if product == "яблоки":
    cal = apple_cal
  elif product == "бананы":
    cal = banana_cal
  elif product == "помидоры":
    cal = tomato_cal
  else:
    print("Некорректный продукт") 
  number_of_calories = number_of_calories + int(quantity) * cal * 10    

print(number_of_calories)