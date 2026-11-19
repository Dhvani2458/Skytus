#Handle Division by zero
print("Handle Division by zero")
try:
    num1 =int(input("Enter first number: "))
    num2 = int(input("Enter Second number: "))
    res = num1 / num2
    print(f"{num1} divided by {num2} is : {res}")

except ZeroDivisionError:
    print("Can't divide by zero.")
