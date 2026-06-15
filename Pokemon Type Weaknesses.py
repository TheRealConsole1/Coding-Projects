valid_types = {
    "normal", "fire", "water", "electric", "grass", "ice",
    "fighting", "poison", "ground", "flying", "psychic",
    "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"
}
pokemon_type = input("What is the Pokemon Type(s): ")
while pokemon_type not in valid_types:
    print("Invalid Typing. Please enter a valid Pokemon type: ")
    pokemon_type = input("What is the Pokemon type: ").strip().lower()
if pokemon_type == "normal":
    print("Normal isn't strong against anything, though they are immune to ghost type moves")
elif pokemon_type == "fire":
    print("Fire is strong against Grass, Ice, Bug, and Steel")
elif pokemon_type == "water":
    print("Water is strong against Fire, Ground, and Rock")
elif pokemon_type == "electric":
    print("Electric is strong against Water and Flying")
elif pokemon_type == "grass":
    print("Grass is strong against Water, Ground, and Rock")
elif pokemon_type == "poison":
    print("Poison is strong against Grass and Fairy")
elif pokemon_type == "ice":
    print("Ice is strong against    Grass, Ground, Flying, and Dragon")
elif pokemon_type == "fighting":
    print("Fighting is strong against Normal, Ice, Rock, Dark, and Steel")
elif pokemon_type == "ground":
    print("Ground is strong against Fire, Electric, Poison, Rock, and Steel")
elif pokemon_type == "flying":
    print("Flying is strong against Grass, Fighting, and Bug")
elif pokemon_type == "psychic":
    print("Pyschic is strong against Fighting and Poison")
elif pokemon_type == "bug":
    print("Bug is strong against Grass, Psychic, and Dark")
elif pokemon_type == "rock":
    print("Rock is strong against Fire, Ice, Flying, and Bug")
elif pokemon_type == "ghost":
    print("Ghost is strong against Psychic and Itself")
elif pokemon_type == "dragon":
    print("Dragon is strong against Itself")
elif pokemon_type == "dark":
    print("Dark is strong against Psychic and Ghost")
elif pokemon_type == "steel":
    print("Steel is strong against Ice, Rock, and Fairy")
elif pokemon_type == "fairy":
    print("Fairy is strong against Fighting, Dragon, and Dark")
else:
    print("That is an invalid typing. Please input a pokemon type: ")
