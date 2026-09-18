#Eligible or not for voting
age = int(input("\nEnter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


#Grade based on marks
marks = int(input("\nEnter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
else:
    print("Grade: C")


#Traffic light signal
signal = input("\nEnter the traffic light signal (red/yellow/green): ").lower()
if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Get ready to move")  
else:
    print("Go")


#Check balance in bank account
balance = float(input("\nEnter your bank account balance: "))
if balance >= 1000:
    print("You have sufficient balance.")   
else:
    print("You have insufficient balance.")


#Check if a number is positive, negative, or zero
number = float(input("\nEnter a number: "))
if number == 0:
    print("The number is zero.")
elif number > 0:
    print("The number is positive.")
else:
    print("The number is negative.")    


#Check a number if it lies within a given range
max = float(input("\nEnter your maximum range: "))
min = float(input("Enter your minimum range: "))
num = float(input("Enter your range: "))
if min <= num <= max:
    print("The number lies within the range.")
else:
    print("The number does not lie within the range.")


#Username and password verification
username = input("\nEnter your username: ")
password = input("Enter your password: ")
if username == "admin" and password == "password123":
    print("Login successful.")
else:
    print("Invalid username or password.")


#Elctricity bill calculation based on units consumed
units = float(input("\nEnter the number of units consumed for electricity bill: "))
if units <= 100:
    bill = units * 5   
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)  
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
print(f"Your electricity bill is: ${bill:.2f}")


#Simple calculator based on user input
num1 = float(input("\nEnter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2    
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operation"    
print(f"The result is: {result}")


#Check type of triangle (equilateral, isosceles, or scalene)
side1 = float(input("\nEnter the length of the first side of the triangle: "))
side2 = float(input("Enter the length of the second side of the triangle: "))
side3 = float(input("Enter the length of the third side of the triangle: "))
if side1 == side2 == side3:
    print("The triangle is equilateral.")   
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")   