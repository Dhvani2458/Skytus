#Genrate Fibonacci series up to n terms
n_terms = int(input("\nEnter the number to generate Fibonacci series for: "))
n1, n2 = 0, 1
count = 0
if n_terms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence: ")
    while count < n_terms:
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
