def user_input():
    import random
    possible_actions = ["Rock", "Paper", "Scissors"]
    choice = str(input("Choose an action(Rock, Paper, Scissors): ")).upper()
    computer_action = random.choice(possible_actions)
    score_1 = 0
    score_2 = 0


def main_program():
    import random
    count = 0
    limit = int(input("how many games do you want to play"))
    while count != limit:
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






# Main Routine
main_program()
