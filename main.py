import requests
import os
#from pprint import pprint

API_KEY = os.environ.get('OPEN_WEATHER_MAPS_API_KEY')
units = 'imperial'

def select_location():
  location = input("Enter a location : ")
  return location

def get_location_weather(location):
    if API_KEY:
        base_url = 'http://api.openweathermap.org/data/2.5/weather?appid=' + API_KEY + '&q=' + location + '&units=' + units
        weather_data = requests.get(base_url).json()
        return weather_data
    else:
        print("Sorry, we seem to be having issues retrieving this data. Please try again later.")

location = select_location()
weather = get_location_weather(location)

print(f"In {location.title()}, the current weather is {weather['weather'][0]['description']}. The temperature is {round(weather['main']['temp'])}°F with a relative humidity level of {weather['main']['humidity']}% and wind speeds of {round(weather['wind']['speed'])} mph.")

#pprint(weather)