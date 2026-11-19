#Function to check Armstrong number
def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == n

n = int(input("\nEnter a number to check if it is an Armstrong number: "))
if is_armstrong(n):
    print(f"{n} is an Armstrong number.") 
else:
    print(f"{n} is not an Armstrong number.")