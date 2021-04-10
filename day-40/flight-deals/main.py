import data_manager, flight_data,flight_search,json
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

dm = data_manager.DataManager()
flight_list = dm.data[]
user_list = dm.get_user_data()
flight_data = []
results = []
for user in user_list():
    current_cities = [fd.from_city for fd in flight_data]
    if user['city'] not in current_cities:
        fs = flight_search.FlightSearch(max_stay=28,min_stay=7,currency="AUD",from_city=f"{user['city']}")
        flight_data.append(fs)
for fd in flight_data:
    for f in flight_list:
        results.append(fd.get_flight(to_city=f['iataCode'],lowest_price=f['lowestPrice']))

for user in user_list:
    ints_flight = [r for r in results if r.origin_city == user['city']]
