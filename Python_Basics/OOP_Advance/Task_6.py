# Create a Bank system with Savings Account and CurrentAccount classes.
print("\nCreate a Bank system with Savings Account and CurrentAccount classes.")  
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def display(self):
        print(f"Balance: ₹{self.balance}")


class SavingsAccount(BankAccount):
    def add_interest(self):
        interest = self.balance * 0.05
        self.balance += interest


class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        self.balance -= amount


choice = input("Enter account type (savings/current): ").lower()
balance = float(input("Enter initial balance: "))

if choice == "savings":
    account = SavingsAccount(balance)
    account.add_interest()
    account.display()

elif choice == "current":
    account = CurrentAccount(balance)

    amount = float(input("Enter withdrawal amount: "))

    if amount <= account.balance:
        account.withdraw(amount)
        account.display()
    else:
        print("Insufficient balance")

else:
    print("Invalid account type")
