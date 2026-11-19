num = [int(x) for x in input("Enter a list of numbers (comma-separated): ").split(",")]
num2 = numbers + sorted(num)
print("Combined list:", num2)
print("The last number in the combined list is:", num2.pop())