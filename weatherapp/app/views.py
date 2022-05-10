from django.shortcuts import render
import requests
import json
from django.conf import settings
import math
from datetime import datetime   



def index(request):

    if request.method == "POST":
        city = request.POST['city']
        url = (f'https://api.openweathermap.org/geo/1.0/direct?q={city}&appid=' + settings.WEATHER_API_KEY)
        r = requests.get(url)
        data = r.json()

        lat = data[0]['lat']
        lon = data[0]['lon']

        url = (f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid=' + settings.WEATHER_API_KEY)
        r = requests.get(url)
        city_data = r.json()

        time_stamp  = city_data['list'][0]['dt']
        next_day = city_data['list'][8]['dt']
        next_day2 = city_data['list'][16]['dt']
        next_day3 = city_data['list'][24]['dt']
        next_day4 = city_data['list'][32]['dt']
 


        data = {
            "name": str(data[0]['name']),
            "state": str(data[0]['state']),
            "country_code": str(data[0]['country']),
            "date": str(datetime.fromtimestamp(time_stamp).strftime("%A, %b %d")),
            "temp": str(int(math.floor(city_data['list'][0]['main']['temp'] - 273.15) * 9/5 + 32)) + '°F',
            "lows": str(int(math.floor(city_data['list'][0]['main']['temp_min'] - 273.15) * 9/5 + 32)) + '°F',
            "highs": str(int(math.floor(city_data['list'][0]['main']['temp_max'] - 273.15) * 9/5 + 32)) + '°F',
            "feels_like": str(int(math.floor(city_data['list'][0]['main']['feels_like'] - 273.15) * 9/5 + 32)) + '°F',
            "main": str(city_data['list'][0]['weather'][0]['main']),
            "description": str(city_data['list'][0]['weather'][0]['description'].title()),
            "icon": str(city_data['list'][0]['weather'][0]['icon']),

            # This Week's Weather
            # Day One
            "next_day": str(datetime.fromtimestamp(next_day).strftime("%a \t")),
            "next_temp": str(int(math.floor(city_data['list'][8]['main']['temp'] - 273.15) * 9/5 + 32)) + '°',
            "next_main": str(city_data['list'][8]['weather'][0]['main']),
            "next_icon": str(city_data['list'][8]['weather'][0]['icon']),
            
            # Day Two
            "next_day2": str(datetime.fromtimestamp(next_day2).strftime("%a \t")),
            "next_temp2": str(int(math.floor(city_data['list'][16]['main']['temp'] - 273.15) * 9/5 + 32)) + '°',
            "next_main2": str(city_data['list'][16]['weather'][0]['main']),
            "next_icon2": str(city_data['list'][16]['weather'][0]['icon']),

            # Day Three
            "next_day3": str(datetime.fromtimestamp(next_day3).strftime("%a \t")),
            "next_temp3": str(int(math.floor(city_data['list'][24]['main']['temp'] - 273.15) * 9/5 + 32)) + '°',
            "next_main3": str(city_data['list'][24]['weather'][0]['main']),
            "next_icon3": str(city_data['list'][24]['weather'][0]['icon']),

            # Day Four
            "next_day4": str(datetime.fromtimestamp(next_day4).strftime("%a \t")),
            "next_temp4": str(int(math.floor(city_data['list'][32]['main']['temp'] - 273.15) * 9/5 + 32)) + '°',
            "next_main4": str(city_data['list'][32]['weather'][0]['main']),
            "next_icon4": str(city_data['list'][32]['weather'][0]['icon']),
        }
    else:
        data = {}

    return render(request, 'app/base.html', data)