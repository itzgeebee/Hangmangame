# A program that utilises NLP from the nutrinix API and records your excercise statistics on a google sheet

import requests
import datetime

# nutrinix authorization credentials and endpoint
APP_ID = "YOUR ID"
API_KEY = "YOUR API KEY"
APP_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

#Sheety endpoint and authorization credentials
SHEETY_URL = "YOUR SHEETY URL"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

# create the post request parameters for nutritionix
question = input("What exercises did you do today?: ")
weight = 78
height = 180
age = 25
gender = "male"

post_params = {
    "query": question,
    "weight_kg": weight,
    "height_cm": height,
    "age": age,
    "gender": gender
}
today = datetime.datetime.now()

# post request for nutritionix
post_response = requests.post(url=APP_URL, json=post_params, headers=headers)
post_response.raise_for_status()
response_from_query = (post_response.json())
print(response_from_query)

# definte parameters to be passed into sheety. These parameters would be added to a google sheet
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")
exercise = (response_from_query['exercises'][0]["name"]).title()
duration = int(response_from_query['exercises'][0]['duration_min'])
calories = int(response_from_query['exercises'][0]['nf_calories'])


sheety_headers = {

    "Content-Type": "application/json"
}

sheety_params = {
    "workouts": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}

print(sheety_params)

# post request to sheety and populate google sheet
post_workout_details_to_sheety = requests.post(url=SHEETY_URL, json=sheety_params, headers=sheety_headers)
post_workout_details_to_sheety.raise_for_status()
print(post_workout_details_to_sheety.text)
