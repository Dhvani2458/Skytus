movie = input("Enter your 5 favourite movies (comma-separated): ").split(",")
print("Your favourite movies are:")

print("Want to remove any movies? (yes/no)")
if input().lower() == "yes":
        movie.pop(0)
        print("Your updated movie list is:", movie)
else:
        print("Your movie list remains unchanged:", movie)