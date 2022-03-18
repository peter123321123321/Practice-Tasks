def main_program():
    user_choice = 0
    while user_choice != 3:
        print("<============================================>")
        print("Welcome to Kidz Fun")
        print("Please select one of the options below")
        print("<============================================>")
        print("Sign up for Fun in the Sun[1] ")
        print("Sign up for Active_kidz[2] ")
        print("Exit program[3] ")
        print("<============================================>")
        user_choice = int(input("Enter your choice(1, 2, 3, 4): "))
        if user_choice == 1:
            fun_in_the_sun()
        elif user_choice == 2:
            active_kidz()
        elif user_choice == 3:
            print("Thanks for using Kidz Fun")
            exit()
        else:
            print("Please enter valid number.")
            main_program()


def fun_in_the_sun():
    confirm = str(input("Would you like to register for fun in the sun(Y/N): "))
    if confirm.upper() == "Y":
        print("Choice confirmed")
        age = float(input("What is your age: "))
        if 4 < age < 16:
            print("Your child is eligible for participation in fun in the sun")
            fun_in_the_sun_list.append(age)
        else:
            print("Your child is not eligible for participation in fun in the sun")
    else:
        print("Choice confirmed")
        main_program()


def active_kidz():
    confirm = str(input("Would you like to register for active kidz(Y/N): "))
    if confirm.upper() == "Y":
        print("Choice confirmed")
        age = float(input("What is your age: "))
        if 4 < age < 16:
            print("Your child is eligible for participation in Active Kidz")
            active_kidz_list.append(age)
        else:
            print("Your child is not eligible for participation in Active Kidz")
    else:
        print("Choice confirmed")
        main_program()


def exit():
    confirm = str(input("Would you like to leave the program?")).upper()
    if confirm == "Y":
        if len(fun_in_the_sun_list) == 0:
            print("No kids have been registered for Fun in the Sun")
        else:
            print(f"In the Fun in the Sun program the sum of all ages is {sum(fun_in_the_sun_list)} ")
            print(f"In the Fun in the Sun program the average of all ages is {sum(fun_in_the_sun_list)/len(fun_in_the_sun_list)}")
        if len(active_kidz_list) == 0:
            print("No kids have been registered for Fun in the Sun")
        else:
            print(f"In the Active Kidz program the sum of all ages is {sum(active_kidz_list)} ")
            print(f"In the Active Kidz program the average of all ages is {sum(active_kidz_list)/len(active_kidz_list)}")
    else:
        main_program()

# Main Routine
fun_in_the_sun_list = []
active_kidz_list = []
main_program()
