def main_program():
    import random
    score_1 = 0
    score_2 = 0
    count = 0
    limit = int(input("how many games do you want to play"))
    while count != limit:
        possible_actions = ["Rock", "Paper", "Scissors"]
        computer_action = random.choice(possible_actions)
        user_input = str(input("Choose an action(Rock, Paper, Scissors): ")).upper()
        if user_input == computer_action:
            print("It's a tie!")
            count += 1
            print(f"you {score_1}, computer {score_2}")
        elif user_input == "ROCK":
            if computer_action == "SCISSORS":
                print("Computer chose Scissors")
                print("Rock beats Scissors, You win!")
                count += 1
                score_1 += 1
                print(f"you {score_1}, computer {score_2}")
            else:
                print("Computer chose Paper")
                print("Paper beats Rock, You lose!")
                count += 1
                score_2 += 1
                print(f"you {score_1}, computer {score_2}")
        elif user_input == "PAPER":
            if computer_action == "ROCK":
                print("Computer chose Rock")
                print("Paper beats Rock, You win!")
                count += 1
                score_1 += 1
                print(f"you {score_1}, computer {score_2}")
            else:
                print("Computer chose Scissors")
                print("Scissors beats Paper, You lose!")
                count += 1
                score_2 += 1
                print(f"you {score_1}, computer {score_2}")
        elif user_input == "SCISSORS":
            if computer_action == "PAPER":
                print("Computer chose Paper")
                print("Scissors beats Paper, You win!")
                count += 1
                score_1 += 1
                print(f"you {score_1}, computer {score_2}")
            else:
                print("Computer chose Rock")
                print("Rock beats Scissors, You lose!")
                count += 1
                score_2 += 1
                print(f"you {score_1}, computer {score_2}")
    if count == limit:
        if user_input == computer_action:
            print(f"you won {score_1} games, computer won {score_2} games!")
            print("you tied!")
        elif user_input <= computer_action:
            print(f"you won {score_1} games, computer won {score_2} games!")
            print("you lost!")
        elif user_input >= computer_action:
            print(f"you won {score_1} games, computer won {score_2} games!")
            print("you won!")


# Main Routine
main_program()
