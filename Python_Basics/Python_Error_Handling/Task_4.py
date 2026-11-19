#Demonstrate multiple exception block
print("\nDemonstrate multiple exception block.")
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a / b
    print(c)
except ValueError:
    print("Check the value it must be an Integer only.")
except ZeroDivisionError:
    print("Can't divide any number by zero.")
