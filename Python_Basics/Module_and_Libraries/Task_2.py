# A module to perform string operations.
print("\nA module to perform string operations.")
from string_module import reverse,uppercase,lowercase

text = input("Enter a text: ")

print(f"Original Text: {text}")
print(f"Reverse text: {reverse(text)}")
print(f"Uppercase: {uppercase(text)}")
print(f"Lowercase: {lowercase(text)}")
