from django.db import models

# Create your models here.

# brand =tate_choices = (
#     ("Hyundai","Hyundai"),
#     ("Kia","Kia"),
#     ("Mahindra","Mahindra"),
#     ("Toyota","Toyota"),
#     ("Honda","Honda"),
#     ("Maruti Suzuki","Maruti Suzuki"),
#     ("Tata Motors","Tata Motors"),
#     ("Renault","Renault"),
#     ("Honda","Honda"),
#     ("Honda","Honda"),
# )


class Brand(models.Model):
    brand_name = models.CharField(max_length = 20)
    brand_desc = models.TextField()

    def __str__(self):
        return self.brand_name
    
class Model(models.Model):
    model_name = models.CharField(max_length = 20)
    model_desc = models.TextField()

    def __str__(self):
        return self.model_name


class NewCars(models.Model):
    image_1 = models.ImageField(upload_to='images/')
    image_2 = models.ImageField(upload_to='images/')
    image_3 = models.ImageField(upload_to='images/',blank=True, null=True)
    image_4 = models.ImageField(upload_to='images/',blank=True, null=True)
    image_5 = models.ImageField(upload_to='images/',blank=True, null=True)
    image_6 = models.ImageField(upload_to='images/',blank=True,null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model =models.ForeignKey(Model, on_delete=models.CASCADE)
    engine = models.CharField(max_length=100)
    milege = models.FloatField()
    fuel_type = models.CharField(max_length=100)
    seat_capacity = models.IntegerField()
    body_type = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    fuel_tank_capacity = models.FloatField()
    exshowroom_price = models.IntegerField()
    onroad_price = models.IntegerField()
    car_detail = models.TextField(blank=True, null=True)
    
    

class UsedCars(models.Model):
    image_1 = models.ImageField(upload_to='images/')
    image_2 = models.ImageField(upload_to='images/')
    image_3 = models.ImageField(upload_to='images/',blank=True, null=True)
    image_4 = models.ImageField(upload_to='images/',blank=True, null=True)
    image_5 = models.ImageField(upload_to='images/',blank=True, null=True)
    image_6 = models.ImageField(upload_to='images/',blank=True,null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model =models.ForeignKey(Model, on_delete=models.CASCADE)
    milege = models.FloatField()
    fuel_type = models.CharField(max_length=100)
    dent = models.BooleanField(default=False)
    kilometer_run = models.FloatField()
    buy_year = models.IntegerField()
    demand = models.FloatField()
    owner = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10)
    used_car_detail = models.TextField(blank=True, null=True)

