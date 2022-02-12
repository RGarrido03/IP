import math

def floatInput(prompt, min = -math.inf, max = math.inf):    # By default, min and max are equal to +/- infinite.
    a = True
    while a:    # This creates a loop that only ends when the input is a float.
        try:
            res = float(input(prompt))
            a = False
        except:
            print("ERROR: Not a float!")
    
    if min != -math.inf or max != math.inf: # When min or max values are different from the default ones.
        assert min < max    # Verify that min is always lower than max.

        if min <= res <= max:
            return res
        else:
            print(f"ERROR: Value should be in [{min}, {max}]!")
            return floatInput(prompt, min, max)
    else:
        return res


def main(): # Several pre-created inputs from Susana Mota.
    print("a) Try entering invalid values such as 1/2 or 3,1416.")
    v = floatInput("Value? ")
    print("v:", v)

    print("b) Try entering invalid values such as 15%, 110 or -1.")
    h = floatInput("Humidity (%)? ", 0, 100)
    print("h:", h)

    print("c) Try entering invalid values such as 23C or -274.")
    t = floatInput("Temperature (Celsius)? ", min=-273.15)
    print("t:", t)

if __name__ == "__main__":
    main()
