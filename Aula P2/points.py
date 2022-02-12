# This program reads the coordinates of two points (x1,y1) and (x2,y2).

x1 = float(input("x1? "))
y1 = float(input("y1? "))
x2 = float(input("x2? "))
y2 = float(input("y2? "))

# Find and print the distance between the points!
import math
print(f"A distância entre os dois pontos é {round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)} unidades de comprimento.")
