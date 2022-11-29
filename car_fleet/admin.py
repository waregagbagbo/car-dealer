from django.contrib import admin
from .models import *
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_category','car_image','make','price','release_year','fuel','power','color')
    prepopulated_fields = {"slug": ("make",)} # mechanism which automatically adds the slug field
class CarExtraAdmin(admin.ModelAdmin):
    list_display = ('extra_1','extra_2','extra_3','extra_4')

    
admin.site.register(Car, CarAdmin)
admin.site.register(CarExtra, CarExtraAdmin)
admin.site.register(Description)
admin.site.register(Contact)
admin.site.register(Category)

