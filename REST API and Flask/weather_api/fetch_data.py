import requests

from config import API_KEY, CITY

def fetch_weather_data():
    url=f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {
            "error": f"Failed to fetch weather data for {CITY}. Please check the city name and API key."
        }, response.status_code
        