#Program that takes two numbers and handles all possible errors
print("\nProgram that takes two numbers and handles all possible errors.")
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result:", result)

except ValueError:
    print("Please enter valid integers")

except ZeroDivisionError:
    print("Cannot divide by zero")

except Exception as e:
    print("Some other error occurred:", e)
