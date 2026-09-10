from datetime import date

bd = int(input("What is your Birth Date ? "))
bm = int(input("What is your Birth Month ? "))
by = int(input("What is your Birth Year ? "))

today = date.today()
age = today.year - by - ((today.month, today.day) < (bm, bd))
print(f"Your age is {age}")
