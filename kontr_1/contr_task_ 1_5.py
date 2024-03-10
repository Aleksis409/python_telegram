# задача 5 (контрольная 1)

def is_palindrom(num: int) -> bool:
    """функция проверки является ли число палиндромом"""

    revers_num = ''.join(reversed(str(num)))
    return str(num) == revers_num


def palindrome_search(num: int) -> int:
    """функция поиска ближайщего палиндрома"""

    # проверка, положительное ли число
    if num < 0:
        print("Необходимо ввести положительное число")
        return 0
    
    # проверка, является ли число палиндромом
    if is_palindrom(num):
        return num
    else:
        # ищем полиндром вниз и вверх от заданного числа
        sum_down = sum - 1
        sum_up = sum + 1
        
        while True:
            if is_palindrom(sum_down):
                return sum_down
            elif is_palindrom(sum_up):
                return sum_up
            
            sum_up += 1
            sum_down -= 1


# ввод суммы
sum = int(input())

print(palindrome_search(sum))

