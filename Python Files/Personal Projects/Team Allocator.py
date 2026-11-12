import random

names = [
    "Oliver Bennett",
    "Amelia Carter",
    "Ethan Brooks",
    "Sophia Mitchell",
    "Lucas Hayes",
    "Isabella Foster",
    "Mason Reed",
    "Charlotte Parker",
    "Elijah Morgan",
    "Harper Collins",
    "Noah Sullivan",
    "Evelyn Brooks",
    "Caleb Anderson",
    "Victoria James",
    "Adrian Cooper",
    "Scarlett Bailey",
    "Julian Hayes",
    "Madeline Ross",
    "Theodore Price",
    "Natalie Bennett"
]
random.shuffle(names)
team_1 = names[:len(names) // 2]
captain_1 = random.choice(team_1)
team_2 = names[len(names) // 2:]
captain_2 = random.choice(team_2)
print("Team one is: ")
for names in team_1:
    print(names)
print("---------------")
print("Team two is: ")
for names in team_2:
    print(names)