import requests, json, data_manager
import datetime as dt
MIN_STAY=7
MAX_STAY=28
CURRENCY="GBP"
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self,from_city,dm:data_manager.DataManager):
        with open("../cred.json") as f:
            cred_data = json.loads(f.read())
        self.base_endpoint = "https://tequila-api.kiwi.com"
        self.api_key = cred_data["tequila_kiwi"]["api_key"]
        self.headers = {
            "apikey":self.api_key,
        }
        self.from_city = from_city
        self.dm = dm
    
    def get_flight(self):
        endpoint = f"{self.base_endpoint}/search"
        date_from = dt.datetime.now().strftime("%d/%m/%Y")
        date_to = dt.datetime.now() + dt.timedelta(days=1)
        date_to = date_to.strftime("%d/%m/%Y")
        for d in self.dm.data:
            body = {
                "fly_from":self.from_city,
                "fly_to":d['iataCode'],
                "date_from":date_from,
                "date_to":date_to,
                "nights_in_dst_from":MIN_STAY,
                "nights_in_dst_to":MAX_STAY,
                "curr":CURRENCY,
                "price_to":d['lowestPrice']
            }
            response = requests.get(url=endpoint,params=body,headers=self.headers)
            response.raise_for_status()
            flight_data = response.json()['data']
            return flight_data