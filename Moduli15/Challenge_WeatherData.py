import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('weather_tokyo_data.csv')

print(df.info())

df["full_date"] = pd.to_datetime(df['year'].astype(str) + '/'+df["day"])

df["temperature"] = pd.to_numeric(df["temperature"], errors='coerce')

average = df["temperature"]


df["month"] = df["full_date"].dt.month

monthly_average = df.groupby('month')['temperature'].mean()

print("Average temperature for each month:")
print(monthly_average)

monthly_average.plot(kind='bar')

plt.title("Monthly average temperature", fontsize=16)

plt.xlabel("Month", fontsize=14)
plt.ylabel("Temperature", fontsize=14)

plt.show()

