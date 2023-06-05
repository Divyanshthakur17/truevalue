from django.contrib import admin
from image_cropping import ImageCroppingMixin
from accounts.models import User, Export
from import_export.admin import ExportActionMixin


# Register your models here.
# admin.site.register(User)

class UserAdmin(ExportActionMixin ,ImageCroppingMixin, admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 
        'mobile', 'address',  
         'user_image', 'cropping')}),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Export)
