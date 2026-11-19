fruit = []

for i in range(5):
    name = input("Enter a fruit name: ")
    fruit.append(name)
fruits = set(fruit)

print("Fruits: ", fruits)

print("Want to remove a fruit? (yes/no): ")
if input().lower() == "yes":
    name = input("Enter a fruit name: ")
    fruits.remove(name)
    print("Fruits: ", fruits)
else:
    print("Fruits: ", fruits)
