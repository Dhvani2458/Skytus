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

