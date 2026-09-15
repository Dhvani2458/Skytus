## Dictionary in Python
student = {
    "name": "Dhruti Patel",
    "marks": 74 
}

print(f"Student Name: {student['name']}\nObtaining Marks: {student['marks']}")

#Adding new key-value pair to the dictionary
print("\nAdding new key-value pair to the dictionary")
city = input("Enter the City Name: ")

student["city"] = city
print(f"Student Name: {student['name']}\nObtaining Marks: {student['marks']}\nCity: {student['city']}")

#Deleting a key-value pair from the dictionary
print("\nDeleting a key-value pair from the dictionary")    
key = input("Enter the key you want to delete: ")
if key in student:
    del student[key]
    print(f"Key '{key}' has been deleted from the dictionary.")
print(student)

#Merging two dictionaries
student1 = {
    "name": "Dhruti Patel",
    "marks": 74,
}
student2 = {
    "city": "Ahmedabad",
    "age": 20
}
student1.update(student2)
print("\nMerged Dictionary:", student1)

#Checking if a key exists in the dictionary
print("\nChecking if a key exists in the dictionary")
key = input("Enter the key you want to check: ")
if key in student1:
    print(f"Key '{key}' exists in the dictionary.")
else:
    print(f"Key '{key}' does not exist in the dictionary.")


#Count words frequency in a string using dictionary
print("\nCount words frequency in a string using dictionary")
text = input("Enter a string: ")
words = text.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print("Word frequencies:", frequency)


#Find the maximum and minimum values in a dictionary
print("\nFind the maximum and minimum values in a dictionary")
marks = {
    "Dhruti": 74, 
    "Raj": 85, 
    "Priya": 92, 
    "Vikram": 78
}
print("Marks Dictionary:", marks)
highest = max(marks, key=marks.get)
print("Student with highest marks: ", highest," ", marks[highest]," with marks.")

#Reverse key-value pairs in a dictionary
print("\nReverse key-value pairs in a dictionary")
print("Original dictionary:", marks)
reversed_marks = {v: k for k, v in marks.items()}
print("Reversed dictionary:", reversed_marks)


#updating values in a dictionary
print("\nUpdating values in a dictionary")
print("Original dictionary:", marks)
marks["Dhruti"] = 80
print("Updated dictionary:", marks)

#converting a list of tuples into a dictionary
print("\nConverting a list of tuples into a dictionary")
tuple_list = [("Dhruti", 74), ("Raj", 85), ("Priya", 92), ("Vikram", 78)]
print("List of tuples:", tuple_list)
student_dict = dict(tuple_list)
print("Converted dictionary:", student_dict)
