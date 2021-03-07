from django.contrib import admin
from .models import User
from django.contrib.sites.models import Site
from django.contrib import auth

from rest_framework.authtoken.models import TokenProxy
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialApp, SocialToken, SocialAccount

# Register your models here.
admin.site.site_title = "Wedogood Admin Portal"
admin.site.site_header = "Wedogood Admin"

class UserAdmin(admin.ModelAdmin):
    fields = ("email","name","phone","title","dob","img_url","location","city","occupation")
    list_display = ["id","title","name","phone","email","dob"]

admin.site.register(User, UserAdmin)
admin.site.unregister(Site)
admin.site.unregister(auth.models.Group)
admin.site.unregister(TokenProxy)
admin.site.unregister(SocialApp)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(EmailAddress)