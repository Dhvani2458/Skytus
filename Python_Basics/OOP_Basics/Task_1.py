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
