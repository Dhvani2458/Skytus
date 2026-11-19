# Use datetime module to display current date and time.
print("\nUse datetime module to display current date and time.")
import datetime

current = datetime.datetime.now()
print("Date:" , current.strftime("%D-%M-%Y"))
print("Time: ", current.strftime("%H:%M:%S"))
