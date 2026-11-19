class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))

r = Rectangle(length, width)

print("Area of Rectangle:", r.area())
print("Perimeter of Rectangle:", r.perimeter())