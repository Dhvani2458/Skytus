num = float(input("Enter a decimal number: "))

integer = int(num)
if num - integer >= .5:
    integer += 1

print("The integer part of", num, "is", integer)