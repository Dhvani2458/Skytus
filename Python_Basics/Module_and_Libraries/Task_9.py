# A program to calcualate the difference between 2 dates.
print("\nAprogram to calcualate the difference between 2 dates.")
from datetime import datetime

date1 = input("Enter first date (DD-MM-YYYY): ")
date2 = input("Enter second date (DD-MM-YYYY): ")

date1 = datetime.strptime(date1, "%d-%m-%Y")
date2 = datetime.strptime(date2, "%d-%m-%Y")

difference = abs(date2 - date1)

print(f"Difference: {difference.days} days")
