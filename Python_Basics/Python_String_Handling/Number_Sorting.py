
numbers = [int(x) for x in input("Enter a list of numbers (comma-separated): ").split(",")]

ascending_order = sorted(numbers)

print("Original list:", numbers)
print("Sorted list in ascending order:", ascending_order)
print("Reverse order:", ascending_order[::-1])
print("The largest number is:", max(numbers))

num = [int(x) for x in input("Enter a list of numbers (comma-separated): ").split(",")]
num2 = numbers + sorted(num)
print("Combined list:", num2)
print("The last number in the combined list is:", num2.pop())
