# Prompting for input with spaces after colons for clarity
sPrincipal = input("Principal Investment (PV): ")
sInterestRate = input("Interest Rate (R): ")
sCompoundingTimes = input("Compounding Times per Year (m): ")
sTermYears = input("Term Number of Years (t): ")

# Converting input strings to appropriate numeric types
nPrincipal = float(sPrincipal)
nInterestRate = float(sInterestRate) / 100  # Convert interest rate to decimal
nCompoundingTimes = int(sCompoundingTimes)
nTermYears = float(sTermYears)

# Calculating the Future Value using the compound interest formula
# FV = PV * (1 + r / m)^(m * t)
nFutureValue = nPrincipal * (1 + nInterestRate / nCompoundingTimes) ** (nCompoundingTimes * nTermYears)

# Displaying the result, formatted to 2 decimal places with a dollar sign
print(f"\nFuture Value: ${nFutureValue:,.2f}")
