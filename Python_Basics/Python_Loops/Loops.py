#print numbers from 1 to 10
for i in range(1,11):
    print(i)


#Display multiplication table of a given number
num = int(input("\nEnter a number for multiplication table: "))
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)


#Find factorial of a given number
num = int(input("\nEnter a number to find its factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is", factorial)

#genrate Fibonacci series up to n terms
n_terms = int(input("\nEnter the number to generate Fibonacci series for: "))
n1, n2 = 0, 1
count = 0
if n_terms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence: ")
    while count < n_terms:
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


#Check if a number is prime
num = int(input("\n\nEnter a number to check if it is prime: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")


#Reverse a number series
num = int(input("\nEnter a number to reverse its digits: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = (reversed_num * 10) + digit
    num //= 10
print("Reversed number:", reversed_num)


#Count the number of digits in a number
num = int(input("\nEnter a number to count its digits: "))
digit_count = 0
while num > 0:
    num //= 10
    digit_count += 1
print("Number of digits:", digit_count)


#Find the sum of digits in a number(1 to 100)
total_sum = 0
for i in range(1, 101):
    total_sum += sum(int(digit) for digit in str(i))
print("\nSum of digits from 1 to 100:", total_sum)


#Pyramid Pattern
n = int(input("\nEnter the no. of rows: "))

for i in range(1, n+1):
    for j in range(1, n - i + 1):
        print(" ", end= "")

    for i in range(1, i + 1):
        print("* ", end="" )
    print("")