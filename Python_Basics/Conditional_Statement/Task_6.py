#Check a number if it lies within a given range
max = float(input("\nEnter your maximum range: "))
min = float(input("Enter your minimum range: "))
num = float(input("Enter your range: "))
if min <= num <= max:
    print("The number lies within the range.")
else:
    print("The number does not lie within the range.")
