numbers = [int(x) for x in input("Enter a list of numbers (comma-separated): ").split(",")]

ascending_order = sorted(numbers)

print("Original list:", numbers)
print("Sorted list in ascending order:", ascending_order)
