# задача 3-2
def format_contact(*agrs) -> None:
    """ функция преобразования контакта - фамилия имя отчество в фамилия + инициалы"""

    last_name = agrs[0]
    # добавление в фоматируемый контакт фамилии
    format_fio = last_name 
    # формирование и добавление инициалов
    for i in range(1,len(agrs)):
        agr = agrs[i]
        format_fio = format_fio + " " + agr[0] + "."

    return print(format_fio)
   
# ввод контакта
fio = list(input().split())

# преобразование контакта
format_contact(*fio)