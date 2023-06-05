def total_interest(deposit, rate, length_years, interest_type):
    if interest_type == "simple":
        interest = deposit * (1 + rate * length_years)
    elif interest_type == "compound":
        interest = deposit * pow(1 + rate, length_years)
    else:
        return None
    return round(interest, 2)


def bond_repayment(value_house, rate_monthly, num_months):
    if num_months == 0:
        print("Error: Please enter a non-zero value for the number of months.")
        return None
    repayment = (rate_monthly * value_house) / \
        (1 - pow(1 + rate_monthly, -num_months))
    return round(repayment, 2)


def main():
    print("Welcome to the financial calculator!")
    user_selection = input(
        "Please enter whether you want an 'Investment' or a 'Bond' calculation:\n > ").lower()

    if user_selection == "investment":
        print("You have chosen to calculate the interest on your investment.")
        try:
            deposit = float(
                input("Enter the amount of money you are depositing:\n > "))
            length_years = int(
                input("Enter the number of years you plan on investing:\n > "))
            rate = float(input("Enter the rate of interest:\n > ")) / 100
        except ValueError:
            print("Error: Please enter a valid numerical value.")
            return

        user_interest = input(
            "Please enter whether you would like to calculate 'Simple' or 'Compound' interest:\n > ").lower()
        interest = total_interest(deposit, rate, length_years, user_interest)
        if interest is not None:
            total_message = f"Based on your choice of '{user_interest.title()} interest' calculation, the total amount is £ {interest}"
            print(total_message)

    elif user_selection == "bond":
        print("You have selected the calculation of the 'Bond repayment' amount.")
        try:
            value_house = float(
                input("Enter the current value of the house:\n > "))
            rate_monthly = float(
                input("Enter the interest rate:\n > ")) / 100
            num_months = int(
                input("Enter the number of months you plan to take to repay the bond: \n > "))
        except ValueError:
            print("Error: Please enter a valid numerical value.")
            return

        repayment = bond_repayment(value_house, rate_monthly, num_months) / 12
        if repayment is not None:
            message_bond = f"The monthly bond repayment will be £ {repayment}"
            print(message_bond)

    else:
        print("Incorrect input. Please enter either 'investment' or 'bond'.")


if __name__ == '__main__':
    main()
