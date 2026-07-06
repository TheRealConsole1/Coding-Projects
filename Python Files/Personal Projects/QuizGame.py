import time
questions = ("When did America Declare it's independece?",
             "What console did the first Luigi's Mansion come out on?",
             "What day was the New York Terror Attacks in 2001?>",
             "What Element on the Periodic Table is #1?",
             "Which animal lays the largest eggs?"
)

options = (("A. 1776", "B. 1952 ", "C. 2026 " , "D. 1876 "),
           ("A. Wii U", "B. Xbox One ", "C. Gamecube" , "D.  Switch"),
           ("A. September 28th", "B.  September 11th", "C. September 21st" , "D.  September 1st"),
           ("A. Hydrogen ", "B. Oxygen ", "C. Helium " , "D. Uranium"),
           ("A. Ostrich", "B. Platypus", "C. Frog" , "D. Duck"))

answers = ("A", "C", "B", "A", "A",)
guesses = []
score = 0
question_num = 0
print("Welcome to Ash's Amazing Answering Announcement!")
time.sleep(2)
print("Today, we have some questions for you, and you have to do your best to answer them.")
time.sleep(2)
print("Let's get started with our first question!")
time.sleep(2)
for question in questions:
    print("-----------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    if guess == answers[question_num]:
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("You guessed the correct answer!")
        else:
            print("You guessed the incorrect answer!")
            print(f"(answer was {answers[question_num]})")
    question_num += 1
    percentage_score = score / (len(questions) )* 100
print("-----------------------------------------------")
print("                   RESULTS                         ")
print(f"    Your final score was {score} out of {len(questions)}")
print(f"    Resulting in a final score of {percentage_score}%")
print("-----------------------------------------------")


