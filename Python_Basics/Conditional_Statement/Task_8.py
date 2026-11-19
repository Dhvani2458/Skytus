#Elctricity bill calculation based on units consumed
units = float(input("\nEnter the number of units consumed for electricity bill: "))
if units <= 100:
    bill = units * 5   
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)  
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
print(f"Your electricity bill is: ${bill:.2f}")
