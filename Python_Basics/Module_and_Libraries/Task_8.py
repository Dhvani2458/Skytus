# A program to shuffle a list using module.
print("\nA program to shuffle a list using module.")
import random

numbers = input("Enter numbers separated by space: ").split()

print("Original list:", numbers)

random.shuffle(numbers)

print("Shuffled list:", numbers)
