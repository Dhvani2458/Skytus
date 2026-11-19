#Display multiplication table of a given number
num = int(input("\nEnter a number for multiplication table: "))
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)

