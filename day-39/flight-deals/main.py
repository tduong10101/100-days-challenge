import data_manager, flight_data,flight_search,json
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

dm = data_manager.DataManager()
data = dm.get_data()
print(data)
fs = flight_search.FlightSearch(from_city="LON",dm=dm)
sample = fs.get_flight()

with open("sample.json","w") as f:
    f.write(json.dumps(sample,indent=4))