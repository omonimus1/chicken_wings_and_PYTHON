# Author: Davide
# Date: 01/12/2019

# Source of the brilliant Asci Art -> https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe

import random as rand
import sys
from typing import Any, Union


def computer_move():
    a = 1
    b = 3
    computer_choose = generate_computer_choose(a, b)
    print_hand(computer_choose)
    return computer_choose


def user_move():
    a = 1
    b = 3
    print("Choose an option between 1 and 3 where:")
    print("1- Paper")
    print("2 - Rock")
    print("3- Scissor")
    print("Press any other key to stop the application")
    user_choose = int(input("Choose: "))
    if 1 <= user_choose <= 3:
        print_hand(user_choose)
        return user_choose
    else:
        print("Goodbye")
        # Stop the application
        sys.exit(0)


def print_hand(choose):
    if choose == 1:
        print_paper()
    elif choose == 2:
        print_rock()
    else:
        print_scissor()
    return


def print_paper():
    # Paper
    print("""
         _______
    ---'    ____)____
               _______)
              ________)
             ________)
    ---.___________)
    """)
    return


def print_rock():
    # Rock
    print("""
        _______
    ---'   ___)
          (____)
          (____)
          (___)
    ---.__(__)
    """)
    return


def print_scissor():
    # Scissors
    print("""
        _______
    ---'   ___)____
              _____)
           _________)
          (___)
    ---.__(__)
    """)
    return


def generate_computer_choose(a, b):
    # Create a random integer between 1 and 3, that is going to be the options for the game.
    computer_choose = rand.randint(a, b)
    return computer_choose


def get_winner(user_choose, computer_choose):
    # Get the winner of the game.
    if user_choose == computer_choose:
        return "nobody"
    if user_choose == 1:
        if computer_choose == 2:
            return "user"
        else:
            return "computer"
    elif user_choose == 2:
        if computer_choose == 1:
            return "computer"
        else:
            return "user"
    else:
        if computer_choose == 1:
            return "user"
        else:
            return "computer"


def print_winner(wi):
    if wi == "nobody":
        print("Nobody won")
        return
    elif wi == "user":
        print("User won")
        return
    else:
        print("Computer won")
        return


# Core of the program
while 1:
    user_option = user_move()
    computer_option = computer_move()
    winner = get_winner(user_option, computer_option)
    print_winner(winner)
