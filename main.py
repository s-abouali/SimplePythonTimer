#Python Countdown and Countup Timer ⏳

import time

Time= int(input("Enter The Time in seconds :"))
Count_Direction= input("Do you want to count up or down?(up, down): ").lower()

if Count_Direction== "up":
    for t in range(0, Time+1):
        seconds= t % 60
        minutes= int(t / 60) % 60
        hours= int(t / 3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
    print("TIME IS UP!!⏳")

elif Count_Direction== "down":
    for t in reversed(range(0, Time+1)):
        seconds = t % 60
        minutes = int(t / 60) % 60
        hours = int(t / 3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
    print("TIME IS UP!!⏳")

else:
    print("Invalid choice! Please enter 'up' or 'down'.")

