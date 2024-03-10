# задача 3-1

def format_contact(last_name: str, first_name: str, patronymic: str = "") -> None:
    """ функция преобразования контакта - фамилия имя отчество в фамилия + инициалы"""

    if patronymic != "":
         return print(last_name + " " + first_name[0] + ". " + patronymic[0] + ".")
    else:
        return print(last_name + " " + first_name[0] + ".")

# ввод контакта
fio = list(input().split())

# преобразование контакта
format_contact(*fio)

