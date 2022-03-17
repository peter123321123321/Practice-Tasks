def main_routine():
    adult_tickets = 0
    student_tickets = 0
    child_tickets = 0
    gift_tickets = 0
    total_sales = 0
    tickets_sold = 0

    ticket_wanted = input("would you like to sell a ticket Y/N: ").upper()
    while ticket_wanted == "Y":
        ticket = sell_ticket()
        num_tickets = int(input("How many tickets do you want: "))
        confirm = input(f"Confirm purchase of {num_tickets} type {ticket} ticket(s)? (Y/N): ").upper()
        if confirm == "Y":
            price = num_tickets * float(get_price(ticket))
            total_sales += price
            tickets_sold += num_tickets
            if ticket == "A":
                adult_tickets += num_tickets
            elif ticket == "C":
                child_tickets += num_tickets
            elif ticket == "S":
                student_tickets += num_tickets
            else:
                gift_tickets += num_tickets

        ticket_wanted = input("\nDo you want to sell another ticket Y/N: ").upper()

        print("_____________________________________________________")
        print(f"The total tickets sold today was {tickets_sold}\n"
              f"This was made up of:\n"
              f"\t{adult_tickets} for adults; and\n"
              f"\t{student_tickets} for students; and\n"
              f"\t{child_tickets} for children; and\n"
              f"\t{gift_tickets} gifts vouchers\n")
        print(f"sales for the day come to {total_sales:.2f}")
        print("_____________________________________________________")


def sell_ticket():
    ticket_type_ = input("what kind of ticket do you want: \n"
                         "\tA for adult, or"
                         "\tS for student, or"
                         "\tC for child, or"
                         "\tG for gift voucher"
                         ">>").upper()
    return ticket_type_


def get_price(type_):
    prices = [["A", 12.5], ["S", 9], ["C", 7], ["G", 0]]
    for price in prices:
        if price[0] == type_:
            return price[1]


# Main Routine
print(" ************** Fanfare Movies - Ticketing Service ************** \n")
main_routine()
