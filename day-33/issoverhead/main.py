import requests
from datetime import datetime
import math, smtplib, json, time

# load email cred
with open("../cred.json") as f:
    jsonf = f.read()
cred_object = json.loads(jsonf)

my_email = cred_object["email"]
password = cred_object["password"]

MY_LAT = -37.785000 # Your latitude
MY_LONG = 145.315002 # Your longitude
TIME_ZONE = 10

#Your position is within +5 or -5 degrees of the ISS position.
def is_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    lat_diff = abs(math.floor(MY_LAT - iss_latitude))
    lng_diff = abs(math.floor(MY_LONG - iss_longitude))
    if lat_diff <= 5 and lng_diff <=5:
        return True
    else:
        return False

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour-TIME_ZONE
    if sunset <= hour_now <= sunrise:
        return True
    else:
        return False

while True:
    if is_above() and is_dark():
        with smtplib.SMTP("smtp.mail.yahoo.com",port=587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr=my_email,to_addrs=my_email,msg="Subject:Look up👆!\n\nThe iss is above you!"
            )
    time.sleep(60)



