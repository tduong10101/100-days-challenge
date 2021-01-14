import requests

def get_question():
    parameters = {
        "amount":10,
        "type":"boolean"
    }
    response = requests.get("https://opentdb.com/api.php",params=parameters)
    response.raise_for_status()
    data = response.json()
    return data['results']