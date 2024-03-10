# задача 2-4
# ввод количества студентов
students = int(input())

# ввод количества сочинений
works_number = int(input())

# список сочинений студентов
student_works = list()

# ввод работ студентов
for i in range(students):
    student_works.append(set(input().split()))

# список списанных работ
all_copy_works = list()

# наполнение списка списанных работ, которые списаны всеми студентами
intersection_set = student_works[0]
for i in range(1, students): 
    intersection_set=intersection_set.intersection(student_works[i])
    print(intersection_set)
    for work in intersection_set:
        all_copy_works.append(work)

# печать списка списанных работ без повторений
print(" ".join(set(all_copy_works)))