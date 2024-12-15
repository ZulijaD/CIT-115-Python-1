import math

# Function to get valid float input
def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Error: Please enter a positive, non-zero value.")
        except ValueError:
            print("Error: Please enter a valid number.")

# Function to calculate gallons of paint
def getGallonsOfPaint(fSquareFeet, fFeetPerGallon):
    return math.ceil(fSquareFeet / fFeetPerGallon)

# Function to calculate labor hours
def getLaborHours(fLaborHoursPerGallon, iTotalGallons):
    return fLaborHoursPerGallon * iTotalGallons

# Function to calculate labor cost
def getLaborCost(fLaborHours, fLaborChargePerHour):
    return fLaborHours * fLaborChargePerHour

# Function to calculate paint cost
def getPaintCost(iTotalGallons, fPaintPrice):
    return iTotalGallons * fPaintPrice

# Function to determine sales tax rate based on state
def getSalesTax(sState):
    state_tax_rates = {
        "CT": 0.06,
        "MA": 0.0625,
        "ME": 0.085,
        "NH": 0.0,
        "RI": 0.07,
        "VT": 0.06
    }
    return state_tax_rates.get(sState.upper(), 0.0)

# Function to display cost estimate
def showCostEstimate(fSquareFeet, iTotalGallons, fLaborHours, fPaintCost, fLaborCost, fSalesTaxRate, sLastName):
    total_cost = fPaintCost + fLaborCost
    total_tax = total_cost * fSalesTaxRate
    grand_total = total_cost + total_tax

    output = (
        f"Customer: {sLastName}\n"
        f"Square Feet of Wall: {fSquareFeet:.2f}\n"
        f"Gallons of Paint Needed: {iTotalGallons}\n"
        f"Labor Hours: {fLaborHours:.2f}\n"
        f"Paint Cost: ${fPaintCost:.2f}\n"
        f"Labor Cost: ${fLaborCost:.2f}\n"
        f"Sales Tax Rate: {fSalesTaxRate * 100:.2f}%\n"
        f"Total Tax: ${total_tax:.2f}\n"
        f"Grand Total: ${grand_total:.2f}\n"
    )

    print(output)

    file_name = f"{sLastName}_PaintJobOutput.txt"
    with open(file_name, "w") as file:
        file.write(output)

    print(f"File created: {file_name}")

# Main function
def main():
    # Get inputs from user
    fSquareFeet = getFloatInput("Enter Square Feet of the Wall: ")
    fPaintPrice = getFloatInput("Enter Paint Price per Gallon: ")
    fFeetPerGallon = getFloatInput("Enter Feet per Gallon of Paint: ")
    fLaborHoursPerGallon = getFloatInput("Enter Labor Hours per Gallon of Paint: ")
    fLaborChargePerHour = getFloatInput("Enter Painting Labor Charge per Hour: ")

    sState = input("Enter the state where the job will take place: ").strip()
    sLastName = input("Enter the customer's last name: ").strip()

    # Perform calculations
    iTotalGallons = getGallonsOfPaint(fSquareFeet, fFeetPerGallon)
    fLaborHours = getLaborHours(fLaborHoursPerGallon, iTotalGallons)
    fLaborCost = getLaborCost(fLaborHours, fLaborChargePerHour)
    fPaintCost = getPaintCost(iTotalGallons, fPaintPrice)
    fSalesTaxRate = getSalesTax(sState)

    # Show cost estimate and save to file
    showCostEstimate(fSquareFeet, iTotalGallons, fLaborHours, fPaintCost, fLaborCost, fSalesTaxRate, sLastName)

# Run the program
if __name__ == "__main__":
    main()
