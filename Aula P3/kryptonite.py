
# This program should find the phase of a fictional substance
# for given temperature and pressure conditions.

print("Kryptonite phase classifier")

# Input.
T = float(input("Temperature (K)? "))
P = float(input("Pressure (kPa)? "))

# Determine the phase.
if (P < 50) and (T < 400):
    if P < (1/8 * T):
        phase = "Gas"
    else:
        phase = "Solid"

elif (P > 50) and (T < 400):
    phase = "Solid"

elif (P < 50) and (T > 400):
    phase = "Gas"

else:
    phase = "Liquid"

# Output.
print("At {:.1f} K and {:.3f} kPa, Kryptonite is in the {} phase.".format(T, P, phase))

