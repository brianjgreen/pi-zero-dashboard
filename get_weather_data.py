#
# Get weather data and place in a JSON file
# http://api.worldweatheronline.com/premium/v1/weather.ashx?key={API_KEY}&q={LOCATION}&num_of_days=5&tp=3&format=json
#

import datetime
import json

import requests

NUM_OF_DAYS = 3

#
# For locations.json, dictionary of key name and value zipcode
# {
#     "Boston": "02110",
#     "NewYorkCity": "10010"
# }
#
with open("locations.json", "r") as file:
    locations = json.load(file)

with open("weather_api.key", "r") as file:
    api_key = file.read().rstrip()

for loc, addr in locations.items():
    # print(f"{loc} = {addr} => {loc}.json")

    api_url = f"http://api.worldweatheronline.com/premium/v1/weather.ashx?key={api_key}&q={addr}&num_of_days={NUM_OF_DAYS}&tp=24&format=json"
    response = requests.get(api_url)
    weather_full = response.json()
    weather_report = {"location": loc, "forecast": []}

    # https://www.worldweatheronline.com/weather-api/api/docs/local-city-town-weather-api.aspx
    for i in range(NUM_OF_DAYS):
        weather = weather_full["data"]["weather"][i]
        conditions = weather["hourly"][0]["weatherDesc"][0]["value"]
        snow = weather["totalSnow_cm"]
        if snow != "0.0":
            # accum = float(snow) / 2.54
            # conditions = f"Snow: {accum:.2f} in."
            conditions = f"{snow}cm Snow"
        date_string = weather["date"]
        date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
        day_of_week = date_object.strftime("%A")[:3]

        weather_report["forecast"].append(
            {
                "day_temp": f"{day_of_week} {weather['mintempF']}{chr(176)}-{weather['maxtempF']}{chr(176)}",
                "conditions": conditions,
            }
        )
        # print(
        #     f"{day_of_week} {weather['mintempF']}{chr(176)}-{weather['maxtempF']}{chr(176)} {conditions}"
        # )

    with open(f"{loc}.json", "w") as f:
        json.dump(weather_report, f)
