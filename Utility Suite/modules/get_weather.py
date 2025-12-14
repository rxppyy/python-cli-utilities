import requests
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv(), override=True)
api_key = os.getenv("WEATHER_API_KEY")

def fetchWeather(city, unit):
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={unit}&appid={api_key}"
    )
    
    data = weather_data.json()

    if weather_data.status_code == 200:
        weather = data["weather"][0]["main"]
        temp = round(data["main"]["temp"])

        unit_symbol = "°F" if unit == "imperial" else "°C"

        print(
            f"\rWeather in '{city}': {weather} | Temperature: {temp}{unit_symbol}".ljust(80),
            end="",
            flush=True
        )
    else:
        print("\nCity not available or API error")

#print("API Key:", api_key)

