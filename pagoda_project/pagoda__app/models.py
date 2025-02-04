from django.db import models


class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self): #show the actual city name on the dashboard
        return self.name

    class Meta: #show the plural of city as cities instead of cities
        verbose_name_plural = 'cities'


class UserCity(models.Model):
    name = models.CharField(max_length=25,unique=True)

    def __str__(self): #show the actual city name on the dashboard
        return self.name

    class Meta: #show the plural of city as cities instead of cities
        verbose_name_plural = 'user_cities'
