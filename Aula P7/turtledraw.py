import turtle
from tkinter import filedialog

t = turtle.Turtle()
sc = turtle.Screen()

# Use t.up(), t.down() and t.goto(x, y)

# Put your code here
filename = filedialog.askopenfilename(title="Choose File")
file = open(filename, "r")

for line in file:
    if line == "UP\n":
        t.up()
    
    elif line == "DOWN\n":
        t.down()
    
    else:
        line_split = line.split()
        t.goto(float(line_split[0]), float(line_split[1]))

# wait
sc.exitonclick()

