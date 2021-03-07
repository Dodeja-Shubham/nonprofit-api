from django.db import models
from volunteer.models import User
from role.models import Role
from city.models import City

# Create your models here.
class Application(models.Model):
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.volunteer