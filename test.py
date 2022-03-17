def calc_cost(number):
    days = int(input("how many days are your dogs staying"))
    rate = 22.50
    cost = days*rate*number
    confirm = str(input("Do you want to calculate the cost(Y/N): ")).upper()
    if confirm == "Y":
        print(f"Your cost for {days} days and {number} dogs is {cost}")


# Main Routine
calc_cost()

def main_function():
    print("======== Welcome to DogsRus Dog sitting ========")
    print("What do you want to do today: ")
    print("1 Drop off a dog")
    print("2 pick up a dog")
    print("3 calculate cost")
    print("4 print dog list")
    print("5 quit")

    choice = int(input("Enter your choice(Must be between 1 and 5): "))
        calc_cost(len(dog_list))
