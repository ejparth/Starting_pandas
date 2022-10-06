## read weather data ##


##-- opening the file and reading it --##

''''
import csv

with open("weather_data - weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print (temperature)
'''
import pandas
total = 0
data = pandas.read_csv("./weather_data - weather_data.csv")
temp = (data["temp"])
list_of_temp =  temp.to_list()
print(list_of_temp)

## --- method 1 -- for avg --##
for one in list_of_temp:
    total += one

## --- method 2 -- for avg --##
avg = total/len(list_of_temp)
print(avg)


print(data["temp"].mean())
print(data["temp"].max())

print(data.temp) #key method
print(data.temp) #attribute method


## searchin in the data ##

print(data[data.day == "Monday"])   ## filter
print(data[data.temp == data.temp.max()]) ##fiter condition


## converting temp to farenhite ##

temp_list = data.temp.to_list()
print(temp_list)


new_fa_temp = []
for data in temp_list:
    new_fa_temp.append(data * 9/5 +32)
print(new_fa_temp)

## for monday


## create data frame from scratch

data_dict = {
    "name" : ["aakash", "anil", "alok", "anuj"],
    "age" : [21, 32, 32, 21],

}

data = pandas.DataFrame(data_dict)
print (data)