# with open("weather_data.csv") as data:
#     weather = data.readlines()
#     print(weather)
import csv

# with open("weather_data.csv") as data_files:
#     data = csv.reader(data_files)
#     temperature = []
#     print(data)
#     for row in data:
#         temperature.append(row[1])
# temperature.pop(0)
# real_temperature = []
# for num in temperature:
#     integer = int(num)
#     real_temperature.append(integer)
# print(real_temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
print(temp_list)
# sum = 0
# for temp in temp_list:
#     sum += temp
# average = sum / len(temp_list)
# print(average)

# Get data in Columns

print(data["condition"])
print(data.condition)


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

print(grey_squirrel_count)
print(black_squirrel_count)
print(cinnamon_squirrel_count)

data_dict = {
    "Fur_Colors": ["grey", "red", "black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count],
}
data = pandas.DataFrame(data_dict)
data.to_csv("counts_of_squirrels_of_different_colors.csv")
# # print(data[data.day == "Monday"])
