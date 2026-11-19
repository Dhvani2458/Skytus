element = int(input("Enter a number to search for: "))
print(f"{element} is present {sum(row.count(element) for row in num)} times in the nested list.")