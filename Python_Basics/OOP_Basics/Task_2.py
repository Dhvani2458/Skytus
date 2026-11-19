#Create a Banking Account class with deposite and withdrawl method
print("\nCreate a Banking Account class with deposite and withdrawl method.")
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawl(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance.")

    def display(self):
        print(f"Balance: {self.balance}")

balance = float(input("Enter initial balance: "))

account = BankAccount(balance)

deposit = float(input("Enter deposit amount: "))
account.deposit(deposit)

withdraw = float(input("Enter withdrawal amount: "))
account.withdrawl(withdraw)

account.display()

