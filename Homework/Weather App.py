from datetime import datetime   
import requests
import math

city = input("\nChoose a city: ")
url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid=3840960a46edb04110ccd44620fc98cc"
r = requests.get(url)
citydata = r.json()
# print(f"Status code: {r.status_code}")

lat = citydata[0]['lat']
lon = citydata[0]['lon']
city = citydata[0]['name']
if 'state' in citydata[0].keys():
    state = citydata[0]['state']
else:
    state = ''
country = citydata[0]['country']

url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid=3840960a46edb04110ccd44620fc98cc'
r = requests.get(url)
data = r.json()
daily = data['daily']
# print(daily[0]) 

dates = [datetime.fromtimestamp(date['dt']) for date in daily]
days = [datetime.strftime(date, '%A') for date in dates]
datestr = [datetime.strftime(date, '%m/%d') for date in dates]
feels_like = [math.floor((temp['feels_like']['day'] - 273.15) * 9/5 + 32) for temp in daily]
lows = [math.floor((low['temp']['min'] -273.15) * 9/5 + 32) for low in daily]
highs = [math.floor((highs['temp']['max'] -273.15) * 9/5 + 32) for highs in daily]
rain = [day['pop'] for day in daily]

print(f'Location: {country} {state} {city} {lat}, {lon}')
print('Day\t\t', 'Date\t', '\tLow\t', '\tHigh\t', '\tFeels Like', '\tRain Chance')

for i in range(len(days)):
    print(f'{days[i]}  \t {datestr[i]}\t\t{lows[i]}\t\t{highs[i]}\t\t{feels_like[i]}\t\t{rain[i]:.0%}')


 