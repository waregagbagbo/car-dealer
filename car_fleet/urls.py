from nturl2path import url2pathname
from django.contrib import admin
from django.urls import path
from .views import CarListView,CarDetailAccessView

app_name = 'car_fleet'

urlpatterns = [
    path('',CarListView.as_view(), name='home'),
    path('<slug:slug>/',CarDetailAccessView.as_view(), name='car'),
]