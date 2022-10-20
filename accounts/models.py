from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(_('email_address'), unique=True)
    
    def __str__(self):
        return self.email    
    
    

class Car(models.Model):
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car_type = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    model_type = models.CharField(max_length= 255)
    year = models.IntegerField()
    fuel = models.CharField(max_length=255)
    engine_mode_size = models.CharField(max_length=255)
    power = models.CharField(max_length=255)
    gearbox = models.CharField(max_length=255)
    number_of_seats = models.IntegerField()
    doors = models.IntegerField()
    color = models.CharField(max_length=255)
    
    def __str__(self):
        return self.car_type  

    
    
class Extras(models.Model):
    car = models.ManyToManyField(Car, on_delete=models.CASCADE)
    extra_1 = models.CharField(max_length= 30)
    extra_2 = models.CharField(max_length= 30)
    extra_3 = models.CharField(max_length= 30)
    extra_4 = models.CharField(max_length= 30)    
    
    def __str__(self):
        return self.extra_1       
    
    

class VehicleDescription(models.Model):
    car = models.ManyToManyField(Car, on_delete=models.CASCADE)
    desc_1 = models.CharField(max_length=255)
    desc_2 = models.CharField(max_length=255)
    desc_3 = models.CharField(max_length=255)
    desc_4 = models.CharField(max_length=255)
    desc_5 = models.CharField(max_length=255)    
    
    def __str__(self):
        return self.desc_1    
    
    
class Contact(models.Model):
    dealer_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=255)
    
    def __str__(self):
        return self.dealer_name
    
    
    
    
 
