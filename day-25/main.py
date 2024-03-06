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
