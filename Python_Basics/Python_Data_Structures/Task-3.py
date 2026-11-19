#Deleting a key-value pair from the dictionary
print("\nDeleting a key-value pair from the dictionary")    
key = input("Enter the key you want to delete: ")
if key in student:
    del student[key]
    print(f"Key '{key}' has been deleted from the dictionary.")
print(student)
