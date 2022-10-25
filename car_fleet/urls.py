from nturl2path import url2pathname
from django.contrib import admin
from django.urls import path
from car_fleet import views
app_name = 'car_fleet'

urlpatterns = [
    path('',views.index, name='home')
]
