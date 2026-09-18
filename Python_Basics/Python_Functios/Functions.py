#Function to check if n is a prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("\nEnter a number to check if it is prime: "))
if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")


#Function to reverse a string
def reverse_string(s):
    return s[::-1]  

s = input("\nEnter a string to reverse: ")
print(f"The reversed string is: {reverse_string(s)}")


#Function to calculate the factorial of a number
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
n = int(input("\nEnter a number to calculate its factorial: "))
print(f"The factorial of {n} is: {factorial(n)}")


#Function to calculate simple interest
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

principal = float(input("\nEnter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
print(f"The simple interest is: {simple_interest(principal, rate, time)}")


#Function to check if a word is a palindrome
def is_palindrome(word):
    return word == word[::-1]

word = input("\nEnter a word to check if it is a palindrome: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")


#Function to count vowels in a string
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
   
s = input("\nEnter a string to count vowels: ")
print(f"The number of vowels in '{s}' is: {count_vowels(s)}")


#Function to merge two lists
def merge_lists(list1, list2):
    return list1 + list2

list1 = input("\nEnter the first list (comma-separated): ").split(',')
list2 = input("Enter the second list (comma-separated): ").split(',')
print(f"The merged list is: {merge_lists(list1, list2)}")


#Function to find GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("\nEnter the first number to find GCD: "))
b = int(input("Enter the second number to find GCD: "))
print(f"The GCD of {a} and {b} is: {gcd(a, b)}")


#Function to find area of a rectangle
def area_of_rectangle(length, width):
    return length * width

length = float(input("\nEnter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print(f"The area of the rectangle is: {area_of_rectangle(length, width)}")


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