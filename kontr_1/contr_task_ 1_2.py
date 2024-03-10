# задача 2 (контрольная 1)
def get_annual_rating(rating_list: list[int]) -> int:
    """функция возвращает среднееарифметическое всех четных оценок ученика"""

    rating = 0
    number_of_even = 0
    for i in rating_list:
        if i % 2 == 0:
            number_of_even += 1 
            rating += i
    return rating // number_of_even


# количество оценок   
number_of_ratings = int(input())
 
# ввод оценок
ratings = list(map(int, input().split()))

if number_of_ratings < len(ratings) or number_of_ratings > len(ratings):
    print("Введено количество оценок не равное " + str(number_of_ratings))
    exit
else:
    print(get_annual_rating(ratings))