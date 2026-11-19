#Function to check if a word is a palindrome
def is_palindrome(word):
    return word == word[::-1]

word = input("\nEnter a word to check if it is a palindrome: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
