import requests, json

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        with open("../cred.json") as f:
            cred = json.loads(f.read())
        
        api_key = cred["sheety"]["api_key"]
        self.endpoint = cred["sheety"]["endpoint"]
        
        self.headers = {
            "Authorization": f"Bearer {api_key}"
        }
    
    def get_data(self):
        response = requests.get(url=self.endpoint,headers=self.headers)
        response.raise_for_status()
        return response.json()['prices']
    
    def update_data(self,data):
        current_data = self.get_data()
        for d in data:
            if d not in current_data:
                body = {
                    'price': d
                }
                response = requests.put(url=f"{self.endpoint}/{d['id']}",json=body,headers=self.headers)
                print(response.text)