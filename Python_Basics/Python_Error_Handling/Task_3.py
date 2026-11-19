#Open file and handle "File not Found"
print("\nOpen File nd Handle 'File not Found Error.'")
try:
    file = open("data.txt", "r")
    file.close()
except FileNotFoundError:
    print("File Not Found. Check the root again.")
