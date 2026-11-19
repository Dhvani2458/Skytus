#A Flight class with seat booking functionality
print("\nA Flight class with seat booking functionality")
class Flight:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.booked_seats = 0

    def book_seat(self):
        if self.booked_seats < self.total_seats:
            self.booked_seats += 1
            print("Seat booked successfully")
        else:
            print("No seats available")

    def display(self):
        print(f"Total seats: {self.total_seats}")
        print(f"Booked seats: {self.booked_seats}")
        print(f"Available seats: {self.total_seats - self.booked_seats}")

total_seats = int(input("Enter total number of seats: "))

flight = Flight(total_seats)

number = int(input("How many seats do you want to book? "))

for i in range(number):
    flight.book_seat()

flight.display()
