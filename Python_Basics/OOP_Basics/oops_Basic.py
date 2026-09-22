#Car Class with attributes like Brand, Model and Speed and method to Accelerate/Brake
print("Car Class with attributes like Brand, Model and Speed and method to Accelerate/Brake.")
class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 10
        if self.speed < 0:
            self.speed = 0

    def display(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Speed: {self.speed}")

brand = input("Enter Brand Name: ")
model = input("Enter Model Name: ")
speed = int(input("Enter Current Speed: "))
car = Car(brand, model, speed)


car.accelerate()
print("\nAfter Accelration: ")
car.display()

car.brake()
print("\nAfter Braking: ")
car.display()


#Create a Banking Account class with deposite and withdrawl method
print("\nCreate a Banking Account class with deposite and withdrawl method.")
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawl(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance.")

    def display(self):
        print(f"Balance: {self.balance}")

balance = float(input("Enter initial balance: "))

account = BankAccount(balance)

deposit = float(input("Enter deposit amount: "))
account.deposit(deposit)

withdraw = float(input("Enter withdrawal amount: "))
account.withdrawl(withdraw)

account.display()

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

#A Rectangle class with method to find area and perimeter
print("\nA Rectangle class with method to find area and perimeter")
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


length = float(input("Enter length: "))
width = float(input("Enter width: "))

rectangle = Rectangle(length, width)

print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")

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

#A Book class t store title, author and price and display details
print("\nA Book class t store title, author and price and display details.")
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ₹{self.price}")


title = input("Enter book title: ")
author = input("Enter author name: ")
price = float(input("Enter book price: "))

book = Book(title, author, price)

book.display()

#A Circle class to find area and circumference
print("\nA Circle class to find area and circumference")
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius


radius = float(input("Enter radius: "))

circle = Circle(radius)

print(f"Area: {circle.area()}")
print(f"Circumference: {circle.circumference()}")

#A laptop class with a method to apply discounts on price
print("\nA laptop class with a method to apply discounts on price")
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def apply_discount(self, discount):
        self.price = self.price - (self.price * discount / 100)

    def display(self):
        print(f"Brand: {self.brand}")
        print(f"Final Price: ₹{self.price}")


brand = input("Enter laptop brand: ")
price = float(input("Enter laptop price: "))
discount = float(input("Enter discount percentage: "))

laptop = Laptop(brand, price)

laptop.apply_discount(discount)

laptop.display()

#A Flight class with seat booking functionality
print("\nA Flight class with seat booking functionality")
class Flight:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.booked_seats = 0

    def book_seat(self):
        if self.booked_seats < self.total_seats:
            self.booked_seats += 1
            print("Seat booked successfully")
        else:
            print("No seats available")

    def display(self):
        print(f"Total seats: {self.total_seats}")
        print(f"Booked seats: {self.booked_seats}")
        print(f"Available seats: {self.total_seats - self.booked_seats}")


total_seats = int(input("Enter total number of seats: "))

flight = Flight(total_seats)

number = int(input("How many seats do you want to book? "))

for i in range(number):
    flight.book_seat()

flight.display()

#A shop class with a method to add and list products
print("\nA shop class with a method to add and list products.")
class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        print("\nProducts:")

        for product in self.products:
            print(product)


shop = Shop()

number = int(input("How many products do you want to add? "))

for i in range(number):
    product = input(f"Enter product {i + 1}: ")
    shop.add_product(product)

shop.list_products()