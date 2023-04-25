from django.contrib import admin
from .models import NewCars, Brand, Model, UsedCars
# Register your models here.

admin.site.register(NewCars)
admin.site.register(UsedCars)
admin.site.register(Brand)
admin.site.register(Model)