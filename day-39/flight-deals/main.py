import data_manager, flight_data,flight_search,json
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

dm = data_manager.DataManager()
data = dm.get_data()
print(data)
fs = flight_search.FlightSearch(max_stay=28,min_stay=7,currency="AUD")
for d in data:
    sample = fs.get_flight(from_city="MEL",to_city=d['iataCode'],lowest_price=d['lowestPrice'])
