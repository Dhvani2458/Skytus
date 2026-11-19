#Read a file and print only lines containing a specific word
print("\nRead a file and print only lines containing a specific word.")
file = open("data.txt", "r")
word = input("Enter a word to search: ")

for line in file:
    if word.lower() in line.lower():
        print(line , end="")
file.close()



