# Program to demonstrate the use of set in Python
fruit = []

for i in range(5):
    name = input("Enter a fruit name: ")
    fruit.append(name)
fruits = set(fruit)

print("Fruits: ", fruits)

print("Want to add more fruits? (yes/no): ")
if input().lower() == "yes":
    name = input("Enter a fruit name: ")
    fruits.add(name)
    print("Fruits: ", fruits)
else: 
    print("Fruits: ", fruits)

print("Want to remove a fruit? (yes/no): ")
if input().lower() == "yes":
    name = input("Enter a fruit name: ")
    fruits.remove(name)
    print("Fruits: ", fruits)
else:
    print("Fruits: ", fruits)

# Demonstrating set operations in Python
set1 = {1,8,6,7,2}
set2 = {9,5,6,8,7}

print("Set1: ", set1)
print("Set2: ", set2)

s1= set1.union(set2)
s2= set1.intersection(set2)

print("Union of Set1 and Set2: ", s1)
print("Intersection of Set1 and Set2: ", s2)

if set1.issubset(set2):
    print("Set1 is a subset of Set2")
else:
    print("Set1 is not a subset of Set2")

num = [1,2,2,5,7,7,8,9,9]
print("New Set is: ", num)
unique = set(num)
print("Unique elements in the new set: ", unique)