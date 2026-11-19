#Open file in read mode
print("Opening and reading a file.")
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()