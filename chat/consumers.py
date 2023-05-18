import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
# from django.contrib.auth import get_user_model
# from django.conf import settings
# User = settings.AUTH_USER_MODEL
from accounts.models import User
# User = get_user_model()
# print(get_user_model())
print('_______************__________')

class Chatconsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('connencted', event)
        user = self.scope['user']
        chat_room = f'user_chatroom_{user.id}'
        self.chat_room = chat_room
        await self.channel_layer.group_add(
            chat_room,
            self.channel_name
        )
        await self.send({
            'type':'websocket.accept'
        })

    async def websocket_receive(self, event):
        print('received', event)
        received_data = json.loads(event['text'])
        msg = received_data.get('message')
        sent_by_id = received_data.get('sent_by')
        send_to_id = received_data.get('send_to')
        if not msg:
            print('Error:: empty message ')
            return False
        
        sent_by_user = await self.get_user_object(sent_by_id)
        send_to_user = await self.get_user_object(send_to_id)
        
        if not sent_by_user:
            print('Error:: Sent by user is incorrect')
        if not send_to_user:
            print('Error:: Send to user is incorrect')

        other_user_chat_room = f'user_chatroom_{send_to_id}'
        self_user = self.scope['user']

        response = {
            'message':msg,
            'sent_by':self_user.id
        }
        await self.channel_layer.group_send(
            other_user_chat_room,
            {
                'type': 'chat_message',
                'text': json.dumps(response)
            }    
        )
        
        await self.channel_layer.group_send(
            self.chat_room,
            {
                'type': 'chat_message',
                'text': json.dumps(response)
            }    
        )
        
        
    async def websocket_disconnect(self, event):
        print('disconnected', event)
        
    async def chat_message(self, event):
        print('chat_message', event)
        await self.send({
            'type': 'websocket.send',
            'text': event['text']
        })


    @database_sync_to_async
    def get_user_object(self , user_id):
        qs = User.objects.filter(id = user_id)
        if qs.exists():
            obj = qs.first()
        else:
            obj = None
        return obj