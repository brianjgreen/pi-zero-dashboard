#
# Get weather data and place in a JSON file
# http://api.worldweatheronline.com/premium/v1/weather.ashx?key={API_KEY}&q={LOCATION}&num_of_days=5&tp=3&format=json
#

import json
import requests

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
    print(f"{loc} = {addr} => {loc}.json")

    api_url = f"http://api.worldweatheronline.com/premium/v1/weather.ashx?key={api_key}&q={addr}&num_of_days=3&tp=24&format=json"
    response = requests.get(api_url)
    weather = response.json()

    with open(f"{loc}.json", "w") as f:
        json.dump(weather, f)
