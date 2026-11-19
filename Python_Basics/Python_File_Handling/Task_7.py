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


