# This program gives the day before and the day after a certain date you input.

from datetime import datetime

current_day = input("Input the current day: ")
current_month = input("Input the current month: ")
current_year = input("Input the current year: ")
current_date_str = f"{current_day.zfill(2)}/{current_month.zfill(2)}/{current_year[2:4]}"

from datetime import datetime, timedelta
current_date = datetime.strptime(current_date_str, "%d/%m/%y")

day_before = str(current_date - timedelta(days=1))
day_after = str(current_date + timedelta(days=1))

print(f"The day before is {day_before[:10]} and the day after is {day_after[:10]}.")