import data_manager, flight_data
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

dm = data_manager.DataManager()
data = dm.get_data()

fd = flight_data.FlightData(data)

dm.update_data(fd.data)

print(fd.data)