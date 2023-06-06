# _Project Name:_ Financial Calculator

> **Table of Contents:**
>
> - Project description
> - Code description

#### Project description:

A Python program called the financial calculator project is designed to help users calculate interest and bond repayment for investments.

Using this code, users can perform financial calculations using a user-friendly interface, and it allows them to enter relevant information, such as interest rates, investment amounts, and repayment periods. Depending on the method selected (simple interest or compound interest for investments or bond repayments for loans), the corresponding results are calculated.

#### Code description:

1. The function `get_float(prompt)` takes a prompt as input and repeatedly prompts the user to enter a valid numerical value until a valid float is provided. It uses a while loop and a `try-except` block to handle `ValueError` exceptions when converting the input to a float.

2. The function `total_interest` calculates interest based on deposit, interest rate, investment period, and type of interest ("simple" or "compound"). The calculated interest amount is returned, rounded to two decimal places.

3. The function`bond_repayment` calculates the monthly bond repayment amount based on the value of the house, monthly interest rate, and number of months for bond repayment. The calculated repayment amount is returned, rounded to two decimal places.

4. The `main` function is the entry point of the financial calculator program. It displays a welcome message and prompts the user to choose between an "investment" or "bond"calculation. Based on the user's selection, it prompts for the necessary input values and calls the corresponding function to calculate and display the result.

Main()'s breakdown is as follows:
- It displays a welcome message and prompts the user to select either an "investment" or a "bond" calculation.
- It enters an infinite loop using `while True`, which allows the user to perform multiple calculations without having to restart the program.
- Inside the loop, it prompts the user to enter their choice of calculation: "investment" or "bond". The input is converted to lowercase using `.lower()` to handle variations in user input.

- If the user selects "investment", it prompts for the necessary input values:
  - The amount of money being deposited (deposit)
  - The number of years for the investment (length_years)
  - The interest rate as a percentage (rate)
  - It then prompts the user to choose between "simple" or "compound" interest calculation (`user_interest`).
  - It calls the `total_interest()` function with the provided inputs to calculate the total interest.
  - If the calculated interest `is not None`, it displays a message with the calculated amount.

- If the user selects "bond", it prompts for the necessary input values:
  - The current value of the house (value_house)
  - The interest rate as a percentage (rate_monthly)
  - The number of months to repay the bond (num_months)
  - It calls the `bond_repayment()` function with the provided inputs to calculate the monthly "bond" repayment.
  - If the calculated repayment `is not None`, it displays a message with the calculated amount.

- If the user enters an invalid input (neither "investment" nor "bond"), it displays an error message and prompts the user again to enter a valid choice.
- Once the calculation is performed and the result is displayed, the loop breaks, and the program ends.
- The code is executed when the script is run directly `(__name__ == '__main__')`, and the main function is called to start the program.
