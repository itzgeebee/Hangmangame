# A program that gets the weather information of your coordinates from openweathermap and sends a notification when it will rain

API_KEY = "Your API key for open weather"

import requests
from twilio.rest import Client



account_sid = "your twilio sid"
auth_token = 'your twilio auth token'
client = Client(account_sid, auth_token)
parameters={
    "lat": "your latitude",
    "lon": "your longitude",
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?", params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_weather = weather_data["hourly"]
next_12_hours = hourly_weather[:12]
will_rain = False
for i in range(len(next_12_hours)):
    update = (next_12_hours[i]["weather"][0]["id"])
    if 1 < 700:
        will_rain = True

if will_rain:
    print("yes")

    client = Client(account_sid, auth_token)
    message = client.messages\
        .create(
        to='destination number',
        body='🌧️. take an ☂',
        from_= 'your twilio number'
    )

    print(message.status)
