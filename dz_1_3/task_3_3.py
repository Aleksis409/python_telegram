# задача 3-3
# образовательная база
students = [{"id":367673,"full_name":"Ярцев Валерий Рустэмович"},
            {"id":563234,"full_name":"Шиптенко Виталий Программирович"},
            {"id":982123,"full_name":"Датабейзов Иван Джетлагович"},]


# функция
def give_license(student_id: int) -> bool:
    """ функция проверки регистрации студента в образовательной базе"""

    # объявляем глобальную переменную
    global students

    # цикл для проверки каждого словаря - элемента списка образовательной базы, по id студента
    for student in students:
        if student['id'] == student_id:
            res = True
            break
        else:
            res = False

    return res


# ввод id студента
student_id = input()
# результат
print("Студент " + student_id + " есть в образовательной базе = " + str(give_license(int(student_id))))