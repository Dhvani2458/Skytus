# Demonstrate the use of super() in inheritance.
print("\nDemonstrate the use of super() in inheritance.")
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name: {self.name}")


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def display(self):
        super().display()
        print(f"Course: {self.course}")


name = input("Enter student name: ")
course = input("Enter course: ")

student = Student(name, course)

student.display()