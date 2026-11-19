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

