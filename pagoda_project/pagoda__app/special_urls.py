from django.urls import path
from . import views

urlpatterns = [
    path('', views.kira),
    path('layer_TeleVision/', views.majishian),
    path('nagai_shita/', views.saientisuto),  #the path for our index view
]
