# This program lets you know if the points you input make a square.
from math import sqrt

print("""
P1 * * * * P2
   *     *
   *     *
P4 * * * * P3
""")

# Get the points
x1 = float(input("Input x1: "))
y1 = float(input("Input y1: "))
print()
x2 = float(input("Input x2: "))
y2 = float(input("Input y2: "))
print()
x3 = float(input("Input x3: "))
y3 = float(input("Input y3: "))
print()
x4 = float(input("Input x4: "))
y4 = float(input("Input y4: "))
print()

# Check if the sides are equal
top_side = sqrt((x2-x1)**2 + (y2-y1)**2)
left_side = sqrt((x4-x1)**2 + (y4-y1)**2)
right_side = sqrt((x3-x2)**2 + (y3-y2)**2)
bottom_side = sqrt((x4-x3)**2 + (y4-y3)**2)


if top_side == left_side == right_side == bottom_side:
    print("It's a square.")

else:
    print("It's not a square.")