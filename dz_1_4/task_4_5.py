# задача 4.5
# абстрактный базовый класс
from abc import ABC, abstractmethod

# абстрактный класс
class Animal(ABC):
    @abstractmethod
    def __init__(self):
        self.habitat = None  # Абстрактная переменная среда обитания
        self.age = None  # Абстрактная переменная возраст
        self.size = None  # Абстрактная переменная размер

    def get_habitat(self):
        """метод возвращает среду обитания"""
        return self.habitat

    def get_age(self):
        """метод возвращает возраст"""
        return self.age

    def get_size(self):
        """метод возвращает размер"""
        return self.size

    def walk(self):
        """метод возвращает звук животного"""
        pass

# инициализация класса собаки
class Dog(Animal):
    def __init__(self, habitat: str, age: int, size: str):
        super().__init__()
        self.habitat = habitat
        self.age = age
        self.size = size

    def walk(self):
        return "Gav, Gav"
    
# инициализация класса кошки
class Cat(Animal):
    def __init__(self, habitat: str, age: int, size: str):
        super().__init__()
        self.habitat = habitat
        self.age = age
        self.size = size

    def walk(self) -> str:
        return "Meow, Meow"
    
# инициализация класса дельфина
class Dolphin(Animal):  
    def __init__(self, habitat: str, age: int, size: str):
        super().__init__()
        self.habitat = habitat
        self.age = age
        self.size = size

    def walk(self) -> str:
        return "Tiu, Tiu"

# инициализация класса слона
class Elephant(Animal):
    def __init__(self, habitat: str, age: int, size: str):
        super().__init__()
        self.habitat = habitat
        self.age = age
        self.size = size
    
    def walk(self) -> str:
        return "Thuu, Thuu"

# инициализация класса циркового ансамбля животных
class CircusAnimalEnsemble:
    def __init__(self, animals: list[Animal]):
        self.animals = animals

    def speak(self) -> str:
        sound = ""
        for i in self.animals:
            walk_result = i.walk()
            if walk_result is not None: # проверяем,что животное издает звук
                sound += i.walk() + "\n"
        return sound



# # проверка
# dog1 = Dog("город", 3, "средний")
# cat1 = Cat("деревня", 2, "маленький")
# dolphin1 = Dolphin("море", 10, "средний")
# elephant1 = Elephant("саванна", 25, "большой")

# print(dog1.get_age())
# print(dog1.get_size())
# print(dog1.get_habitat())
# print("--------------------")
# print(cat1.get_age())
# print(cat1.get_size())
# print(cat1.get_habitat())
# print("--------------------")
# print(dolphin1.get_age())
# print(dolphin1.get_size())
# print(dolphin1.get_habitat())
# print("--------------------")
# print(elephant1.get_age())
# print(elephant1.get_size())
# print(elephant1.get_habitat())
# print("--------------------")

# ensemble1 = CircusAnimalEnsemble([cat1])
# ensemble2 = CircusAnimalEnsemble([cat1, dog1])
# ensemble3 = CircusAnimalEnsemble([cat1, dog1, dolphin1, elephant1])
# print(ensemble1.speak())
# print("--------------------")
# print(ensemble2.speak())
# print("--------------------")
# print(ensemble3.speak())
