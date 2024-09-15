"""
    Author: BENEDICT KARIUKI M.
    Date: September 15, 2024
    Description: A simple Rock, Paper, Scissors game where a user plays against the computer.
             The game follows traditional rules, and the result is displayed after each round.
"""
# Instructions:
# 1. Run the script.
# 2. Input your choice (Rock, Paper, or Scissors).
# 3. The computer will randomly select a choice.
# 4. The winner will be displayed based on the rules.


import random

print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

print("Enter your choice\n"
      "1 - Rock\n"
      "2 - Paper\n"
      "3 - Scissors")
user_choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
while True:
    choice = int(input("Enter your choice: "))
    print(f"User choice is: \033[92m{user_choices[choice]}\033[0m")
    print("Now it's computer's turn...")
    # a dict of the remaining two choices
    computer_choices = {key: value for key, value in user_choices.items() if key != choice}
    computer = random.choice(list(computer_choices.keys()))
    print(f"Computers choice is: \033[92m{computer_choices[computer]}\033[0m")
    print(f"{user_choices[choice]} vs {computer_choices[computer]}")
    win = 0
    # if you chose 1 and the computer chose 2, or vice versa, 2 won
    if (choice == 1 and computer == 2) or (computer == 1 and choice == 2):
        win = 2
    # if you chose 1 and the computer chose 3, or vice versa,  1 won
    elif (choice == 1 and computer == 3) or (computer == 1 and choice == 3):
        win = 1
    # if you chose 2 and the computer chose 3, or vice versa, 3 won
    elif (choice == 2 and computer == 3) or (computer == 2 and choice == 3):
        win = 3

    # compare the win with what user chose
    if win == choice:
        print("\033[92mCongratulations! You Won.\033[0m")
    else:
        print("\033[91mComputer Won!\033[0m")

    play = input("Do you want to play again? (Y/N)").lower()
    if play != 'y':
        break



