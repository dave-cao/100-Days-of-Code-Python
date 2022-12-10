import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

# date variables
today = datetime.now()
date_string = today.strftime("%d/%m/%Y")
time_string = today.strftime("%H:%M:%S")

# Interacting with Nutr api
API_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("API_KEY")

headers = {"x-app-id": API_ID, "x-app-key": APP_KEY, "Content-Type": "application/json"}
nutr_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_config = {
    "query": input("Tell me which exercises you did! "),
    "gender": "male",
    "weight_kg": 86,
    "height_cm": 183,
    "age": 23,
}

response = requests.post(url=nutr_endpoint, headers=headers, json=exercise_config)
exercises = response.json()["exercises"]

# Interacting with sheety api
sheety_endpoint = os.getenv("SHEET_ENDPOINT")

# Post exercises into google sheet based on user input
sheety_headers = {"Authorization": f"Bearer {os.getenv('TOKEN')}"}
for exercise in exercises:
    sheety_data = {
        "workout": {
            "date": date_string,
            "time": time_string,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    response = requests.post(
        url=sheety_endpoint, json=sheety_data, headers=sheety_headers
    )
    print(response)
