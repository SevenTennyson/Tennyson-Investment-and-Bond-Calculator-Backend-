import math
# displaying a menu of 2 options (invest and bond) to the user
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
print("")

# asking the user to input one of the options above
user_selects = str(input("Enter either 'investment' or 'bond' from the menu above to proceed: "))

# determining the type of financial calculation to perform (investment or bond)
if user_selects.lower() == "investment":
    deposit_amount = int(input("Enter the deposit amount: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    years = int(input("Enter the number of years for your investment plan: "))
    interest = input("Enter 'simple' or 'compound' to calculate the interest: ")
    
    # using .lower() to make the user's input lowercase because python is case sensitive
    if interest.lower() == "simple": # Calcultes simple interest
        result = deposit_amount * (1 + (interest_rate/100) * years)
        print(f"The total amount after {years} years will be: {result}")

    elif interest.lower() == "compound": # Calculates compound interest
        result = deposit_amount * math.pow((1 + (interest_rate/100)), years)
        print(f"The total amount after {years} years will be: {result}")

    else:
        print("Invalid input. Please enter 'simple' or 'compound'.")
        
elif user_selects.lower() == "bond":
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    months = int(input("Enter the number of months for your bond repayment plan: "))
    monthly_interest_rate = interest_rate / 100 / 12
    
    # Calculate bond repayment using the formula for monthly payments
    repayment = (monthly_interest_rate * present_value) / (1 - (1 + monthly_interest_rate)**(-months))

    print(f"The monthly bond repayment amount will be: {repayment}")

else:
    # Handling invalid input
    print("Invalid input. Please enter 'investment' or 'bond'.")
    