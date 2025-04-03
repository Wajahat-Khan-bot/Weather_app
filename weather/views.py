from django.shortcuts import render, redirect
import requests
from .models import City

def index(request):
    print(request.POST)
    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            ci = City.objects.create(name = city)

    cities = City.objects.all().order_by('-id')[:2] #return all the cities in the database

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
        
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) #add the data for the current city into our list , 'form' : form
    
    context = {'weather_data' : weather_data}

    return render(request, 'weather/index.html', context) #returns the index.html template