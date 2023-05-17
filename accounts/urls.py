from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.sign_in, name='signin'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path("password_reset_confirm/", views.resetpassword, name="password_reset_confirm"),
    path("password_reset_complete/", views.resetpassword_complete, name="password_reset_complete")
]