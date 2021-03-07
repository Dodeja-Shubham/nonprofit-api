import uuid
from django.db import models

from city.models import City

# Create your models here.
class Organization(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    city = models.ManyToManyField(City)
    contact = models.CharField(max_length=11)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('id',)