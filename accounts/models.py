from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.manager import UserManager
# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10, unique=True)
    address = models.TextField(default='Indore')
    is_verified = models.BooleanField(default=False)
    last_login_time = models.DateTimeField(auto_now=True)
    last_logout_time = models.DateTimeField(auto_now=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []