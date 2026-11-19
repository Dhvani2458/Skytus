#Pyramid Pattern
n = int(input("\nEnter the no. of rows: "))

for i in range(1, n+1):
    for j in range(1, n - i + 1):
        print(" ", end= "")

    for i in range(1, i + 1):
        print("* ", end="" )
    print("")