from django.urls import path
from . import consumers
print('^^^^^^^^<<<<<<<<<') 
websocket_urlpatterns = [
    path('chat/',consumers.Chatconsumer.as_asgi()),
]