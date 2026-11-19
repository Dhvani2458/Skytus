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
