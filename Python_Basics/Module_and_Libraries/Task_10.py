# Use os module to list files in a directory.
print("\nUse os module to list files in a directory.")
import os

folder = input("Enter folder path: ")

if os.path.exists(folder):
    files = os.listdir(folder)

    print("\nFiles and folders:")

    for item in files:
        print(item)
else:
    print("Directory does not exist")