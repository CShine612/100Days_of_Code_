class FlightData:

    def __init__(self, flight):
        self.data = flight
        self.origin_city = flight["cityFrom"]
        self.origin_iata = flight["flyTo"]
        self.dest_city = flight["cityTo"]
        self.dest_iata = flight["flyFrom"]
        self.price = f"€{flight['conversion']['EUR']}"
        self.departure_date = flight["local_departure"][:10]
        self.departure_time = flight["local_departure"][11:16]



    def text_string(self):
        text_string = f"Low price alert! Only {self.price} to fly from {self.origin_city}-{self.origin_iata} to " \
                      f"{self.dest_city}-{self.dest_iata}, leave on {self.departure_date} at {self.departure_time}."
        return text_string
