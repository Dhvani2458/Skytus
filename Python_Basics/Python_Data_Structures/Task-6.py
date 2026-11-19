#Count words frequency in a string using dictionary
print("\nCount words frequency in a string using dictionary")
text = input("Enter a string: ")
words = text.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print("Word frequencies:", frequency)
