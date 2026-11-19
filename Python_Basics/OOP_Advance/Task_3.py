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
