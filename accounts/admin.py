from django.contrib import admin
from .models import *
# Register your models here.
class UserAccount(admin.ModelAdmin):
    list_display = ('username','email','first_name','last_name')

admin.site.register(CustomUser, UserAccount)
