import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240127.csv")

color_count = data['Primary Fur Color'].value_counts()

color_count.to_csv("squirrel_color")
