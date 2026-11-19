#Function to find GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("\nEnter the first number to find GCD: "))
b = int(input("Enter the second number to find GCD: "))
print(f"The GCD of {a} and {b} is: {gcd(a, b)}")
