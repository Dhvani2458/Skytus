#Back up a file by copying its contents into another file
print("\nBack up a file by copying its contents into another file.")
file1 = open("data.txt", "r")
file2 = open("backup.txt", "w")
file2.write(file1.read())
file1.close()
file2.close()

print("Backup Created.")