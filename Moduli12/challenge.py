from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def area(self):
        pass

class Person(Printable):
    def __init__(self, name, age, weight, height ):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

class Adult(Person):
    def __init__(self):


    def area(self):
        return self.weight * self.height

class Child(Person):
    def __init__(self):


    def area(self):
        return self.weight * self.height

person_1 = Adult("Anna", 30, 60, 1.7)
person_1.print_info()