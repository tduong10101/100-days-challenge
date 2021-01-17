import requests, json
import datetime as dt

GENDER = "male"
WEIGHT = 69.8
HEIGHT = 169.00
AGE = 31

# get credentials
with open("../cred.json") as f:
    cred_data = json.loads(f.read())

api_id = cred_data["nutritionix"]["app_id"]
api_key = cred_data["nutritionix"]["api_key"]

exercise_npt = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id":api_id,
    "x-app-key":api_key
}

parameters ={
    "query":(input("Tell me which exercise you did? ")).lower(),
    "gender":GENDER,
    "weight_kg":WEIGHT,
    "height_cm":HEIGHT,
    "age":AGE
}

response = requests.post(url=exercise_npt,json=parameters,headers=headers)
response.raise_for_status()
data = response.json()


sheetty_npt = "https://api.sheety.co/ba5d13a527b6b1b1e451f0ca98c50390/workoutsTracking/workouts"
sheety_token = cred_data["sheety"]["token"]
headers = {
    "Authorization": f"Bearer {sheety_token}",
    "Content-Type": "application/json"
}

date = dt.datetime.now().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%X")
for d in data['exercises']:
    body = {
        'workout':
        {
            'date':date,
            'time':time,
            'exercise':d['name'].title(),
            'duration':d['duration_min'],
            'calories':d['nf_calories']
        }
    }
    print(body)
    response = requests.post(url=sheetty_npt,json=body,headers=headers)