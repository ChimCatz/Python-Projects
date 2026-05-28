# DAY 12 - GUESS THE NUMBER
# Run: python .\Udemy_Projects\day_12_guessthenumber.py
# Related: Udemy_Projects\ (no helper files yet)

import random

logo = r"""
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

def check_guess(number_guess, random_number, attempts_count):
    if number_guess > random_number:
        print("Too high.\nGuess again.")
        return attempts_count - 1
    elif number_guess < random_number:
        print("Too low.\nGuess again.")
        return attempts_count - 1
    else:
        print(f"You got it! The answer was {random_number}.")
        return attempts_count

def play_game():
    random_number = random.randint(1, 100)
    attempts_count = 0

    print(logo)
    print(
        "Welcome to ChiggaHaxlord's Number Guessing Game!\n"
        "I'm thinking of a number between 1 and 100.\n"
    )

    game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if game_difficulty == "easy":
        attempts_count = 10
        print("You choose EASY mode. You have 10 attempts remaining to guess the number.")
    elif game_difficulty == "hard":
        attempts_count = 5
        print("You are on HARD mode. You only have 5 attempts remaining to guess the number.")
    else:
        print("Invalid difficulty! Please type 'easy' or 'hard'.")
        return

    game_over = False
    while not game_over:
        print(f"You have {attempts_count} attempts remaining to guess the number.")
        number_guess = int(input("Make a guess: "))
        updated_attempts = check_guess(number_guess, random_number, attempts_count)

        if number_guess == random_number:
            game_over = True
        else:
            attempts_count = updated_attempts
            if attempts_count == 0:
                game_over = True
                print(
                    f"You lose! You ran out of guesses. The correct answer was {random_number}."
                )

while input("Do you want to play a round of Guess Number Game? Type 'y' or 'n': ") == "y":
    play_game()
