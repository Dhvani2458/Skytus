#Write 5 user-entered sentences to a file
print("\nWrite 5 user-entered sentences to a file.")
file = open("data.txt", "w")

for i in range(5):
    sentence = input("Enter a sentence: ")
    file.write(sentence + "\n")
file.close()
print("Sentence Saved!")


