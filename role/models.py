from city.models import City
import uuid
from django.db import models
from organization.models import Organization
from city.models import City
from volunteer.models import User

# Create your models here.
class Role(models.Model):
    virtual = 'virtual'
    onground = 'onground'

    types = [
        (virtual, 'virtual'),
        (onground, 'onground')
    ]
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role_id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices= types, default=1)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    recruited = models.ManyToManyField(User, blank=True, related_name='recruited_volunteer')
    rejected = models.ManyToManyField(User, blank=True, related_name='rejected_volunteer')

    def __str__(self) -> str:
        return self.name