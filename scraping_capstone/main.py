from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import config
import time

data = []

def get_data():
    response = requests.get(config.zwillo_search, headers=config.headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    properties = soup.find_all(name="div", class_="list-card-info")
    print(properties)

    for ind, item in enumerate(properties):
        data.append({
            "address": item.find(class_="list-card-addr").text,
            "price": item.find(class_="list-card-price").text,
            "url": item.find(name="a")["href"]
        })


def send_responses():
    for item in data:
        driver = webdriver.Chrome(config.chrome_driver)
        driver.get(config.form)

        time.sleep(2)

        address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                               '1]/div/div[1]/input')
        price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                             '1]/div/div[1]/input')
        link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                            '1]/div/div[1]/input')

        address.send_keys(item["address"])
        price.send_keys(item["price"])
        link.send_keys(item["url"])

        submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
        submit_button.click()

        driver.quit()

        time.sleep(1)

get_data()
send_responses()
