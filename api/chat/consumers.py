
import json

from asgiref.sync import sync_to_async, async_to_sync
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer

# from django.contrib.auth import get_user_model
from .models import (
    ChatSession, ChatSessionMember, ChatSessionMessage, deserialize_user, User
)


async def save_message(message, user, uri):
    print('here')
    print(message, user, uri)


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user_json = text_data_json['user']
        uri = text_data_json['uri']

        user = User.objects.get(username=user_json['username'])
        chat_session = ChatSession.objects.get(uri=uri)

        ChatSessionMessage.objects.create(
            user=user, chat_session=chat_session, message=message
        )

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': {
                    'message': message,
                    'user': deserialize_user(user),
                },
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
