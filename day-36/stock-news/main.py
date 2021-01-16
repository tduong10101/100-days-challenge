from alphavantage import Alphavantage
from newsapi import Newsapi
import json
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
DOWN_ICON = "🔻"
UP_ICON = "🔺"

with open("../cred.json") as f:
    api_json = f.read()
twilio_cred = json.loads(api_json)["twilio"]
account_sid = twilio_cred['TWILIO_ACCOUNT_SID']
auth_token = twilio_cred['TWILIO_AUTH_TOKEN']

tesla_obj = Alphavantage()
tesla_data = tesla_obj.time_series_daily_adjusted(STOCK)

diff_per = tesla_obj.prev_diff_percentage(tesla_data)

if diff_per > 5 or diff_per < -5:
    if diff_per < 0:
        icon = DOWN_ICON
    else:
        icon = UP_ICON
    newsapi = Newsapi()
    tesla_news = newsapi.get_news(keyword=COMPANY_NAME,page_size=3)
    message_body = f"{STOCK}: {icon}{abs(diff_per)}%\n"
    for n in tesla_news:
        message_body += f"\nHeadline: {n['title']}\nBrief: {n['description']}\n"
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=f"{message_body}",
                        from_=f'{twilio_cred["from_number"]}',
                        to=f'{twilio_cred["to_number"]}'
                    )

    print(message.status)
