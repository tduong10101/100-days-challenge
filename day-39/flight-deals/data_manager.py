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
        self.data=self.get_data()
        self.update_iataCode()
    
    def get_data(self):
        response = requests.get(url=self.sheety_endpoint,headers=self.sheety_headers)
        response.raise_for_status()  
        return response.json()['prices']
    
    def update_iataCode(self):
        new_data = self.data
        for d in new_data:
            if not d['iataCode']:
                print(d['city'])
                d.update({"iataCode": self.find_city_id(d['city'])})
        for d in new_data:
            if d not in self.data:
                self.update_row(d)
        self.data=new_data
    
    def update_row(self,d):
        body = {
            'price': d
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