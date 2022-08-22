import dateutil.relativedelta
import config
import requests
import datetime

# destination_list = ['Paris', 'Berlin', 'Tokyo', 'Sydney', 'Istanbul', 'Kuala Lumpur', 'New York', 'San Francisco',
#                     'Cape Town']


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, origin):
        self.headers = {'accept': 'application/json',
                        'apikey': config.tequila_api_key}
        self.endpoint = "https://tequila-api.kiwi.com/"
        self.origin = self.get_iata([origin])[0]
        delta_day = dateutil.relativedelta.relativedelta(days=1)
        now = datetime.datetime.now() + delta_day
        self.start_date = now.strftime("%d/%m/%Y")
        delta = dateutil.relativedelta.relativedelta(months=6)
        future = now + delta
        self.end_date = future.strftime("%d/%m/%Y")

    def get_iata(self, locations):
        iata = []
        for place in locations:
            query = {"term": place,
                     "location_types": "city",
                     }
            response = requests.get(url=f"{self.endpoint}locations/query", params=query, headers=self.headers)
            response.raise_for_status()
            data = response.json()["locations"][0]["code"]
            iata.append(data)
        return iata

    def flight_search(self, fair_prices: dict):
        flights = []
        for place in list(fair_prices.keys()):
            price = fair_prices[place]

            query = {"fly_from": self.origin,
                     "fly_to": place,
                     "date_from": self.start_date,
                     "date_to": self.end_date,
                     "adults": "2",
                     "adult_hold_bag": "1,0",
                     "adult_cabin_bag": "1,1",
                     "only_weekends": "true",
                     "price_to": price,
                     "max_stopovers": "1",
                     "curr": "EUR"
                     }
            search_response = requests.get(url=f"{self.endpoint}v2/search", params=query, headers=self.headers)
            search_response.raise_for_status()
            data = search_response.json()["data"]
            if len(data) > 1:
                flights.append(data[0])
            elif len(data) == 0:
                pass
            else:
                flights.append(data)
        return flights
