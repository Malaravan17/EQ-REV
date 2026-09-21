import requests

from config.settings import URL


def CurrentWeather(latitude: float, longitude: float):

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
    }

    response = requests.get(URL, params=params)

    weather = response.json()

    current = weather["current"]

    advice = Weather_Advice(
        current["temperature_2m"],
        current["relative_humidity_2m"],
        current["weather_code"]
    )

    return {
        "latitude": latitude,
        "longitude": longitude,
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"],
        "weather_code": current["weather_code"],
        "advice": advice
    }


def Weather_Advice(temperature, humidity, weather_code):

    advice = []

    if weather_code == 61:
        advice.append(
            "Rain expected."
        )

    if humidity > 85:
        advice.append(
            "High humidity."
        )

    if temperature > 35:
        advice.append(
            "High temperature."
        )

    if len(advice) == 0:
        advice.append(
            "Normal."
        )

    return advice