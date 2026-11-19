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