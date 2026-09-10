num = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(num[1][0])

num = [list(map(int, input("Enter a sequence of numbers (comma-separated): ").split(",")))]
element = int(input("Enter a number to search for: "))
print(f"{element} is present {sum(row.count(element) for row in num)} times in the nested list.")