# Program to demonstrate the use of tuples in Python
nums = []

for i in range(5):
    num = int(input("Enter a number: "))
    nums.append(num)
number = tuple(nums)

print("Tuples: ", number)
print("The third element of the tuple is:  ", number[2])

## Unpacking a tuple in Python
person = ("Raj", 24, "Navsari")
name,age,city = person

print("Name: ", name)
print("Age: ", age)
print("City: ", city)