# Write a Python program to print yesterday, today, tomorrow.

from datetime import datetime, timedelta
current_date = datetime.now()
new_date = current_date -timedelta(days=1)
new_date2 = current_date + timedelta(days=1)
print(new_date.strftime("%Y-%m-%d"))
print(current_date.strftime("%Y-%m-%d"))
print(new_date2.strftime("%Y-%m-%d"))