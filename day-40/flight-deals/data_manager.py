import requests, json

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        with open("../cred.json") as f:
            cred = json.loads(f.read())
        
        sheety_api_key = cred["sheety"]["api_key"]
        kiwi_api_key = cred["tequila_kiwi"]["api_key"]
        self.sheety_endpoint = cred["sheety"]["endpoint"]
        self.kiwi_base = "https://tequila-api.kiwi.com"
        
        self.sheety_headers = {
            "Authorization": f"Bearer {sheety_api_key}"
        }
        self.kiwi_headers = {
            "apikey":kiwi_api_key
        }
        self.data= {}
        self.data["prices"] = self.pull_flight_data()
        self.data["users"] = self.pull_user_data()
        for key in data.keys():
            self.update_iataCode(self.data[key])
        
    
    def pull_data(self,sheet):
        response = requests.get(url=f"{self.sheety_endpoint}/{sheet}",headers=self.sheety_headers)
        response.raise_for_status()  
        return response.json()[sheet]

    def pull_flight_data(self):
        return self.pull_data("prices")

    def get_flight_data(self):
        return self.data[0]

    def get_user_data(self):
        return self.data[1]

    def pull_user_data(self):
        return self.pull_data("users")

    def update_iataCode(self,sheet):
        for d in self.data[sheet]:
            if not d['iataCode']:
                d.update({"iataCode": self.find_city_id(d['city'])})
                self.update_row(d,sheet)
    
    def update_row(self,d,sheet):
        body = {
            sheet[0:-1]: d
        }
        response = requests.put(url=f"{self.sheety_endpoint}/{d['id']}",json=body,headers=self.sheety_headers)
        response.raise_for_status()
        print(response.text)
    
    def find_city_id(self, city_name):        
        endpoint = f"{self.kiwi_base}/locations/query"
        parameters ={
            "term":city_name,
            "locale":"city",
        }
        response = requests.get(url=endpoint, headers=self.kiwi_headers, params=parameters)
        response.raise_for_status()
        return response.json()["locations"][0]['code']