import requests,json

class Newsapi:
    
    def __init__(self):
        with open("../cred.json") as f:
            cred_data = json.loads(f.read())["newsapi"]            
        self.api_key = cred_data["api_key"]
        
    def get_news(self,keyword,page_size):
        api_url = "https://newsapi.org/v2/top-headlines"
        parameters = {
            "apiKey":self.api_key,
            "pageSize":page_size,
            "q":keyword
        }
        response = requests.get(api_url,params=parameters)
        response.raise_for_status()
        return response.json()["articles"]