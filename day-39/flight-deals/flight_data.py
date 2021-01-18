import requests, json

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,data):
        with open("../cred.json") as f:
            cred_data = json.loads(f.read())
        self.base_endpoint = "https://tequila-api.kiwi.com"
        self.api_key = cred_data["tequila_kiwi"]["api_key"]
        self.headers = {
            "apikey":self.api_key,
        }
        for d in data:
            if not d['iataCode']:
                print(d['city'])
                d.update({"iataCode": self.find_city_id(d['city'])})
        self.data = data
    
    def find_city_id(self, city_name):
        endpoint = f"{self.base_endpoint}/locations/query"
        parameters ={
            "term":city_name,
            "locale":"city",
        }
        response = requests.get(url=endpoint, headers=self.headers, params=parameters)
        response.raise_for_status()
        return response.json()["locations"][0]['code']