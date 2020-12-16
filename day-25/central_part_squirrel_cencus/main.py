import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data["Primary Fur Color"].count()
count_by_color = data["Primary Fur Color"].value_counts()
new_data = pd.DataFrame(count_by_color)
new_data = new_data.reset_index()
new_data.columns = ['fur_color','counts']
print(new_data)
new_data.to_csv("count_by_color.csv")