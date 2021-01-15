import requests
import datetime
import json
import os
from twilio.rest import Client

# load api key
with open("../cred.json") as f:
    api_json = f.read()
owm_api_key = json.loads(api_json)["openweathermap"]
twilio_cred = json.loads(api_json)["twilio"]
account_sid = twilio_cred['TWILIO_ACCOUNT_SID']
auth_token = twilio_cred['TWILIO_AUTH_TOKEN']

MY_LAT = -37.785000
MY_LONG = 145.315002

def get_data():
    parameters = {
        "lat":MY_LAT,
        "lon":MY_LONG,
        "appid":owm_api_key,
        "exclude":"current,minutely,daily"
    }
    api_url=f"https://api.openweathermap.org/data/2.5/onecall"
    response = requests.get(api_url,params=parameters)
    response.raise_for_status()
    return response.json()

data = get_data()
# with open("data.json","w") as f:
#     f.write(json.dumps(data,indent=4))


data_12hr = data["hourly"][:12]
rain_code=[]
will_rain=False
for d in data_12hr:
    rain_code.extend([rf["id"] for rf in d["weather"] if rf["id"] < 700])
    if len(rain_code) > 0:
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="It's going to rain! Bring ☔",
                        from_=twilio_cred['from_number'],
                        to=twilio_cred['to_number']
                    )

print(message.status)