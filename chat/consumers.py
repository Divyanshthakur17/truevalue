import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model

User = get_user_model()

class Chatconsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('connencted', event)

    async def websocket_receive(self, event):
        print('received', event)
        

    async def websocket_disconnect(self, event):
        print('disconnected', event)

    