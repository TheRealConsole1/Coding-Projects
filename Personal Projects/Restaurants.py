import random
import time
import datetime

        

    
restaurants = {"Fast Food" : ["Wendy's", "Mcdonalds", "Taco Bell", "Burger King", "Chick Fil A", "Sonic", ],
"Sit Down" : ["Olive Garden", "Mugshots", "Texas RoadHouse", "Garcia's", "New Orleans Food and Spirit", "New Orleans Style Seafood", "Four Seasons", "Golden Coral",]}

def fast_food():
    f = True
    while f == True:
        print(random.choice(restaurants["Fast Food"]))
        answer = input("Is this option ok?: ")
        if answer == "y":
            print("Enjoy your food!")
            f = False
            break
        if answer == "n":
            pass
def sit():
    f = True
    while f == True:
        print(random.choice(restaurants["Sit Down"]))
        answer = input("Is this option ok?: ")
        if answer == "y":
            print("Enjoy your food!")
            f = False
        if answer == "n":
            pass
f = True
while f == True:
    choice = input("What are we feeling? ").lower()

    if choice == "fast":
        fast_food()
        break
    elif choice == "sit":
        sit()
        break
    elif choice == "sad":
        ...
    else:
        print("That is not a valid option, Please enter a valid option")
      
    