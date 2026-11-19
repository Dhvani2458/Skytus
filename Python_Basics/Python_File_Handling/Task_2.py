#Count the number of lines in a file
print("\nCounting the number of lines in a file and displaying it.")
file = open("file1.txt", "r")
lines = file.readlines()
print("Number of lines: ", len(lines))
file.close()

