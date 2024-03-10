# задача 3
product = input()
quantity = input()
apple_cal = 52
banana_cal = 89
tomato_cal = 24
number_of_cal = 0
if product == "яблоки":
  cal = apple_cal
elif product == "бананы":
  cal = banana_cal
elif product == "помидоры":
  cal = tomato_cal
else:
  print("Некорректный продукт") 
  cal = 0 
number_of_cal = int(quantity) * 10 * cal
print(number_of_cal)