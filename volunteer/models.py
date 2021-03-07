from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, phone, password=None, name=None, title=None):
        if not email:
            raise ValueError("User must have an email address")
        if not phone:
            raise ValueError("User must have phone number")
        if not name:
            raise ValueError("User must have a name")

        user = self.model(
            email = self.normalize_email(email),
            phone = phone,
            name = name,
            title = title
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, phone, password, name, title):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            phone = phone,
            name = name,
            title = title
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    mr = "Mr."
    ms = "Ms."
    mrs = "Mrs."
    title_choice = ((mr,"Mr."),(ms,"Ms."),(mrs,"Mrs."))
    name = models.CharField(max_length=255)
    email = models.EmailField(verbose_name="email",max_length=255, unique=True)
    phone = models.CharField(max_length=15,unique=True, verbose_name="phone")
    dob = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=5, choices=title_choice)
    img_url = models.ImageField(max_length=500, blank=True)
    date_joined = models.DateTimeField(verbose_name="date_joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last_login", auto_now=True)
    city = models.CharField(verbose_name="city", blank=True, max_length=255)
    location = models.CharField(verbose_name="current_location", blank=True, max_length=255)
    occupation = models.CharField(verbose_name="occupation", blank=True, max_length=255)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone","name","title"]

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
