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
