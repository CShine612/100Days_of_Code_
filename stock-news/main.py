import config
import requests
import datetime
from twilio.rest import Client

STOCK = "ETRN"
COMPANY_NAME = "Equitrans Midstream"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

date = datetime.date.today()
today = date - datetime.timedelta(days=1)
yesterday = today - datetime.timedelta(days=1)

alpha_params = {"apikey": config.alpha_api_key,
                "function": "TIME_SERIES_DAILY",
                "symbol": STOCK}


price_response = requests.get("https://www.alphavantage.co/query", params=alpha_params)
price_response.raise_for_status()
print(price_response.json())
price_data = price_response.json()["Time Series (Daily)"]
today_price = price_data[f"{today}"]["4. close"]
yesterday_price = price_data[f"{yesterday}"]["4. close"]

percentage_change = ((float(today_price)/float(yesterday_price)) * 100) -100
text_percentage = round(percentage_change, 2)

text = False

if percentage_change > 5:
    text = f"{STOCK}: 📈{text_percentage}% 🚀\n"
elif percentage_change < -5:
    text = f"{STOCK}: 📉{text_percentage}% 🤷‍\n"

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news_params = {"qInTitle": COMPANY_NAME,
               "sortBy": "publishedAt",
               "language": "en"}

news_headers = {"X-Api-Key": config.news_api_key}

news_response = requests.get("https://newsapi.org/v2/everything", params=news_params, headers=news_headers)
news_response.raise_for_status()

news_data = news_response.json()["articles"][:3]

article_list = [f"Headline: {item['title']}\n Brief: {item['content']}\n URL: {item['url']}" for item in news_data]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

client = Client(config.account_sid, config.auth_token)
for item in article_list:
    message = client.messages \
                    .create(
                         body=f"{text}{item}",
                         from_='+16065175616',
                         to=config.PHONE_NUMBER
                     )
    print(message.sid)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

