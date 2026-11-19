fruit = []

for i in range(5):
    name = input("Enter a fruit name: ")
    fruit.append(name)
fruits = set(fruit)

print("Fruits: ", fruits)