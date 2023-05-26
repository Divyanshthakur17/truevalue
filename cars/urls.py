from django.urls import path, include
from . import views

urlpatterns = [
    path('newcars/',views.NewCarViews, name='newcars'),
    path('usedcars/',views.UsedCarViews, name='usedcars'),
    path('newcars/<int:pk>/',views.cardetail, name='details'),
    path('usedcars/<int:pk>/',views.usedcardetail, name='useddetails'),
    path('cart/', views.cartview, name = 'add-to-cart'),
    path('wishlist/', views.wishlist, name = 'wishlist'),
    path('add-to-wishlist/',views.addToWishlist, name = "add-to-wishlist"),
    path('delete-from-wishlist/',views.deleteFromWishlist, name = "remove-from-wishlist"),
    path('addcars/',views.addCars, name = "addcars"),
    path('ajax/load-models/', views.load_models, name='ajax_load_models'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]