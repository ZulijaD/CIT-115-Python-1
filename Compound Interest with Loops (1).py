# Function to validate numeric input
def get_positive_numeric_input(prompt, allow_zero=False):
    while True:
        try:
            value = float(input(prompt))
            if value > 0 or (allow_zero and value == 0):
                return value
            else:
                print("Error: Please enter a positive value." if not allow_zero else "Error: Value cannot be negative.")
        except ValueError:
            print("Error: Please enter a valid numeric value.")

# Prompt user for inputs with validation
flt_deposit = get_positive_numeric_input("Enter the initial deposit amount: ")
flt_interest_rate_percentage = get_positive_numeric_input("Enter the annual interest rate (as a percentage, e.g., 5 for 5%): ")
int_num_months = int(get_positive_numeric_input("Enter the number of months: "))
flt_goal = get_positive_numeric_input("Enter your goal amount (can be 0): ", allow_zero=True)

# Convert interest rate percentage to monthly decimal rate
flt_monthly_interest_rate = (flt_interest_rate_percentage / 100) / 12

# Display monthly compounding details
print("\n--- Monthly Compounding Details ---")
flt_account_balance = flt_deposit

for int_month in range(1, int_num_months + 1):
    flt_monthly_interest = flt_account_balance * flt_monthly_interest_rate
    flt_account_balance += flt_monthly_interest
    print(f"Month {int_month}: Account Balance = ${flt_account_balance:,.2f}")

# Determine the number of months to reach the goal
if flt_goal > 0:
    print("\n--- Predicting Time to Reach Goal ---")
    flt_account_balance = flt_deposit
    int_goal_months = 0

    while flt_account_balance < flt_goal:
        flt_monthly_interest = flt_account_balance * flt_monthly_interest_rate
        flt_account_balance += flt_monthly_interest
        int_goal_months += 1

    print(f"It will take {int_goal_months:,} months to reach the goal of ${flt_goal:,.2f}.")
else:
    print("\nNo goal specified (0). Skipping goal prediction.")
