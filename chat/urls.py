from django.urls import path
from . import views
urlpatterns = [
    path('', views.messages_page),
    path('usedcars/<int:pk>/chat/', views.send_msg, name='send_msg'),
]