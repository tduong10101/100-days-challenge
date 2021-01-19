import data_manager, flight_data
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

dm = data_manager.DataManager()
data = dm.get_data()


print(dm.data)