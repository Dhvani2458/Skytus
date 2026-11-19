# Create a package shapes with modules for circle and rectangle.
print("\nCreate a package shapes with modules for circle and rectangle.")
from circle import circumference
from rectangle import perimeter
import circle
import rectangle
radius = float(input("Enter circle radius: "))

print(f"Circle area: {circle.area(radius)}")
print(f"Circle circumference: {circumference(radius)}")

length = float(input("\nEnter rectangle length: "))
width = float(input("Enter rectangle width: "))

print(f"Rectangle area: {rectangle.area(length, width)}")
print(f"Rectangle perimeter: {perimeter(length, width)}")
