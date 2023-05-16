from django.contrib import admin
from image_cropping import ImageCroppingMixin
from accounts.models import User

# Register your models here.
# admin.site.register(User)

class UserAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
