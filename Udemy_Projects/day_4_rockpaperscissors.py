# DAY 4 - ROCK PAPER SCISSORS
# Run: python .\Udemy_Projects\day_4_rockpaperscissors.py
# Related: Udemy_Projects\ (no helper files yet)

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]

print("Hello, let's play Rock, Paper, Scissors. See if you can beat me!")
player_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
)

if player_choice < 0 or player_choice > 2:
    print("Wrong input. Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
else:
    print(game_images[player_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {computer_choice}")
    print(game_images[computer_choice])

    if player_choice == computer_choice:
        print("It's a draw!")
    elif player_choice == 0 and computer_choice == 2:
        print("You win!")
    elif player_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif player_choice > computer_choice:
        print("You win!")
    else:
        print("You lose!")
