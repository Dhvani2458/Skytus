age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
if age >= 18 and marks >= 65:
    print("You are eligible for the program.")
elif age < 18 and marks >= 65:
    print("You are partially eligible for the program.")
else:
    print("You are not eligible for the program.")