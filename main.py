import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
TOKEN = os.getenv("TOKEN")
nutrition_endpoint = os.getenv("NUTRITION_ENDPOINT")
sheety_endpoint = os.getenv("SHEETY_ENDPOINT")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

headers = {
    "Content-Type": "application/json",
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

exercise = input('Tell me which exercises you did: ')

parameters = {
    "query": exercise,
    "gender": "male",
    "weight_kg": "61",
    "height_cm": "171",
    "age": 21
}
auth_header = {
    "Authorization": f"Basic {TOKEN}",
}

now = datetime.now()

response = requests.post(url=nutrition_endpoint, headers= headers, json=parameters)
response.raise_for_status()
result = response.json()

for exer in result["exercises"]:
    exercise_name = exer["name"]
    duration = exer["duration_min"]
    calories = exer["nf_calories"]
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")
    sheety_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise_name,
            "duration": duration,
            "calories": calories,
        }
    }
    sheety_response = requests.post(url=sheety_endpoint, json=sheety_params, headers=auth_header)
    sheety_response.raise_for_status()
    print(f"Logged: {exercise_name} for {duration} min, {calories} kcal")