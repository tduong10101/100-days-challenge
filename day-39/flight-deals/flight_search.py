import requests, json
from flight_data import FlightData
import datetime as dt

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self,currency,max_stay,min_stay):
        with open("../cred.json") as f:
            cred_data = json.loads(f.read())
        self.base_endpoint = "https://tequila-api.kiwi.com"
        self.api_key = cred_data["tequila_kiwi"]["api_key"]
        self.headers = {
            "apikey":self.api_key,
        }
        self.min_stay = min_stay
        self.max_stay = max_stay
        self.currency = currency
    
    def get_flight(self,from_city,to_city,lowest_price):
        endpoint = f"{self.base_endpoint}/v2/search"
        date_from = dt.datetime.now().strftime("%d/%m/%Y")
        date_to = dt.datetime.now() + dt.timedelta(days=1)
        date_to = date_to.strftime("%d/%m/%Y")
        body = {
            "fly_from":from_city,
            "fly_to":to_city,
            "date_from":date_from,
            "date_to":date_to,
            "nights_in_dst_from":self.min_stay,
            "nights_in_dst_to":self.max_stay,
            "curr":self.currency,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
        }
        response = requests.get(url=endpoint,params=body,headers=self.headers)
        response.raise_for_status()
        data = response.json()
        print(data)
        if len(data["data"])>0:
            data = data["data"][0]            
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: {flight_data.price} {self.currency}")
            return flight_data
        else:
            pass