#Function to calculate simple interest
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

principal = float(input("\nEnter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
print(f"The simple interest is: {simple_interest(principal, rate, time)}")

