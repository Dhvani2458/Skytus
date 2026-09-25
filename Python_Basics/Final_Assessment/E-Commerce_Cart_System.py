products = {
    "laptop": 50000,
    "mouse": 800,
    "keyboard": 1500,
    "headphones": 2000,
    "usb cable": 500
}

cart = []

while True:
    print("\n===== E-COMMERCE CART =====")
    print("1. View Products")
    print("2. Add Product to Cart")
    print("3. View Cart")
    print("4. Remove Product from Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("\nAvailable Products:")

        for product, price in products.items():
            print(f"{product} - ₹{price}")

    elif choice == "2":
        print("\nAvailable Products:")

        for product, price in products.items():
            print(f"{product.title()} - ₹{price}")

        product = input("\nEnter product name to add: ").lower()

        if product in products:
            cart.append(product)
            print(f"{product.title()} added to cart.")
        else:
            print("Product not found.")

    elif choice == "3":
        if len(cart) == 0:
            print("\nCart is empty.")
        else:
            print("\n===== YOUR CART =====")

            total = 0

            for product in cart:
                price = products[product]
                print(f"{product} - ₹{price}")
                total += price

            print(f"Total: ₹{total}")

    elif choice == "4":
        if len(cart) == 0:
            print("\nCart is empty.")
        else:
            print("\n===== YOUR CART =====")

            for i, product in enumerate(cart, 1):
                print(f"{i}. {product} - ₹{products[product]}")

            number = int(input("\nEnter product number to remove: "))

            if 1 <= number <= len(cart):
                removed_product = cart.pop(number - 1)
                print(f"{removed_product} removed from cart.")
            else:
                print("Invalid product number.")

    elif choice == "5":
        if len(cart) == 0:
            print("\nCart is empty.")
        else:
            print("\n===== CHECKOUT =====")

            total = 0

            for product in cart:
                price = products[product]
                print(f"{product} - ₹{price}")
                total += price

            print(f"\nTotal amount: ₹{total}")

            discount = float(input("\nEnter discount percentage: "))

            discount_amount = total * discount / 100
            final_amount = total - discount_amount

            print(f"Discount: ₹{discount_amount}")
            print(f"Final amount: ₹{final_amount}")

            print("\nThank you for shopping!")

    elif choice == "6":
        print("\nThank you for shopping!")
        print()
        break

    else:
        print("Invalid choice")