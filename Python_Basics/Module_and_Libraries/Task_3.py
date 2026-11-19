# Use a random module to generate 5 random integers.
print("\nUse a random module to generate 5 random integers.")
import random

min = int(input("Enter Minimum Value: "))
max = int(input("Enter Maximum Value: "))
print("Random Numbers: ")

for i in range(5):
    print(random.randint(min,max))
