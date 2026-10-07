class Student:
    school_name = "Digital School"

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student1=Student("Gresa", 20, "Python")
student2=Student("Yllka", 17, "JavaScript")
print(student1.school_name)
print(student1.course)
print(student2.course)