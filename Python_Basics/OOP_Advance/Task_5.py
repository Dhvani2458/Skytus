# Create a polymorphic function that works with different shapes.
print("\nCreate a polymorphic function that works with different shapes.")  
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


def print_area(shape):
    print(f"Area: {shape.area()}")


choice = input("Enter shape (circle/rectangle): ").lower()

if choice == "circle":
    radius = float(input("Enter radius: "))
    shape = Circle(radius)

elif choice == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    shape = Rectangle(length, width)

else:
    print("Invalid shape")
    shape = None

if shape:
    print_area(shape)
