#
# Get weather data from JSON files, parse, and print
# https://www.worldweatheronline.com/weather-api/api/docs/local-city-town-weather-api.aspx
#

import json

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

for loc, addr in locations.items():
    print(f"{loc} = {addr} => {loc}.json")

    with open(f"{loc}.json", "r") as file:
        report = json.load(file)

    for i in range(NUM_OF_DAYS):
        weather = report["data"]["weather"][i]
        conditions = weather["hourly"][0]["weatherDesc"][0]["value"]
        snow = weather["totalSnow_cm"]
        if snow != "0.0":
            accum = float(snow) / 2.54
            conditions = f"Snow: {accum:.2f} in."
        print(
            f"{weather['mintempF']}{chr(176)}-{weather['maxtempF']}{chr(176)} {conditions}"
        )
