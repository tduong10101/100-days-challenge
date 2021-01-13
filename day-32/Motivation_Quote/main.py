import datetime as dt
import smtplib,random,json

with open("../cred.json") as f:
    jsonf = f.read()
cred_object = json.loads(jsonf)

my_email = cred_object["email"]
password = cred_object["password"]

with open("quotes.txt",encoding="utf8") as f:
    quotes = f.readlines()
    
quote_of_the_day = random.choice(quotes)
now = dt.datetime.now()
if now.weekday() == 0:
    with smtplib.SMTP("smtp.mail.yahoo.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="tduong1010111@gmail.com",
            msg=f"Subject:Quote of the day  - {now.date()}\n\n{quote_of_the_day}".encode("utf8")
    )