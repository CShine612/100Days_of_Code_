import requests
from twilio.rest import Client
import config
import random


PHONE_NUMBER = config.PHONE_NUMBER
API_KEY = config.API_KEY
current_city = "Lubbock"
my_lat = 33.583580
my_lon = -101.855110
exclude = "current,minutely,daily,alerts"


def send_message(text):
    account_sid = config.account_sid
    auth_token = config.auth_token

    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=f"{text}",
                         from_=config.from_number,
                         to=PHONE_NUMBER
                     )
    print(message.sid)


params = {"lat": my_lat,
          "lon": my_lon,
          "exclude": exclude,
          "appid": API_KEY}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=params)
response.raise_for_status()

data = response.json()["hourly"]
today = [data[num]["weather"][0]["id"] for num in range(17)]
print(today)

rain = False
snow = False


for code in today:
    if code < 600 or code == 701:
        rain = True
    elif 600 <= code < 700:
        snow = True

text = False

rainy_options = ["Its going to rain today.", "🌧", "Gunna need an umbrella 😉", "RAAAAAAAIIIIIIINNN!!!!!",
                 "High chance of precipitation", "Oooooooo, it'sa rainin'", "Are you sweating? NOPE JUST RAIN"]
snowy_options = ["Its going to snow today.", "❄🌨⛄", "BRRRRRRRR. Its cold out there!", "Watch out for snow.",
                 "Careful on the roads, SNOW"]

if snow:
    text = random.choice(snowy_options)
elif rain:
    text = random.choice(rainy_options)


if text:
    send_message(text)

