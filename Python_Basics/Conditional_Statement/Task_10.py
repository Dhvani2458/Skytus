#Check type of triangle (equilateral, isosceles, or scalene)
side1 = float(input("\nEnter the length of the first side of the triangle: "))
side2 = float(input("Enter the length of the second side of the triangle: "))
side3 = float(input("Enter the length of the third side of the triangle: "))
if side1 == side2 == side3:
    print("The triangle is equilateral.")   
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")  