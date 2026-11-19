# Use math module to fing factorial of a number.
print("\n Use math module to find factorial of a number.")
import math

num = int(input("Enter a number: "))

if num >= 0:
    print(f"Factorial: {math.factorial(num)}")
else:
    print("Factorial is not defined for negative numbers")

