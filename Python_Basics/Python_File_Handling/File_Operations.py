#Open file in read mode
print("Opening and reading a file.")
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

#Count the number of lines in a file
print("\nCounting the number of lines in a file and displaying it.")
file = open("file1.txt", "r")
lines = file.readlines()
print("Number of lines: ", len(lines))
file.close()

#Count how many times each word appears in a file
print("\nCounting how many times each word appears in an opened file.")
file = open("data.txt", "r")
text = file.read()
words = text.split()
count = {}

for word in words:
    count[word] = count.get(word, 0) + 1
print(count)
file.close()


#Write 5 user-entered sentences to a file
print("\nWrite 5 user-entered sentences to a file.")
file = open("data.txt", "w")

for i in range(5):
    sentence = input("Enter a sentence: ")
    file.write(sentence + "\n")
file.close()
print("Sentence Saved!")


#Append a list of strings to an existing file
print("\nAppend a list of strings to an existing file.")
file = open("data.txt", "a")
strings = ["Hello", "Python", "Programmers"]

for text in strings:
    file.write(text + "\n")
file.close()


#Read a file and print only lines containing a specific word
print("\nRead a file and print only lines containing a specific word.")
file = open("data.txt", "r")
word = input("Enter a word to search: ")

for line in file:
    if word.lower() in line.lower():
        print(line , end="")
file.close()


#Replace a specific word and save the changes
print("\nReplace a specific word and save the changes")
file = open("data.txt", "r")
text = file.read()
replace = input("Enter the word it replace: ")
new_word= input("Enter the new word: ")
text = text.replace(replace, new_word)
file.close()

file = open("data.txt", "w")
file.write(text)
file.close()

print("FIle Uploaded.")


#Read a CSV file and display its content in formatted way
print("\nRead a CSV file and display its content in formatted way.")
import csv
file = open("student.csv", "r")
reader = csv.reader(file)

for row in reader:
    print(f"Name: {row[0]}, Marks: {row[1]}, City: {row[2]}")
file.close()


#Back up a file by copying its contents into another file
print("\nBack up a file by copying its contents into another file.")
file1 = open("data.txt", "r")
file2 = open("backup.txt", "w")
file2.write(file1.read())
file1.close()
file2.close()

print("Backup Created.")