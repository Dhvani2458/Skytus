# Create a base class Animal and subclasses Dog and Cat.
print("\nCreate a base class Animal and subclasses Dog and Cat.")
class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Dog says Woof!")


class Cat(Animal):
    def speak(self):
        print("Cat says Meow!")


choice = input("Enter animal (dog/cat): ").lower()

if choice == "dog":
    animal = Dog()
    animal.speak()

elif choice == "cat":
    animal = Cat()
    animal.speak()

else:
    print("Invalid animal")

# Create a class hierarchy for Vehicle → Car → ElectricCar. 
print("\nCreate a class hierarchy for Vehicle → Car → ElectricCar.")
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print(f"Brand: {self.brand}")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")


class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def display(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Battery: {self.battery} kWh")


brand = input("Enter car brand: ")
model = input("Enter car model: ")
battery = float(input("Enter battery capacity: "))

car = ElectricCar(brand, model, battery)

car.display()

# Implement method overriding in a base and derived class. 
print("\nImplement method overriding in a base and derived class.") 
choice = input("Enter animal (animal/dog): ").lower()

if choice == "animal":
    animal = Animal()
    animal.sound()

elif choice == "dog":
    dog = Dog()
    dog.sound()

else:
    print("Invalid choice")

# Demonstrate multiple inheritance with two parent classes.
print("\nDemonstrate multiple inheritance with two parent classes.") 
class Father:
    def father_info(self):
        print("Father's property")


class Mother:
    def mother_info(self):
        print("Mother's property")


class Child(Father, Mother):
    def child_info(self):
        print("Child's information")


name = input("Enter child's name: ")

child = Child()

print(f"Child: {name}")
child.father_info()
child.mother_info()
child.child_info()

# Create a polymorphic function that works with different shapes.
print("\nCreate a polymorphic function that works with different shapes.")  
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


def print_area(shape):
    print(f"Area: {shape.area()}")


choice = input("Enter shape (circle/rectangle): ").lower()

if choice == "circle":
    radius = float(input("Enter radius: "))
    shape = Circle(radius)

elif choice == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    shape = Rectangle(length, width)

else:
    print("Invalid shape")
    shape = None

if shape:
    print_area(shape)

# Create a Bank system with Savings Account and CurrentAccount classes.
print("\nCreate a Bank system with Savings Account and CurrentAccount classes.")  
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def display(self):
        print(f"Balance: ₹{self.balance}")


class SavingsAccount(BankAccount):
    def add_interest(self):
        interest = self.balance * 0.05
        self.balance += interest


class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        self.balance -= amount


choice = input("Enter account type (savings/current): ").lower()
balance = float(input("Enter initial balance: "))

if choice == "savings":
    account = SavingsAccount(balance)
    account.add_interest()
    account.display()

elif choice == "current":
    account = CurrentAccount(balance)

    amount = float(input("Enter withdrawal amount: "))

    if amount <= account.balance:
        account.withdraw(amount)
        account.display()
    else:
        print("Insufficient balance")

else:
    print("Invalid account type")

# Create a class with private attributes and getter/setter methods. 
print("\nCreate a class with private attributes and getter/setter methods.") 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Invalid age")


name = input("Enter name: ")
age = int(input("Enter age: "))

person = Person(name, age)

print(f"Name: {person.name}")
print(f"Age: {person.get_age()}")

new_age = int(input("Enter new age: "))

person.set_age(new_age)

print(f"Updated age: {person.get_age()}")


# Create a Teacher and Student class to show inheritance.
print("\nCreate a Teacher and Student class to show inheritance.")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Invalid age")


name = input("Enter name: ")
age = int(input("Enter age: "))

person = Person(name, age)

print(f"Name: {person.name}")
print(f"Age: {person.get_age()}")

new_age = int(input("Enter new age: "))

person.set_age(new_age)

print(f"Updated age: {person.get_age()}")


# Create a MusicPlayer class and subclass Spotify to override play method. 
print("\nCreate a MusicPlayer class and subclass Spotify to override play method.")
class MusicPlayer:
    def play(self):
        print("Playing music")


class Spotify(MusicPlayer):
    def play(self):
        print("Playing music from Spotify")


choice = input("Enter player (music/spotify): ").lower()

if choice == "music":
    player = MusicPlayer()
    player.play()

elif choice == "spotify":
    player = Spotify()
    player.play()

else:
    print("Invalid player")


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