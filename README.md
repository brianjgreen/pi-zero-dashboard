# pi-zero-dashboard
Create an LED screen dashboard using a raspberry pi zero to display weather, air traffic, etc.

See it in action! https://youtu.be/gYM97AqxEqI

## Setup

>`git clone https://github.com/brianjgreen/pi-zero-dashboard.git`
>`cd pi-zero-dashboard/`
>`python3 -m venv .venv`
>`. .venv/bin/activate`
>`pip install -r requirements.txt`

## Required Files
Create a file for your weather api key and another file with your locations you want to find weather forecasts.

### weather_api.key
Create a test file with the name `weather_api.key` with your api key generated from: https://www.worldweatheronline.com/weather-api/
Sign up for the free option with the 100/day limit.

### locations.json
Create a JSON file with your locations in this format:
>`{`
>`    "Boston": "02110",`
>`    "NewYorkCity": "10010"`
>`}`

The key (*e.g. "Boston"*) is the name printed. The value (*e.g. "02110"*) is the postal, zipcode, or city name using the required 'q' parameter format of the API described here: https://www.worldweatheronline.com/weather-api/api/docs/local-city-town-weather-api.aspx#qparameter 

## Scripts
### get_weather.py
`get_weather_data.py` requests the weather forecast from the API and generates a JSON file for each location
>`python get_weather_data.py`

### print_weather_data.py
`print_weather_data.py` reads the generated JSON files and prints the weather forecasts
>`python print_weather_data.py`

## Crontabs
Use these example crontabs to make occasional requests for weather forecast data and to automatically start the display of the weather forecasts to a small OLED display.

## References
- https://www.worldweatheronline.com/weather-api/
- https://www.worldweatheronline.com/weather-api/api/docs/local-city-town-weather-api.asp
- https://www.amazon.com/dp/B09C5K91H7?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1
- https://pypi.org/project/luma.core/
- https://github.com/rm-hull/luma.examples.git
