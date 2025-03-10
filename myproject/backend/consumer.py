import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatMessage
from asgiref.sync import sync_to_async 

from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """ 连接 WebSocket 并加入房间 """
        # self.user = self.scope["user"]
        self.room_name=self.scope['url_route']['kwargs']['chat_room']
        print(self.room_name)
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        """ 断开 WebSocket 连接 """
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        """ 处理接收到的消息 """
        data = json.loads(text_data)
        print(data)
        sender = data["sender"]
        receiver = data["receiver"]
        content = data["content"]
        # Save message to database (fixed with sync wrapper)
        await self.save_message(self.room_name,sender, receiver, content)

        # 发送消息到房间
        await self.channel_layer.group_send(
            self.room_name,
            {
                "type": "chat_message",
                "sender": sender,
                "content": content,
            }
        )

    async def chat_message(self, event):
        """ 发送消息到 WebSocket """
        await self.send(text_data=json.dumps({
            "sender": event["sender"],
            "content": event["content"],
        }))
        
    @sync_to_async  # 🚀 This makes it work in async!
    def save_message(self, room_name,sender, receiver, content):
        """Save message to the database safely in async mode."""
        ChatMessage.objects.create(chat_id=room_name,sender_id=sender, receiver_id=receiver, content=content)