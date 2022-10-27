from nturl2path import url2pathname
from django.contrib import admin
from django.urls import path
from .views import IndexView

app_name = 'car_fleet'

urlpatterns = [
    path('',IndexView.as_view(), name='home'),
]
