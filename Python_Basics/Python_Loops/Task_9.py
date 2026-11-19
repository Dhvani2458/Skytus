#Find the sum of digits in a number(1 to 100)
total_sum = 0
for i in range(1, 101):
    total_sum += sum(int(digit) for digit in str(i))
print("\nSum of digits from 1 to 100:", total_sum)

