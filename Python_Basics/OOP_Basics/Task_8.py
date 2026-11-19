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

