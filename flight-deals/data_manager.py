import config
import requests


class DataManager:

    def __init__(self):
        self.fair_prices = None
        self.cities = None
        self.codes = None
        self.user_info = None
        self.headers = {"Content-Type": "application/json",
                        "Authorization": f"Bearer {config.sheety_bearer}"}
        self.endpoint_prices = "https://api.sheety.co/7f53d6a2657015c6b5b91f51775cc5d5/flightDeals/prices"
        self.endpoint_users = "https://api.sheety.co/7f53d6a2657015c6b5b91f51775cc5d5/flightDeals/users"
        self.get_data()

    def get_data(self):
        response_prices = requests.get(url=self.endpoint_prices, headers=self.headers)
        response_prices.raise_for_status()
        data_prices = response_prices.json()["prices"]
        self.cities = [item["city"] for item in data_prices]
        self.codes = [item["iataCode"] for item in data_prices]
        self.fair_prices = {item["iataCode"]: item["lowestPrice"] for item in data_prices}
        response_users = requests.get(url=self.endpoint_users, headers=self.headers)
        response_users.raise_for_status()
        data_users = response_users.json()["users"]
        self.user_info = [{"email": item["email"],
                           "origin": item["startLocation"],
                           "name": item["firstName"]} for item in data_users]

    def write_codes(self, data):
        for item in data:
            response = requests.put(self.endpoint_prices + f"/{item[0]}",
                                    json={"price": {"iataCode": f"{item[1]}"}},
                                    headers=self.headers)
            response.raise_for_status()
