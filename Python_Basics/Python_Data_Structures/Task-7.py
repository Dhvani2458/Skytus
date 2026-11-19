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
