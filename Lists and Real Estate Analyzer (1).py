# Function to get a valid float input
def getFloatInput(prompt):
    """
    Prompts the user for input, validates that the input is a positive, non-zero float,
    and returns the valid input.
    """
    while True:
        try:
            value = float(input(prompt))  # Attempt to convert input to float
            if value <= 0:
                print("Error: Value must be a positive, non-zero number. Please try again.")
            else:
                return value  # Return the valid float
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

# Function to calculate the median
def getMedian(values):
    """
    Receives a list of numbers and calculates the median.
    If the number of elements is odd, it returns the middle value.
    If even, it returns the average of the two middle values.
    """
    count = len(values)
    values.sort()  # Ensure the list is sorted
    if count % 2 == 1:  # Odd number of elements
        return values[count // 2]
    else:  # Even number of elements
        mid = count // 2
        return (values[mid - 1] + values[mid]) / 2

# Main function
def main():
    """
    Main function to gather sales data, compute analytics, and display results.
    """
    sales = []  # List to store sales values

    # Loop to gather sales data
    while True:
        # Get sales price
        sales_price = getFloatInput("Enter property sales value: ")
        sales.append(sales_price)  # Add the value to the list

        # Prompt for more entries
        while True:
            more_input = input("Enter another value (Y/N): ").strip().lower()
            if more_input in ['y', 'n']:
                break
            else:
                print("Error: Please enter Y or N.")

        if more_input == 'n':  # Exit loop if 'N' is entered
            break

    # Sort the sales list
    sales.sort()

    # Display sales values formatted as currency
    print("\nProperty Sales (sorted):")
    for sale in sales:
        print(f"${sale:,.2f}")

    # Calculate and display analytics
    total = sum(sales)
    min_value = sales[0]
    max_value = sales[-1]
    average = total / len(sales)
    median = getMedian(sales)
    commission = total * 0.03

    # Output results
    print("\nSales Analytics:")
    print(f"Minimum Sale: ${min_value:,.2f}")
    print(f"Maximum Sale: ${max_value:,.2f}")
    print(f"Total Sales: ${total:,.2f}")
    print(f"Average Sale: ${average:,.2f}")
    print(f"Median Sale: ${median:,.2f}")
    print(f"Commission (3%): ${commission:,.2f}")

# Run the program
if __name__ == "__main__":
    main()

