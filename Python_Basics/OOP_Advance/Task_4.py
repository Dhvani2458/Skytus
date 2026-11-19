# Demonstrate multiple inheritance with two parent classes.
print("\nDemonstrate multiple inheritance with two parent classes.") 
class Father:
    def father_info(self):
        print("Father's property")


class Mother:
    def mother_info(self):
        print("Mother's property")


class Child(Father, Mother):
    def child_info(self):
        print("Child's information")


name = input("Enter child's name: ")

child = Child()

print(f"Child: {name}")
child.father_info()
child.mother_info()
child.child_info()
