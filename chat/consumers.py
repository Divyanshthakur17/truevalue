import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
# from django.contrib.auth import get_user_model
from django.conf import settings
User=settings.AUTH_USER_MODEL

# User = get_user_model()
# print(get_user_model())
print('_______************__________')
class Chatconsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('connencted', event)
        await self.send({
            'type':'websocket.accept'
        })

    async def websocket_receive(self, event):
        print('received', event)
        received_data = json.loads(event['text'])
        msg = received_data.get('message')
        if not msg:
            return False
        response = {
            'message':msg
        }
        await self.send({
            'type':'websocket.send',
            'text': json.dumps(response)
        })
        
    async def websocket_disconnect(self, event):
        print('disconnected', event)

    