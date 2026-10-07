class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello I am {self.name}, my age is {self.age}")

person1 = Person("Blina", 17)
person2 = Person("Gresa", 18)

person1.greet()
person2.greet()