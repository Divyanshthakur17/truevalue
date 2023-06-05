from django.urls import path
from . import views
urlpatterns = [
    path('', views.chatroom, name='send_msg'),
    path('notification-count/', views.notification_count, name='notification_count'),
    path('update_notification/', views.update_notification, name='update_notification'),
]