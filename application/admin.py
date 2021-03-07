from django.contrib import admin
from .models import Application
# Register your models here.

class ApplicationeAdmin(admin.ModelAdmin):
    list_display = ["volunteer","role_id","city","created_at"]

admin.site.register(Application,ApplicationeAdmin)