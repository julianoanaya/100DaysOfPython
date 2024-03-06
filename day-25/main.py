# with open("weather_data.csv") as data:
#     weather = data.readlines()
#     print(weather)
import csv

with open("weather_data.csv") as data_files:
    data = csv.reader(data_files)
    print(data)
    for row in data:
        print(row)
