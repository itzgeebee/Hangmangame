API_KEY = "029df595b0f53c487032e0c310c9aa18"

import requests
from twilio.rest import Client



account_sid = "ACee8c3fe70faa4a32ec52731181957340"
auth_token = '47e42d2db40539063a8a30910b9ee99a'
client = Client(account_sid, auth_token)
parameters={
    "lat": "55.755825",
    "lon": "37.617298",
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
        to='+2348169876904',
        body='🌧️. take an ☂',
        from_= '+19126008386'
    )

    print(message.status)
