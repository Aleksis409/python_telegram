# задача 5
total_weight = 0
weight = 0
count = 0
while total_weight < 50:
  weight = int(input())
  total_weight = total_weight + weight
  count+=1 
  
print(total_weight - weight)  
print(count - 1)