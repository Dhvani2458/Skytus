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