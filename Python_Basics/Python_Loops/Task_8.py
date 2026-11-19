#Count the number of digits in a number
num = int(input("\nEnter a number to count its digits: "))
digit_count = 0
while num > 0:
    num //= 10
    digit_count += 1
print("Number of digits:", digit_count)
