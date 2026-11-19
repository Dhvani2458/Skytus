#A student class with a method to calculate average marks
print("\nA student class with a method to calculate average marks.")
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)


name = input("Enter student name: ")

marks = []

for i in range(3):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

student = Student(name, marks)

print(f"\nStudent: {student.name}")
print(f"Average marks: {student.average()}")

