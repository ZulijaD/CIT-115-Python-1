# Welcome message
print("Welcome to the Temperature Converter program. Created by Zulija!")

# Get the temperature input from the user (real number)
strTemperature = input("Please enter a temperature value: ")
fltTemperature = float(strTemperature)

# Get the scale of the temperature (C for Celsius, F for Fahrenheit)
strScale = input("Is the temperature in Fahrenheit (F/f) or Celsius (C/c)? ")

# Check if the entered scale is valid
if strScale.lower() not in ['f', 'c']:
    print("Enter a F or C")
else:
    # If Fahrenheit was entered
    if strScale.lower() == 'f':
        if fltTemperature > 212:
            print("Temp can not be > 212")
        else:
            # Convert Fahrenheit to Celsius
            fltCelsius = (5.0 / 9.0) * (fltTemperature - 32)
            print(f"The Celsius equivalent is: {fltCelsius:.1f}")

    # If Celsius was entered
    elif strScale.lower() == 'c':
        if fltTemperature > 100:
            print("Temp can not be > 100")
        else:
            # Convert Celsius to Fahrenheit
            fltFahrenheit = ((9.0 / 5.0) * fltTemperature) + 32
            print(f"The Fahrenheit equivalent is: {fltFahrenheit:.1f}")
