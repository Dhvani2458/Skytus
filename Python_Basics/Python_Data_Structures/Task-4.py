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
