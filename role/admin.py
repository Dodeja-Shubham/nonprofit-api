from django.contrib import admin
from .models import Role
# Register your models here.

class RoleAdmin(admin.ModelAdmin):
    list_display = ["role_id","organization","role_id","name"]

admin.site.register(Role,RoleAdmin)