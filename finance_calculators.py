def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid numerical value.")


def total_interest(deposit, rate, length_years, interest_type):
    if interest_type == "simple":
        interest = deposit * (1 + rate * length_years)
    elif interest_type == "compound":
        interest = deposit * pow(1 + rate, length_years)
    else:
        return None
    return round(interest, 2)


def bond_repayment(value_house, rate_monthly, num_months):
    if num_months <= 0:
        print("Error: Please enter a positive value for the number of months.")
        return None
    repayment = (rate_monthly * value_house) / \
        (1 - pow(1 + rate_monthly, -num_months))
    return round(repayment, 2)


def main():
    print("Welcome to the financial calculator!")
    while True:
        user_selection = input(
            "Please enter whether you want an 'Investment' or a 'Bond' calculation:\n > ").lower()
        if user_selection == "investment":
            print("You have chosen to calculate the interest on your investment.")
            deposit = get_float(
                "Enter the amount of money you are depositing:\n > ")
            length_years = int(
                get_float("Enter the number of years you plan on investing:\n > "))
            rate = get_float("Enter the rate of interest:\n > ") / 100
            while True:
                user_interest = input(
                    "Please enter whether you would like to calculate 'Simple' or 'Compound' interest:\n > ").lower()
                if user_interest == "simple" or user_interest == "compound":
                    break
                else:
                    print(
                        "Incorrect input. Please enter either 'simple' or 'compound'.")
            interest = total_interest(
                deposit, rate, length_years, user_interest)
            if interest is not None:
                total_message = f"Based on your choice of '{user_interest.title()} interest' calculation, the total amount is £ {interest}"
                print(total_message)
            break

        elif user_selection == "bond":
            print("You have selected the calculation of the 'Bond repayment' amount.")
            value_house = get_float(
                "Enter the current value of the house:\n > ")
            rate_monthly = get_float(
                "Enter the interest rate:\n > ") / 100 / 12
            num_months = int(get_float(
                "Enter the number of months you plan to take to repay the bond: \n > "))
            repayment = bond_repayment(value_house, rate_monthly, num_months)
            if repayment is not None:
                message_bond = f"The monthly bond repayment will be £ {repayment}"
                print(message_bond)
            break
        else:
            print("Incorrect input. Please enter either 'investment' or 'bond'.")


if __name__ == '__main__':
    main()
