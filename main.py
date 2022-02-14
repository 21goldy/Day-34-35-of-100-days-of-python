from twilio.rest import Client
import requests

# twilio

account_sid = ""  # account id
auth_token = ""  # auth TOKEN

# api

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "" # API KEY

# my latitude and longitude

MY_LAT = 22.335545
MY_LONG = 77.099609
EXCLUDE = "current,minutely,daily"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": EXCLUDE,
    "appid": api_key,
}

response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

# 12 days hours
slice_hour = weather_data["hourly"][:13]
will_rain = False

for hour_data in slice_hour:
    hourly_weather_data = hour_data["weather"][0]["id"]
    condition_code = hourly_weather_data
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Hey Goldy! It may rain today... Don't forget to bring your umbrella.🌧☔",
        from_='*********',
        to='*************'
    )
    print(message.status)
