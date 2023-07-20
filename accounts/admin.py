from django.contrib import admin
from .models import *


model_list = [Account,UserProfile]
# Register your models here.

for model in model_list:
    admin.site.register(model)






