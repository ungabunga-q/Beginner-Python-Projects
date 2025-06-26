"""
Weather App (uses OpenWeatherMap API)
Fetches and displays current weather for a city.
"""
import requests

def get_weather(city):
    api_key = "your_api_key_here"  # Get a free API key from openweathermap.org
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Description: {data['weather'][0]['description']}")
    else:
        print("City not found or API error.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
