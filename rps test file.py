def score():
    score_1 = 0
    score_2 = 0


def main_program():
    confirm = str(input("Do you want to play a game(Y/N): ")).upper()
    if confirm == "Y":
        user_input = str(input("Choose an action(Rock, Paper, Scissors): ")).upper()
        if user_input == "ROCK":
            rock()
        if user_input == "SCISSORS":
            scissors()
        if user_input == "PAPER":
            paper()


def rock(score_):
    import random
    score_1 = 0
    score_2 = 0
    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(possible_actions)
    if computer_action == "SCISSORS":
        print("Computer chose Scissors")
        print("Rock beats Scissors, You win!")
        score_1 += 1
        print(f"you {score_1}, computer {score_2}")
        main_program()
    elif computer_action == "Rock":
        print("Computer chose Rock")
        print("You tied")
        main_program()
    else:
        print("Computer chose Paper")
        print("Paper beats Rock, You lose!")
        score_2 += 1
        print(f"you {score_1}, computer {score_2}")
        return main_program()


def paper():
    import random
    score_1 = 0
    score_2 = 0
    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(possible_actions)
    if computer_action == "ROCK":
        print("Computer chose Rock")
        print("Paper beats Rock, You win!")
        score_1 += 1
        print(f"you {score_1}, computer {score_2}")
        main_program()
    elif computer_action == "Paper":
        print("Computer chose Paper")
        print("You tied")
        main_program()
    else:
        print("Computer chose Scissors")
        print("Scissors beats Paper, You lose!")
        score_2 += 1
        print(f"you {score_1}, computer {score_2}")
        main_program()


def scissors():
    import random
    score_1 = 0
    score_2 = 0
    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(possible_actions)
    if computer_action == "PAPER":
        print("Computer chose Paper")
        print("Scissors beats Paper, You win!")
        score_1 += 1
        print(f"you {score_1}, computer {score_2}")
        main_program()
    elif computer_action == "scissors":
        print("Computer chose Scissors")
        print("You tied")
        main_program()
    else:
        print("Computer chose Rock")
        print("Rock beats Scissors, You lose!")
        score_2 += 1
        print(f"you {score_1}, computer {score_2}")
        main_program()


# Main Routine
main_program()
