from django.shortcuts import render
import requests
from .models import City
from .models import UserCity
from .user_forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=fb1e015669fd5c36832ebb4dc1ffe5b2'

    cities = City.objects.all() #return all the cities in the database
    weather_data = []

    user_cities = UserCity.objects.all()
    users_weather_data = []

    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST)
        if form.is_valid():# add actual request data to form for processing
            form.save() # will validate and save if validate

    form = CityForm()

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) #add the data for the current city into our list

    context = {'weather_data' : weather_data, 'form' : form}
 #returns the index.html template
    for city in user_cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        users_weather_data.append(weather) #add the data for the current city into our list

    context = {'weather_data' : weather_data, 'users_weather_data': users_weather_data , 'form' : form}

    return render(request, 'weather/index.html', context)
 #returns the index.html template


def kira(requem):
    return render(requem,'weather/first_layer.html')

def majishian(requem):
    return render(requem,'weather/under_weather/under_void.html')
