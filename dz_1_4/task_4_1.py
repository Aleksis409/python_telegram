# задача 4-1

# инициализируем класс Person
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_name(self) -> str:
        """метод возвращает ФИО"""
        return '\"' + self.name + '\"'
    
    def get_age(self) -> int:
        """метод возвращает возраст"""
        return self.age
    
    def get_info(self) -> str:
        """метод возвращает ФИО + возраст"""
        return '\"' + self.name + ", "  + str(self.age) + '\"'

# # проверка
# pupils = Person("Иванов Иван Иванович", 11)
# print(pupils.get_name())
# print(pupils.get_age())
# print("-----------------------------")
# print(pupils.get_info())
