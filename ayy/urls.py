from django.contrib import admin
from django.urls import path,include

from . import views

app_name = "ayy"

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('flight', views.flight, name='flight'),
    path('hotel', views.hotel, name='hotel'),
    path('tour', views.tour, name='tour'),
    path('cruise', views.cruise, name='cruise'),
    path('car', views.car, name='car'),
    path('flightdetail', views.flightdetail, name='flightdetail'),
    path('hoteldetail', views.hoteldetail, name='hoteldetail'),
    path('tourdetail', views.tourdetail, name='tourdetail'), 
]



