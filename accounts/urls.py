from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.SignIn.as_view(), name='signin'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.Signup.as_view(), name='register'),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path("password_reset_confirm/", views.resetpassword, name="password_reset_confirm"),
    path("password_reset_complete/", views.resetpassword_complete, name="password_reset_complete"),
    path("user-list/", views.export_view, name="user-list")

]