#Use finally for resource cleanup
print("\nUse finally for resource cleanup")
try:
    num1 =int(input("Enter first number: "))
    num2 = int(input("Enter Second number: "))
    res = num1 / num2
    print(f"{num1} divided by {num2} is : {res}")

except ZeroDivisionError:
    print("Can't divide by zero.")

finally:
    print("It had came to an end.")
