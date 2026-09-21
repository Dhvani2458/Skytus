#Handle Division by zero
print("Handle Division by zero")
try:
    num1 =int(input("Enter first number: "))
    num2 = int(input("Enter Second number: "))
    res = num1 / num2
    print(f"{num1} divided by {num2} is : {res}")

except ZeroDivisionError:
    print("Can't divide by zero.")


#Handle invalid Interger Input
print("\nHandle invalid Interger Input.")
try:
    num = int(input("Enter a number: "))
    print("You Entered: ", num)
except ValueError:
    print("Invalid Input.")

#Open file and handle "File not Found"
print("\nOpen File nd Handle 'File not Found Error.'")
try:
    file = open("data.txt", "r")
    file.close()
except FileNotFoundError:
    print("File Not Found. Check the root again.")


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

#Create a custom exception for invalid age (<18)
print("\nCreate a custom exception for invalid age (<18)")
class InvalidAgeError(Exception):
    pass
try:
    age= int(input("Enter your age: "))
    if age < 18:
        raise InvalidAgeError("Age must be above 18.")
    else:
        print("Valid Age.")
except InvalidAgeError as e:
    print(e)

#Handle IndexError when accessing a list
print("\nHandle IndexError when accessing a list.")
num = [10,20,30,40,50]
try:
    index = int(input("Enter an index number: "))
    print("Element: ", num[index])
except IndexError:
    print("Index out of the bound.")
except ValueError:
    print("Please inter a valid index.")

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


#Log errors to a file instead of printing them
print("\nLog errors to a file instead of printing them.")
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a / b)

except Exception as e:
    file = open("error.log", "a")
    file.write(str(e) + "\n")
    file.close()

    print("Error has been logged.")


#Validate email format and raise an exception
print("\nValidate email format and raise an exception.")
class InvalidEmailError(Exception):
    pass


try:
    email = input("Enter your email: ")

    if "@" not in email or "." not in email:
        raise InvalidEmailError("Invalid email format")

    print("Valid email")

except InvalidEmailError as e:
    print(e)