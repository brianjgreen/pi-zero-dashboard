#
# Get weather data from JSON files, parse, and print
#

import json

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
    with open(f"{loc}.json", "r") as file:
        report = json.load(file)

    print(report["location"])
    for f in report["forecast"]:
        print(f"  {f['day_temp']} {f['conditions']}")
