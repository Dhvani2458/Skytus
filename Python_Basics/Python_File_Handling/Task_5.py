#Append a list of strings to an existing file
print("\nAppend a list of strings to an existing file.")
file = open("data.txt", "a")
strings = ["Hello", "Python", "Programmers"]

for text in strings:
    file.write(text + "\n")
file.close()


