from django.contrib import admin
from .models import City
# Register your models here.

class CityAdmin(admin.ModelAdmin):
    list_display = ["city","city_code","state_code"]

admin.site.register(City,CityAdmin)
