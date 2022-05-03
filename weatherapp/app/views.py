from django.shortcuts import render
import requests
import json
from django.conf import settings
import math
from datetime import datetime   



def index(request):

    if request.method == "POST":
        city = request.POST['city']

        url = (f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=' + settings.WEATHER_API_KEY)
        r = requests.get(url)
        city_data = r.json()
        time_stamp  = city_data['dt']
         

        data = {
            "name": str(city_data['name']),
            "country_code": str(city_data['sys']['country']),
            "date": str(datetime.fromtimestamp(time_stamp).strftime("%w %b")),
            "temp": str(math.floor(city_data['main']['temp'] - 273.15) * 9/5 + 32) + '°F',
            "feels_like": str(math.floor(city_data['main']['feels_like'] - 273.15) * 9/5 + 32) + '°F',
            "temp_min": str(math.floor(city_data['main']['temp_min'] - 273.15) * 9/5 + 32) + '°F',
            "main": str(city_data['weather'][0]['main']),
            "description": str(city_data['weather'][0]['description'].title()),
            "icon": str(city_data['weather'][0]['icon']),
        }
    else:
        data = {}

    return render(request, 'app/base.html', data)