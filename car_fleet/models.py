from django.db import models
from accounts.models import CustomUser




class Car(models.Model):
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car_image = models.ImageField(upload_to ='motors', default='race.jpg')
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

    
    
class Extra(models.Model):
    car = models.ManyToManyField(Car)
    extra_1 = models.CharField(max_length= 30)
    extra_2 = models.CharField(max_length= 30)
    extra_3 = models.CharField(max_length= 30)
    extra_4 = models.CharField(max_length= 30)    
    
    def __str__(self):
        return self.extra_1       
    
    

class VehicleDescription(models.Model):
    car = models.ManyToManyField(Car)
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
    
    
    
    
 