# Exercise 7 from aula05

print("Please input the numbers you'd like to get the average.")

# Define variables.
n = 0
numerator = 0
denominator = 0

while n != "":              # While n isn't an empty line (which means, while n is a number).
    numerator += n          # Add the number the user inputs.
    n = input()             # Input the number.
    if n != "":
        n = float(n)
        denominator += 1

average = numerator/denominator

print(f"The average is {average}, bestie.")