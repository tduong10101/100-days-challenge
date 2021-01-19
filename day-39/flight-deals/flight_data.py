import requests, json

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        with open("../cred.json") as f:
            cred_data = json.loads(f.read())
        self.base_endpoint = "https://tequila-api.kiwi.com"
        self.api_key = cred_data["tequila_kiwi"]["api_key"]
        self.headers = {
            "apikey":self.api_key,
        }
        
    
