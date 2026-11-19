#Handle invalid Interger Input
print("\nHandle invalid Interger Input.")
try:
    num = int(input("Enter a number: "))
    print("You Entered: ", num)
except ValueError:
    print("Invalid Input.")
