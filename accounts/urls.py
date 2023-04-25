from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.sign_in, name='signin'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),
    path('profile/', views.user_profile, name='profile'),
]