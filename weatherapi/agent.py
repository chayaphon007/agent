# weather_agent.py

import os
import requests
from google.adk.agents import Agent

# Read your OpenWeatherMap API key from env
API_KEY = os.getenv('git init85b9e21667f78746d72dd9926feecc45')

def get_current_weather(location: str) -> dict:
    """
    Fetch the current weather for a given location using OpenWeatherMap.

    Returns a dict with:
      - location: City name
      - weather: Short description
      - temperature: °C
      - feels_like: °C
      - humidity: %
      - error (optional): Error message if lookup fails
    """
    if not API_KEY:
        raise RuntimeError("Missing OPENWEATHER_API_KEY environment variable")

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": API_KEY,
        "units": "metric",
        "lang": "en"
    }

    resp = requests.get(url, params=params)
    data = resp.json()

    if resp.status_code != 200:
        return {"error": data.get("message", "Unable to fetch weather info")}

    return {
        "location": data.get("name"),
        "weather": data["weather"][0]["description"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
    }


# Expose the agent for ADK CLI to discover
root_agent = Agent(
    model="gemini-2.0-flash",
    name="weather_api_agent",
    description="Provides current weather info by calling get_current_weather().",
    instruction=(
        "You are a weather assistant. When the user asks for current weather "
        "in a city, call get_current_weather(location) and return the result."
    ),
    tools=[get_current_weather],
)
