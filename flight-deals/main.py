from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

local_data = DataManager()
local_flights = FlightSearch("Rome")
notifications = NotificationManager()


def fetch_city_codes():
    city_codes = local_flights.get_iata(local_data.cities)
    writer = [(i + 2, city_code) for i, city_code in enumerate(city_codes)]
    local_data.write_codes(writer)


# fetch_city_codes()

for user in local_data.user_info:

    flight_finder = FlightSearch(user["origin"])

    flights = flight_finder.flight_search(local_data.fair_prices)
    flight_texts = []

    for flight in flights:
        flight_data = FlightData(flight)
        flight_texts.append(flight_data.text_string())

    for flight in flight_texts:
        # notifications.send_text(flight)
        notifications.send_email(flight, user["email"], user["name"])
