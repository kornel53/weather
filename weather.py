#! /usr/bin/python3

import sys, requests, json

def get_location():
    print('Detecting your location...')
    ipSite = requests.get('http://ip-api.com/json')
    ipSite.raise_for_status()
    ip = json.loads(ipSite.text)
    ipInfo = ip['city'] + ', ' + ip['regionName']
    return ipInfo

if len(sys.argv) > 1:
    location = ' '.join(sys.argv[1:])
else:
    location = get_location()
    
urlWeather = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=1&appid=bd5e378503939ddaee76f12ad7a97608' % (location)

weatherSite = requests.get(urlWeather)
weatherSite.raise_for_status()
weatherData = json.loads(weatherSite.text)
w = weatherData['list']
print('Weather prediction for %s' % location)
print()
print('Today:')
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print('Temperature: ' + str(round(float((w[0]['temp']['day']))-273)) + ' C')
print('Pressure: ' + str(w[0]['pressure']) + ' hPa')
print('Humidity: ' + str(w[0]['humidity']) + '%')
