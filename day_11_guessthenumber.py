import random

logo = """
   _____                       _   _            _   _                 _               
  / ____|                     | | | |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|                                                                                                           
"""
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
randomNumber = random.randint(1,100)
attemptsCount = 0
continueGame = True

def guess_number():
    global randomNumber
    global attemptsCount
    global continueGame
    if attemptsCount != 0:
        number_guess = int(input("Make a guess: "))
        if number_guess > randomNumber:
            attemptsCount -= 1
            print("Too high. \nGuess again.")
            print(f"You have {attemptsCount} attempts remaining to guess the number.")
        elif number_guess < randomNumber:
            print("Too low. \nGuess again.")
            attemptsCount -= 1
            print(f"You have {attemptsCount} attempts remaining to guess the number.")
        else:
            print(f"You got it! The answer was {randomNumber}")
            continueGame = False
            return
    else:
        continueGame = False
        print(f"You lose! You run out of guesses! The corrent answer is {randomNumber}")

def play_game():
    global randomNumber
    global attemptsCount
    global continueGame
    print(logo)
    print(f"Welcome to ChiggaHaxlord's Number Guessing Game!\n"
          f"I'm thinking of a number between 1 and 100.\n"
          )

    gameDifficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if gameDifficulty == "easy":
        attemptsCount = 10
        print("You choose EASY mode. You have 10 attempts remaining to guess the number.")
    elif gameDifficulty == "hard":
        attemptsCount = 5
        print("You are on HARD mode. You only have 5 attempts remaining to guess the number.")
    else:
        print("Invalid difficulty! Please type 'easy' or 'hard'")

    while continueGame:
        guess_number()

while input("Do wou want to play a round of Guess Number Game? Type 'y' or 'n': ") == "y":
    play_game()
