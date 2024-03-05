import csv

# Data aus dem csv bekommen
"""
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    headers = next(data)
    for row in data:
        temperatures.append(int(row[1]))

    print(temperatures)
"""

import pandas

# Daten aus csv aber mit pandas
data = pandas.read_csv("weather_data.csv")
print(data)

data_dict = data.to_dict()

temp_list = data['temp'].to_list()

average = sum(temp_list)/len(temp_list)
print(f"The Average is {average}")

# panda alternative
print(f"the Average is {data['temp'].mean()}")

# max temp
temp_max = data['temp'].max()
print(temp_max)

# get column
print(data[data['day'] == 'Monday'])
