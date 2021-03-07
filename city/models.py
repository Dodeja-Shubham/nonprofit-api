from django.db import models

# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=255)
    city_code = models.CharField(max_length=255)
    state_code = models.CharField(max_length=255)

    def __str__(self):
        return self.city
