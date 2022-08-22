import requests
from bs4 import BeautifulSoup
import smtplib
import config

PRODUCT_URL = "https://www.amazon.com/Corsair-Wireless-Premium-Headset-Surround/dp/B07XF2TGGK"
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0",
           "Accept-Language": "en-US"}
PRODUCT_TARGET_PRICE = "90.00"

response = requests.get(PRODUCT_URL, headers=HEADERS)
response.raise_for_status()

html = response.text
soup = BeautifulSoup(html, "html.parser")
price_table = soup.find(name="div", id="corePrice_desktop")
price_span = price_table.find(name="span", class_="a-price a-text-price a-size-medium apexPriceToPay")
price = price_span.find_all(name="span")[-1].getText()



if float(price[1:]) < float(PRODUCT_TARGET_PRICE):
    message = f"A product is below your target purchase price of ${PRODUCT_TARGET_PRICE}." \
              f"\n Please find it at the following location: {PRODUCT_URL}"


    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()

    connection.login(config.my_email, config.password)

    connection.sendmail(config.my_email, config.k_email, msg=f"subject:Low Price Alert\n\n {message}")
