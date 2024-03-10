# задача 4-4

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

# инициализируем класс Student
class Student(Person):
    def __init__(self, name: str, age: int, grade: int, subjects: list[str]):
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
        return self.name + ", "  + str(self.age) +  ".\n" + str(self.__grade) + " grade\n" + "Subjects studying: \n" + result
            
    def finish_grade(self):
        """метод увеличивает номер класса на 1"""
        self.__grade = self.get_grade() + 1

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
    
# инициализируем класс Group
class Group:
    def __init__(self, group_name: str, students: list[Student], group_teacher: Teacher):
        self.students = students
        self.group_teacher = group_teacher
        self.group_name = group_name

    def get_info(self) -> str:
        """метод возвращает информацию по классу"""
        result = ''
        for i in self.students:
            result += "\n" + i.get_info() + "\n"
        return '\"' + self.group_name + "\n" + "Group_teacher: \n" + self.group_teacher.get_info() + "\n\n" + "Students:" + result + '\"'

    def get_students_number(self) -> int:
        """метод возвращает колличество студентов"""
        return len(self.students)


# # проверка
# student1 = Student("Виталий", 23, 3, ["Maths", "Physcis"])
# student2 = Student("Геннадий", 21, 3, ["Maths", "Physcis"])
# student3 = Student("Иван", 43, 3, ["Maths", "Physcis", "PE"])
# teacher = Teacher("Ярцев Валерий Рустэмович", 20, "Informatic steacher", 200)
# group = Group("3A", [student1, student2, student3], teacher)

# print(group.get_students_number())
# print("-----------------------------")
# print(group.get_info())