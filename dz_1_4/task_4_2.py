# задача 4-2
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
        return self.name + ", "  + str(self.age)

# инициализируем класс Student
class Student(Person):
    def __init__(self, name: str, age: int, grade: int, subjects: list):
        super().__init__(name,age)
        self.__grade = grade
        self.subjects = subjects

    def get_grade(self) -> int:
        """метод возвращает номер класса ученика"""
        return self.__grade

    def get_info(self) -> str:
        """метод возвращает ФИО + возраст + номер класса + список предметов"""
        # преобразуем список предметов в строку, и разделяем предметы запятой + перенос строки
        separator = ',\n'
        result = separator.join(self.subjects)
        return '\"' + self.name + ", "  + str(self.age) +  ".\n" + str(self.__grade) + " grade\n" + "Subjects studying: \n" + result + '\"'
            
    def finish_grade(self):
        """метод увеличивает номер класса на 1"""
        self.__grade = self.get_grade() + 1
        
    

# # проверка
# student = Student("Иванов Иван Иванович", 11, 3, ["maths","physics"])
# print(student.get_name())
# print(student.get_age())
# print(student.get_grade())
# student.finish_grade()
# print(student.get_grade())
# print("-----------------------------")
# print(student.get_info())