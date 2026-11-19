value = input("Enter a string: ")
count = {}
for char in value:
    count[char] = count.get(char, 0) + 1
print("Character repetition count: ", count)