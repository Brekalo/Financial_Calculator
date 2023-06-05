# _Project Name:_ Financial_Calculator

#### Code description:

1. The code defines two functions: `total_interest(deposit, rate, length_years, interest_type)` and `bond_repayment(value_house, rate_monthly, num_months)`. These functions perform the calculations for interest and bond repayment, respectively.

- The `total_interest` function takes the deposit amount, interest rate, investment period in years, and the type of interest ("simple" or "compound") as inputs. It calculates the interest amount based on the provided inputs and returns the rounded interest amount.
- The `bond_repayment` function takes the value of the house, monthly interest rate, and the number of months for bond repayment as inputs. It calculates the monthly bond repayment amount based on the provided inputs and returns the rounded repayment amount.

2. The `main` function is the entry point of the program.

- It displays a welcome message and prompts the user to select either an "investment" or a "bond" calculation.
- If the user selects "investment", the program asks for the deposit amount, investment period, and interest rate. It also asks the user to choose between "simple" or "compound" interest. The `total_interest` function is called with the provided inputs to calculate the interest amount. If the calculated interest `is not None`, it prints a message displaying the interest amount.
- If the user selects "bond", the program asks for the value of the house, monthly interest rate, and the number of months for bond repayment. The `bond_repayment` function is called with the provided inputs to calculate the monthly bond repayment amount. If the calculated repayment `is not None`, it prints a message displaying the repayment amount.
- If the user enters an incorrect input, an `error` message is displayed.
  The program handles `ValueError` exceptions when converting user inputs to numerical values and displays an error message if an invalid numerical value is entered.
- The code is executed when the script is run directly `(__name__ == '__main__')`, and the main function is called to start the program.
