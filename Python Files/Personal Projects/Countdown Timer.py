#As the name implies, this is a countdown timer, and my project to learn some of the libraries Python uses
import time
import os

os.system("clear")

number = int(input("Please Enter a starting time in seconds: "))

for i in reversed(range(0, number + 1)):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600) % 24
    if i == 0:
        print("Time's Up!")
    else:
        print(f"{hours} hours, {minutes} minutes and {seconds} seconds remaining")
        time.sleep(1)
