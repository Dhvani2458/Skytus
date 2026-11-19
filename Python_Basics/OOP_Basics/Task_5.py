#An employee class that display salary details
print("\nAn employee class that display salary details")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: ₹{self.salary}")


name = input("Enter employee name: ")
salary = float(input("Enter salary: "))

employee = Employee(name, salary)

employee.display()

