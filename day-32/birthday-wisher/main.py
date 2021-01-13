import datetime as dt
import smtplib, random, json
from os import listdir
import pandas as pd

# load email credentials
with open("../cred.json") as f:
    jsonf = f.read()
cred_object = json.loads(jsonf)

my_email = cred_object["email"]
password = cred_object["password"]

# load templates
template_path = "letter_templates/"
template_list = listdir(template_path)

# get today date
now = dt.datetime.now()

# load birthday to_csv
bdays = pd.read_csv("birthdays.csv")

# grab row that match today datetime
bd_list = [data_row for (index, data_row) in bdays.iterrows() if (data_row["month"]==now.month and data_row["day"]==now.day)]

# find out if any one has birthday today
with smtplib.SMTP("smtp.mail.yahoo.com",port=587) as connection:
    connection.starttls()
    connection.login(my_email, password)
    
    for bday in bd_list:
        if now.day == bday.day and now.month == bday.month:
            template = random.choice(template_list)
            with open(f"{template_path}{template}") as f:
                message_body = f.read()
            message_body = message_body.replace("[NAME]",bday["name"])
            connection.sendmail(
                from_addr=my_email,
                to_addrs=bday["email"],
                msg=f"Subject:Happy Birthday {bday['name']}!!!!\n\n{message_body}"
            )
            print(message_body)
