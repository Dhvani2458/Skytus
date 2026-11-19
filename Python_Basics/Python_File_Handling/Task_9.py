#Read a CSV file and display its content in formatted way
print("\nRead a CSV file and display its content in formatted way.")
import csv
file = open("student.csv", "r")
reader = csv.reader(file)

for row in reader:
    print(f"Name: {row[0]}, Marks: {row[1]}, City: {row[2]}")
file.close()
