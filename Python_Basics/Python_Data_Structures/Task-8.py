#Reverse key-value pairs in a dictionary
print("\nReverse key-value pairs in a dictionary")
print("Original dictionary:", marks)
reversed_marks = {v: k for k, v in marks.items()}
print("Reversed dictionary:", reversed_marks)
