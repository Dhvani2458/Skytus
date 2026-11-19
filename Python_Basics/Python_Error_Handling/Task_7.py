#Handle IndexError when accessing a list
print("\nHandle IndexError when accessing a list.")
num = [10,20,30,40,50]
try:
    index = int(input("Enter an index number: "))
    print("Element: ", num[index])
except IndexError:
    print("Index out of the bound.")
except ValueError:
    print("Please inter a valid index.")
