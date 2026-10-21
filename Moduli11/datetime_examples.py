import datetime

current_datetime = datetime.datetime.now()
print(current_datetime)

print("Year: ", current_datetime.year)
print("Month: ", current_datetime.month)
print("Day: ", current_datetime.day)
print("Hour: ", current_datetime.hour)
print("Minutes: ", current_datetime.minute)
print("Second: ", current_datetime.second)
print("Microsecond: ", current_datetime.microsecond)

current_date = datetime.datetime.now().date()
print(current_date)