from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField




CAR_CATEGORY =[
    ('1', 'Used_Car'),
    ('2','New_Car'),      
    
]

CAR_MAKES = [
    ('Aston','Aston Martin'),
    ('Audi','Audi'),
    ('Gmc','Gmc'),
    ('Bentley','Bentley'),
    ('Bmw','Bmw'),
    ('Chevrolet','Chevrolet'),
    ('Cardilac','Cardilac'),
    ('Citroen','Citroen'),
    ('Hyundai','Hyundai'),
    ('Jaguar','Jaguar'),
    ('Lexus','Lexus'),
    ('Mercedes','Mercedes'),
    ('Nissan','Nissan'),
]


CAR_MANUFACTURER =[
    ('Envoy','Envoy'),
    ('Jimmy','Jimmy'),
    ('Saturn','Saturn'),
    ('Savanna','Savanna'),
    ('Sierra','Siera'),
    ('Yukom','Sonoma'),
]

    
class CarExtra(models.Model):
    extra_1 = models.CharField(max_length= 30)
    extra_2 = models.CharField(max_length= 30)
    extra_3 = models.CharField(max_length= 30)
    extra_4 = models.CharField(max_length= 30)    
    
    def __str__(self):
        return '%s,%s,%s' % (self.extra_1),(self.extra_2), (self.extra_3),(self.extra_4)
    

class Contact(models.Model):
    dealer= models.CharField(max_length=30)
    avatar = models.ImageField(upload_to="media/profiles", null=True)
    phone_number = PhoneNumberField()
    
    def __str__(self):
        return self.dealer
        return '%s'% (self.dealer_name)        
    
    

class Description(models.Model):
    desc_1 = models.CharField(max_length=255)
    desc_2 = models.CharField(max_length=255)
    desc_3 = models.CharField(max_length=255)
    desc_4 = models.CharField(max_length=255)
    desc_5 = models.CharField(max_length=255)    
    
    def __str__(self):
        return '%s,%s,%s,%s,%s'% (self.desc_1,self.desc_2,self.desc_3,self.desc_4,self.desc_5) 
    
 

class Category(models.Model):
    name = models.CharField(max_length=255, choices=CAR_CATEGORY, default='used_car')
    slug = models.SlugField(null=True, unique= True)
    
    def __str__(self):
        return self.name  
    
    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})        
       
    
    
class Car(models.Model):
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car_image = models.ImageField(upload_to ='motors', default='race.jpg')
    car_category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    make = models.CharField(max_length=255, choices=CAR_MAKES)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    model_type = models.CharField(max_length= 255, choices=CAR_MANUFACTURER)
    release_year = models.DateField(null=True)
    fuel = models.CharField(max_length=255)
    engine_mode_size = models.CharField(max_length=255)
    power = models.CharField(max_length=255)
    gearbox = models.CharField(max_length=255)
    number_of_seats = models.IntegerField()
    doors = models.IntegerField()
    color = models.CharField(max_length=255)
    description = models.ManyToManyField(Description)
    extra =  models.ManyToManyField(CarExtra)
    slug = models.SlugField(null=True)
    contact = models.ForeignKey(Contact,on_delete=models.CASCADE, null=True)    
    
    
    class Meta:
        ordering = ["-make"]        
    
    def __str__(self):
        return str(self.car_category) + ":$" + str(self.price) + "$" + str(self.make) 
    
    # fetches relative path to the actual object in detailview  
    #def get_absolute_url(self):
      #  return reverse("car", kwargs={'slug': self.slug})

    
    
    

    
    


    
    
    
    
    
    
 