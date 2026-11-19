# A custom math module and import it in another file.
print("\n A custom math module and import it in another file.")
from math_module import add,sub,div,mul,exp,mod

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"Addition: {add(a,b)}")
print(f"Substraction: {sub(a,b)}")
print(f"Multiplication: {mul(a,b)}")
print(f"Division: {div(a,b)}")
print(f"Exponential: {exp(a,b)}")
print(f"Module: {mod(a,b)}")








