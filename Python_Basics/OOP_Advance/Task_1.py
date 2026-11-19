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
