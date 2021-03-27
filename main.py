import requests
import os
#from pprint import pprint

API_KEY = os.environ.get('OPEN_WEATHER_MAPS_API_KEY')

def get_city_weather():
    if API_KEY:
        city = input("Enter a city: ")
        base_url = 'http://api.openweathermap.org/data/2.5/weather?appid=' + API_KEY + '&q=' + city
        weather_data = requests.get(base_url).json()
        print(f"In {city}, the current weather is {weather_data['weather'][0]['description']}, with a relative humidity level of {weather_data['main']['humidity']}% and wind speeds of {weather_data['wind']['speed']} kmph.")
    else:
        print("Sorry, we seem to be having issues retrieving this data. Please try again later.")

get_city_weather()
