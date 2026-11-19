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
