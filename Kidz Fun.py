from sys import exit


def main_program():
    choice = 0
    while choice != 3:
        print("<============================================>")
        print("Welcome to Kidz Fun")
        print("Please select one of the options below")
        print("<============================================>")
        print("Sign up for Fun in the Sun[1] ")
        print("Sign up for Active_kidz[2] ")
        print("Exit program[3] ")
        print("See kidz currently signed up for Kidz Fun[X] ")
        print("<============================================>")
        user_choice = int(input("Enter your choice(1, 2, 3, 4): "))
        if user_choice == 1:
            fun_in_the_sun()
        if user_choice == 2:
            active_kidz()
        if user_choice == 3:
            print("Thanks for using Kidz Fun")
            exit()
        if user_choice == "4":
            active_kidz_list


def fun_in_the_sun():
    confirm = str(input("Confirm your choice(Y/N): "))
    if confirm.upper() == "Y":
        print("Choice confirmed")
        age = float(input("What is your age: "))
        if 5 < age < 15:
            print("Your child is eligible for participation in Active Kidz")
            active_kidz_list.append(age)
        else:
            print("Your child is not eligible for participation in Active Kidz")
    else:
        print("Choice confirmed")
        main_program()


def active_kidz():
    confirm = str(input("Would you like to register for active kidz(Y/N): "))
    if confirm.upper() == "Y":
        print("Choice confirmed")
        age = float(input("What is your age: "))
        if 5 < age < 15:
            print("Your child is eligible for participation in Active Kidz")
            active_kidz_list.append(age)
        else:
            print("Your child is not eligible for participation in Active Kidz")
    else:
        print("Choice confirmed")
        main_program()

def kids_in_program():
    print(f"{fun_in_the_sun_list}")

# Main Routine
fun_in_the_sun_list = []
active_kidz_list = []
main_program()
