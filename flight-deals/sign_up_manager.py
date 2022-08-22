import config
import requests


class SignUp:

    def __init__(self):
        self.headers = {"Content-Type": "application/json",
                        "Authorization": f"Bearer {config.sheety_bearer}"}
        self.endpoint = "https://api.sheety.co/7f53d6a2657015c6b5b91f51775cc5d5/flightDeals/users"

    def post_user_info(self, row):
        put_response = requests.post(f"{self.endpoint}", json=row, headers=self.headers)
        put_response.raise_for_status()

    def get_user_info(self):
        first_name = input("Please enter your first name: ")
        second_name = input("Please enter your second name: ")
        start_location = input("Please enter your preferred city of origin: ")
        while True:
            email = input("Please enter your email address: ")
            confirmation_email = input("Please confirm your email address: ")
            if email == confirmation_email:
                break
        self.post_user_info({"user": {"firstName": first_name,
                                      "secondName": second_name,
                                      "startLocation": start_location,
                                      "email": email}})
        print("Congratulations, your email has been added to the mail list")


test = SignUp()
test.get_user_info()
