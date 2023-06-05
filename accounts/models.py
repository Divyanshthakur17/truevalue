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
    cropping = ImageRatioField('user_image', '300x300', size_warning=True)
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

class Export(models.Model):
    file = models.FileField(
        upload_to='files/', verbose_name="Fichiers Excel"
    )

    def __str__(self):
        return self.file
