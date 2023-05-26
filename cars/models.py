from django.db import models
from django.utils import timezone
from accounts.models import User
from indian_cities.dj_city import cities

# Create your models here.



class Brand(models.Model):
    brand_name = models.CharField(max_length = 20)
    brand_desc = models.TextField()

    def __str__(self):
        return self.brand_name
    
class Model(models.Model):
    model_name = models.CharField(max_length = 20)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE , default=1)


    def __str__(self):
        return self.model_name + "---" + self.brand.brand_name

class State(models.Model):
    states = models.CharField(max_length=100 , null=True, blank=True )
    
    def __str__(self) -> str:
        return self.states

class Cities(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE, blank=True, null=True)
    cities = models.CharField(max_length=100, choices=cities, null=True, blank=True)

    def __str__(self) -> str:
        return self.cities

class NewCars(models.Model):
    image_1 = models.ImageField(upload_to='images/')
    image_2 = models.ImageField(upload_to='images/')
    image_3 = models.ImageField(upload_to='images/',blank=True, null=True)
    image_4 = models.ImageField(upload_to='images/',blank=True, null=True)
    image_5 = models.ImageField(upload_to='images/',blank=True, null=True)
    image_6 = models.ImageField(upload_to='images/',blank=True,null=True)
    car_name = models.CharField(max_length=100, null= True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
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
    date_added = models.DateTimeField(default=timezone.now)

    # class Meta:
        # ordering = ['-exshowroom_price']
    
    def __str__(self):
        return self.model.model_name
    

class UsedCars(models.Model):
    image_1 = models.ImageField(upload_to='images/')
    image_2 = models.ImageField(upload_to='images/')
    image_3 = models.ImageField(upload_to='images/',blank=True, null=True)
    image_4 = models.ImageField(upload_to='images/',blank=True, null=True)
    image_5 = models.ImageField(upload_to='images/',blank=True, null=True)
    image_6 = models.ImageField(upload_to='images/',blank=True,null=True)
    usedcar_name = models.CharField(max_length=100, null= True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model =models.ForeignKey(Model, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE)
    milege = models.FloatField()
    fuel_type = models.CharField(max_length=100)
    dent = models.BooleanField(default=False)
    kilometer_run = models.FloatField()
    buy_year = models.IntegerField()
    demand = models.FloatField()
    owner = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10)
    used_car_detail = models.TextField(blank=True, null=True)
    states = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
    cities = models.ForeignKey(Cities, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.brand.brand_name

  
class Commentcars(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    usedcar = models.ForeignKey(UsedCars, related_name='comment_content', on_delete=models.CASCADE)
    content = models.TextField()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cars = models.ForeignKey(UsedCars, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.cars.brand.brand_name
    

class WishItem(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cars = models.ManyToManyField(UsedCars, blank=True)
    def __str__(self):
        return self.user.first_name
    


