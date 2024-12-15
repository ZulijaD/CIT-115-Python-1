# Constants for each planet's surface gravity factor
GRAVITY_MERCURY = 0.38
GRAVITY_VENUS = 0.91
GRAVITY_MOON = 0.165
GRAVITY_MARS = 0.38
GRAVITY_JUPITER = 2.34
GRAVITY_SATURN = 0.93
GRAVITY_URANUS = 0.92
GRAVITY_NEPTUNE = 1.12
GRAVITY_PLUTO = 0.066

# Prompt the user for their name and Earth weight
sName = input("Enter your name: ")
sEarthWeight = input("Enter your Earth weight: ")

# Convert Earth weight to a floating-point number
nEarthWeight = float(sEarthWeight)

# Calculate weight on each planet
nWeightMercury = nEarthWeight * GRAVITY_MERCURY
nWeightVenus = nEarthWeight * GRAVITY_VENUS
nWeightMoon = nEarthWeight * GRAVITY_MOON
nWeightMars = nEarthWeight * GRAVITY_MARS
nWeightJupiter = nEarthWeight * GRAVITY_JUPITER
nWeightSaturn = nEarthWeight * GRAVITY_SATURN
nWeightUranus = nEarthWeight * GRAVITY_URANUS
nWeightNeptune = nEarthWeight * GRAVITY_NEPTUNE
nWeightPluto = nEarthWeight * GRAVITY_PLUTO

# Display the results with proper formatting
print(f"\n{sName}, here is your weight on the Solar System's planets:\n")
print(f"{'Planet':<10}{'Weight (lbs)':>10}")
print(f"{'-'*20}")
print(f"{'Mercury':<10}{nWeightMercury:>10.2f}")
print(f"{'Venus':<10}{nWeightVenus:>10.2f}")
print(f"{'Moon':<10}{nWeightMoon:>10.2f}")
print(f"{'Mars':<10}{nWeightMars:>10.2f}")
print(f"{'Jupiter':<10}{nWeightJupiter:>10.2f}")
print(f"{'Saturn':<10}{nWeightSaturn:>10.2f}")
print(f"{'Uranus':<10}{nWeightUranus:>10.2f}")
print(f"{'Neptune':<10}{nWeightNeptune:>10.2f}")
print(f"{'Pluto':<10}{nWeightPluto:>10.2f}")
