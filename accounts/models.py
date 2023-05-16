from django.db import models
from image_cropping import ImageRatioField
from django.contrib.auth.models import AbstractUser
from accounts.manager import UserManager
from image_cropping import ImageRatioField, ImageCropField
# Create your models here.
class User(AbstractUser):
    username = None
    user_image = models.ImageField(upload_to="user/", blank=True, null=True)
    # crop_user_image = ImageCropField(blank=True,upload_to="user/")
    cropping = ImageRatioField('user_image', '400x400')
    user_coverimage = models.ImageField(upload_to="user/", blank=True, null=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10, unique=True)
    address = models.TextField(default='Indore')
    is_verified = models.BooleanField(default=False)
    last_login_time = models.DateTimeField(auto_now=True)
    last_logout_time = models.DateTimeField(auto_now=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


