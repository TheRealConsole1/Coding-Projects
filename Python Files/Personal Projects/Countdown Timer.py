import time
import os

os.system("clear")

number = int(input("Please Enter a starting time in seconds: "))

for i in reversed(range(0, number + 1)):
    seconds = i % 60
    if i == 0:
        print("Time's Up!")
    else:
        print(f"{i} seconds remaining")
        time.sleep(1)
