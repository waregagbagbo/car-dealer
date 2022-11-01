from nturl2path import url2pathname
from django.contrib import admin
from django.urls import path
from .views import CarListView

app_name = 'car_fleet'

urlpatterns = [
    path('',CarListView.as_view(), name='home'),
]
