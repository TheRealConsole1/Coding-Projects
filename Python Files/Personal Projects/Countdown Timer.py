#As the name implies, this is a countdown timer, and my project to learn some of the libraries Python uses
import time #Imports the time module into the python script, which lets you use its functions
import os #imports the OS module into the Python script, which let's you use its functions

os.system("clear") #When run, this clears the terminal window of all text

number = int(input("Please Enter a starting time in seconds: ")) #An input function that takes the users input as seconds

for i in reversed(range(0, number + 1)): #This is a for loop that runs the main countdown. as it goes from the number the user input, back down to 0
    seconds = i % 60 #A simple equation to calculate seconds if the time is less than 60, if it is more than 60, it will divide the number, and give the time in minutes/seconds
    minutes = int(i / 60) % 60 
    hours = int(i / 3600) % 24
    if i == 0:
        print("Time's Up!")
    else:
        print(f"{hours} hours, {minutes} minutes and {seconds} seconds remaining")
        time.sleep(1)
