# This program lets you get the number of days in a month, based on the month and the year.

# Get the month and the year
for x in range(10):
    month = int(input("Input the number corresponding to the month (1 to 12): "))
    if month > 12 or month < 1:
        print("Invalid month. Please input a number between 1 and 12.")
    else: break

year = int(input("Input the year: "))

# Get the current date
from datetime import datetime
current_month = datetime.now().month
current_year = datetime.now().year

# Change the verb according to the year and the month
if year == current_year and month == current_month:
    verb = "has"

elif (year < current_year) or (year == current_year and month < current_month):
    verb = "had"

else:
    verb = "will have"

# Printing conditions
if month == 1:
    print(f"January {year} {verb} 31 days.")

elif month == 3:
    print(f"March {year} {verb} 31 days.")

elif month == 4:
    print(f"April {year} {verb} 30 days.")

elif month == 5:
    print(f"May {year} {verb} 31 days.")

elif month == 6:
    print(f"June {year} {verb} 30 days.")

elif month == 7:
    print(f"July {year} {verb} 31 days.")

elif month == 8:
    print(f"August {year} {verb} 31 days.")

elif month == 9:
    print(f"September {year} {verb} 30 days.")

elif month == 10:
    print(f"October {year} {verb} 31 days.")

elif month == 11:
    print(f"November {year} {verb} 30 days.")

elif month == 12:
    print(f"December {year} {verb} 31 days.")

elif month == 2:
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        print(f"February {year} {verb} 29 days.")
    else:
        print(f"February {year} {verb} 28 days.")
