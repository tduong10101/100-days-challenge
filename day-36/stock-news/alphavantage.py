import requests,json
class Alphavantage:
    
    def __init__(self):
        with open("../cred.json") as f:
            cred_data = json.loads(f.read())["alphavantage"]            
        self.api_key = cred_data["api_key"]
    
    def time_series_daily_adjusted(self,company_id):
        api_url = f"https://www.alphavantage.co/query"
        parameters = {
            "function":"TIME_SERIES_DAILY_ADJUSTED",
            "symbol":company_id,
            "apikey":self.api_key
        }
        response = requests.get(api_url,params=parameters)
        response.raise_for_status()
        data = response.json()
        return data
    
    def prev_diff_percentage(self,data:dict):
        data = data["Time Series (Daily)"]
        values_list = list(data.values())
        diff = (float(values_list[1]["4. close"]) - float(values_list[0]["4. close"]))
        return round(diff / 100,2)