import requests
from datetime import datetime
import smtplib

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

#Your position is within +5 or -5 degrees of the ISS position.

def prox_check():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"]

    return -5 < MY_LAT - iss_latitude < 5 and -5 < MY_LONG - iss_longitude < 5


# Check if its dark
def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    return sunrise > time_now.hour or time_now.hour > sunset



#If the ISS is close to my current position and it is currently dark

if prox_check() and is_dark():
    my_email = "cshinepython@gmail.com"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(my_email, "Castlebar0205")
    connection.sendmail(my_email, "karissavb@gmail.com", msg="Look up\n\n The ISS is passing over head")

# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



