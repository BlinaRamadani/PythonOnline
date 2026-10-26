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
print("Year: ", current_date.year)
print("Month: ", current_date.month)
print("Day: ", current_date.day)

current_time = datetime.datetime.now().time()
print("Hour: ", current_time.hour)
print("Minute: ", current_time.minute)
print("Second: ", current_time.second)
print("Microsecond: ", current_time.microsecond)

specific_date = datetime.date(2025, 4, 5)
specific_time = datetime.time(12, 30, 0)
print(specific_date)
print(specific_time)

duration = datetime.timedelta(days=5, hours=3)

new_date = current_date + duration
print(new_date)

previous_date = current_date - duration
print(previous_date)

utc_time = datetime.datetime.now(datetime.timezone.utc)
print("Current UTC time: ", utc_time)

custom_ofset = datetime.timedelta(hours=3)

custom_time = utc_time.replace(tzinfo=datetime.timezone(custom_ofset))
print("Current time in custom time zone(UTC+3): ", custom_time)
