import pandas as pd

data = pd.read_csv("weather_data.csv")

print(type(data["temp"]))

temp_list = data["temp"].to_list()
print(data["temp"].mean())

print(data["temp"].max())

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]

print(int(monday.temp)*1.8 + 32)

#Create dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76,65,65]
}

data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")