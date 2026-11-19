movie = input("Enter your 5 favourite movies (comma-separated): ").split(",")
print("Your favourite movies are:")

print("Want to add more movies? (yes/no)")
if input().lower() == "yes":
    additional_movies = input("Enter additional movies (comma-separated): ").split(",")
    movie.extend(additional_movies)
    print("Your updated movie list is:", movie) 
