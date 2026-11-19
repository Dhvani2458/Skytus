#Function to find area of a rectangle
def area_of_rectangle(length, width):
    return length * width

length = float(input("\nEnter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print(f"The area of the rectangle is: {area_of_rectangle(length, width)}")
