# A custom math module and import it in another file.
print("\n A custom math module and import it in another file.")
from math_module import add,sub,div,mul,exp,mod

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"Addition: {add(a,b)}")
print(f"Substraction: {sub(a,b)}")
print(f"Multiplication: {mul(a,b)}")
print(f"Division: {div(a,b)}")
print(f"Exponential: {exp(a,b)}")
print(f"Module: {mod(a,b)}")

# A module to perform string operations.
print("\nA module to perform string operations.")
from string_module import reverse,uppercase,lowercase

text = input("Enter a text: ")

print(f"Original Text: {text}")
print(f"Reverse text: {reverse(text)}")
print(f"Uppercase: {uppercase(text)}")
print(f"Lowercase: {lowercase(text)}")

# Use a random module to generate 5 random integers.
print("\nUse a random module to generate 5 random integers.")
import random

min = int(input("Enter Minimum Value: "))
max = int(input("Enter Maximum Value: "))
print("Random Numbers: ")

for i in range(5):
    print(random.randint(min,max))

# Use datetime module to display current date and time.
print("\nUse datetime module to display current date and time.")
import datetime

current = datetime.datetime.now()
print("Date:" , current.strftime("%D-%M-%Y"))
print("Time: ", current.strftime("%H:%M:%S"))

# Use math module to fing factorial of a number.
print("\n Use math module to find factorial of a number.")
import math

num = int(input("Enter a number: "))

if num >= 0:
    print(f"Factorial: {math.factorial(num)}")
else:
    print("Factorial is not defined for negative numbers")


# Create a package shapes with modules for circle and rectangle.
print("\nCreate a package shapes with modules for circle and rectangle.")
from circle import circumference
from rectangle import perimeter
import circle
import rectangle
radius = float(input("Enter circle radius: "))

print(f"Circle area: {circle.area(radius)}")
print(f"Circle circumference: {circumference(radius)}")

length = float(input("\nEnter rectangle length: "))
width = float(input("Enter rectangle width: "))

print(f"Rectangle area: {rectangle.area(length, width)}")
print(f"Rectangle perimeter: {perimeter(length, width)}")


# A program to shuffle a list using module.
print("\nA program to shuffle a list using module.")
import random

numbers = input("Enter numbers separated by space: ").split()

print("Original list:", numbers)

random.shuffle(numbers)

print("Shuffled list:", numbers)


# Aprogram to calcualate the difference between 2 dates.
print("\nAprogram to calcualate the difference between 2 dates.")
from datetime import datetime

date1 = input("Enter first date (DD-MM-YYYY): ")
date2 = input("Enter second date (DD-MM-YYYY): ")

date1 = datetime.strptime(date1, "%d-%m-%Y")
date2 = datetime.strptime(date2, "%d-%m-%Y")

difference = abs(date2 - date1)

print(f"Difference: {difference.days} days")


# Use os module to list files in a directory.
print("\nUse os module to list files in a directory.")
import os

folder = input("Enter folder path: ")

if os.path.exists(folder):
    files = os.listdir(folder)

    print("\nFiles and folders:")

    for item in files:
        print(item)
else:
    print("Directory does not exist")