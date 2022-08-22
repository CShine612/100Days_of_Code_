import config
import requests
import datetime

now = datetime.datetime.now()
time = now.strftime("%H:%M:%S")
date = now.strftime("%d/%m/%Y")

exercise = input("What exercises did you do today? ")

headers = {"x-app-id": config.nutritionix_id,
          "x-app-key": config.nutritionix_key}

nutri_params = {"query": exercise}

response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", json=nutri_params, headers=headers)
response.raise_for_status()
print(response.text)

data = response.json()["exercises"]

sheety_headers = {"Content-Type": "application/json",
                  "Authorization": f"Bearer {config.sheety_bearer}"}

rows_to_add = [{"date": date,
               "time": time,
               "exercise": item["name"].title(),
               "duration": item["duration_min"],
               "calories": str(item["nf_calories"])} for item in data]


sheety_endpoint = "https://api.sheety.co/7f53d6a2657015c6b5b91f51775cc5d5/myWorkouts/workouts"

for item in rows_to_add:
    row_formatted = {"workout": item}
    response = requests.post(sheety_endpoint, json=row_formatted, headers=sheety_headers)
    response.raise_for_status()
    print(response.text)

