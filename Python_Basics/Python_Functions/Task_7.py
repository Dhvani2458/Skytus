#Function to merge two lists
def merge_lists(list1, list2):
    return list1 + list2

list1 = input("\nEnter the first list (comma-separated): ").split(',')
list2 = input("Enter the second list (comma-separated): ").split(',')
print(f"The merged list is: {merge_lists(list1, list2)}")

