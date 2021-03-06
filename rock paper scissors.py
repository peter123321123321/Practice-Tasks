import random
from enum import IntEnum
from sys import exit


class Action(IntEnum):
    rock = 0
    paper = 1
    scissors = 2

# asks for users input and then makes it an action returns
def user_selection():
    selection = int(input("Enter an Action(Rock[0], Paper[1] Scissors[2]): "))
    action = Action(selection)
    return action


# asks for computers input and then makes it an action returns
def computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action


# compare actions and print different words based on users and computers input
def find_winner(user_action, computer_action):
    if user_action == computer_action:
        print("You tied!")
    elif user_action == Action.rock:
        if computer_action == Action.paper:
            print("Rock is covered by Paper, You lose!")
        else:
            print("Rock breaks Scissors, You win!")
    elif user_action == Action.paper:
        if computer_action == Action.scissors:
            print("Paper is cut by Scissors, You lose!")
        else:
            print("Paper covers Rock, You win!")
    elif user_action == Action.scissors:
        if computer_action == Action.rock:
            print("Scissors is crushed by Rock, You lose!")
        else:
            print("Scissors cuts Paper, You win!")


# If user selection is not a valid number prints invalid selection asks user to play again if tes loops back to start if no exits program
while True:
    try:
        user_action = user_selection()
    except ValueError as e:
        print("Invalid selection.")
        continue

    computer_action = computer_selection()
    find_winner(user_action, computer_action)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        exit()


# Main Routine
user_selection()
