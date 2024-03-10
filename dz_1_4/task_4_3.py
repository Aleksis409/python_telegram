# задача 4-3
# инициализируем класс Person
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_name(self) -> str:
        """метод возвращает ФИО"""
        return self.name
    
    def get_age(self) -> int:
        """метод возвращает возраст"""
        return self.age
    
    def get_info(self) -> str:
        """метод возвращает ФИО + возраст"""
        return self.name + ", "  + str(self.age)

# инициализируем класс Worker
class Worker:
    def __init__(self, position: str, wage: int):
        self.position = position
        self.wage = wage

    def get_wage(self) -> int:
        """метод возвращает зарплату рабочего"""
        return self.wage
    
    def get_position(self) -> str:
        """метод возвращает должность рабочего"""
        return self.position
    
# инициализируем класс Teacher
class Teacher(Person, Worker):
    def __init__(self, name: str, age: int, position: str, wage: int):
        super().__init__(name,age)
        self.position = position
        self.wage = wage

    def get_info(self) -> str:
        """метод возвращает ФИО + возраст + должность + зарплату"""
        return self.name + ", "  + str(self.age) +  " years.\n" + self.position + ", " + "wage: " + str(self.wage) + " rub."
            
# # проверка
# teacher = Teacher("Иванов Иван Иванович", 20, "Informatics teacher",200)
# print(teacher.get_name())
# print(teacher.get_age())
# print(teacher.get_wage())
# print(teacher.get_position())
# print("-----------------------------")
# print(teacher.get_info())
