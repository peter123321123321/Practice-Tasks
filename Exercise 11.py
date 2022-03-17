def calc_fine(days):
    base_charge = 0.5
    day_charge = 0.8
    total_fine = base_charge + days * day_charge
    if total_fine > 30.00:
        fine = 30
    return total_fine


# Main Routine
days_ = int(input("how many 5days overdue"))
print(f"for {days_} days overdue the fine is ${calc_fine(days_):.2f}")
