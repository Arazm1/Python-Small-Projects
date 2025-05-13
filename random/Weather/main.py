import json
import requests
from datetime import datetime

hakusana = input("Anna paikkakunta: ").lower().capitalize()

API_key = "" #Your API Key --- Get it from: https://openweathermap.org/
pyynto = f"http://api.openweathermap.org/geo/1.0/direct?q={hakusana}&limit=5&appid={API_key}"

try:
    vastaus = requests.get(pyynto)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        lat = json_vastaus[0]['lat']
        lon = json_vastaus[0]['lon']

        saapyynto = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
        saavastaus = requests.get(saapyynto)
        if saavastaus.status_code == 200:
            saa = saavastaus.json()

            lampotila_k = saa['main']['temp']
            lampotila_c = lampotila_k - 273.15
            saakuvaus = saa['weather'][0]['description']

            if -20 < lampotila_c < 0:
                emoji = "❄️"
            elif 0 <= lampotila_c <= 10:
                emoji = "🧥"
            elif 10 < lampotila_c <= 20:
                emoji = "🌤️"
            elif 20 < lampotila_c <= 30:
                emoji = "☀️"
            elif lampotila_c <= -30:
                emoji = "You might wanna stay at home 🥶"
            elif -30 < lampotila_c <= -20:
                emoji = "☃️"
            else:
                emoji = "🔥"

            sunrise = saa['sys']['sunrise']
            sunset = saa['sys']['sunset']
            current_time = saa['dt']

            def is_daytime(current, sunrise, sunset):
                return sunrise <= current <= sunset

            daytime = is_daytime(current_time, sunrise, sunset)
            day_or_night = "Day" if daytime else "Night"

            print(f"Sää paikkakunnalla {hakusana}: {saakuvaus.capitalize()} ({day_or_night})")
            print(f"Lämpötila: {lampotila_c:.2f}°C {emoji}")

except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")
