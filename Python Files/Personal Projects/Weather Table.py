#To run this program, click the run button in the top left
import random
weather_types = ["Drizzle", "Light Rain", 'Heavy Rain', 'Thunderstorm', 'Lightning Storm', 'Tornado', 'Hail', 'Snow', 'Sleet', 'Blizzard', 'Sunny', 'Hot', 'Warm', 'Cold', 'Freezing']
def rand(answer):
    while True:
            print(random.choice(weather_types))
            check = input("Is this option ok?: ").lower().strip()
            if check == "y":
                return False
            if check =="n":
                 pass
def choice(answer):
        print(weather_types)
answer = input("Whould you like to choose or let fate decide?: ")

if answer == 'choose':
    choice(answer)
if answer == 'random':
    rand(answer)
