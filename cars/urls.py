from django.urls import path
from . import views

urlpatterns = [
    path('newcars/',views.NewCarViews, name='newcars'),
    path('usedcars/',views.UsedCarViews, name='usedcars'),
    path('newcars/<int:pk>/',views.cardetail, name='details'),
    path('usedcars/<int:pk>/',views.usedcardetail, name='useddetails'),
    # path('high_to_low/',views.high_low, name='highlow'),
]