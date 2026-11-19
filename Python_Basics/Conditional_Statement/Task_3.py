#Traffic light signal
signal = input("\nEnter the traffic light signal (red/yellow/green): ").lower()
if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Get ready to move")  
else:
    print("Go")