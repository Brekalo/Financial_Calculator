import math

# calculates simple and compound interest in investments and bond repayments

def total_simple(deposit, rate, length_years):
    simple_interest = deposit * (1 + rate * length_years)
    return simple_interest


def total_compound(deposit, rate, lenght_years):
    compound_interest = deposit * math.pow((1 + rate), lenght_years)
    return compound_interest


def bond_repayment(value_house, rate_monthly, num_months):
    repayment = (rate_monthly * value_house) / \
        (1 - (1 + rate_monthly)**(-num_months))
    return repayment


print("Welcome to the financial calculator!")

# all user entries are recognized as valid by using the lower method and converting them to lowercase for case-insensitive comparison
user_selection = input(
    "Please enter whether you want an 'Investment' or a 'Bond' calculation:\n > ").lower()

if (user_selection == "investment"):
    print("You have chosen to calculate the interest on your investment.")

    # inputs values from user
    deposit = float(
        input("Enter the amount of money you are depositing:\n > "))
    # interest entered divided by 100
    length_years = int(
        input("Enter the number of years you plan on investing:\n > "))
    rate = float(input("Enter the rate of interest:\n > ")) / 100

    user_interest = input(
        "Please enter whether you would like to calculate 'Simple' or 'Compound' interest:\n > ").lower()

    # calculate interest simple and compound, and output result
    if (user_interest == "simple"):
        simple_interest = total_simple(deposit, rate, length_years)
        total_message = f"Based on your choice of 'Simple interest' calculation, the total amount is £ {simple_interest:.2f}"
        print(total_message)

    elif (user_interest == "compound"):
        compound_interest = total_compound(deposit, rate, length_years)
        total_message = f"Based on your choice of 'Compound interest' calculation, the total amount is £ {compound_interest:.2f}"
        print(total_message)

    else:
        print("Incorrect input. Please enter either 'simple' or 'compound'.")


elif (user_selection == "bond"):
    print("You have selected the calculation of the 'Bond repayment' amount.")

    # inputs value from user
    value_house = float(input("Enter the current value of the house:\n > "))

    # interest entered divided by 100
    rate_monthly = float(input("Enter the interest rate:\n > ")) / 100
    num_months = int(input(
        "Enter the number of months you plan to take to repay the bond: \n > "))

    # calculate bond repayment and output message and monthly interest divided by 12
    repayment = bond_repayment(value_house, rate_monthly, num_months) / 12
    message_bond = f"The monthly bond repayment will be £ {repayment:.2f}"
    print(message_bond)
else:
    # display error message for invalid input
    print("Incorrect input. Please enter either 'investment' or 'bond'.")
