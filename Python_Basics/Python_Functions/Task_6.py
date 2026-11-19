#Function to count vowels in a string
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
   
s = input("\nEnter a string to count vowels: ")
print(f"The number of vowels in '{s}' is: {count_vowels(s)}")

