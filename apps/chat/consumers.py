import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from apps.chat.models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data: dict):
        data: dict = json.loads(text_data)
        message: str = data.get('message')
        file: bytes = data.get('file')

        if file:
            await self.save_file_to_message(file, message)

        await self.save_message_to_db(message)
        await self.send(text_data=json.dumps({
            'message': message,
            'file': file 
        }))

    @database_sync_to_async
    def save_message_to_db(self, message):
        author = self.scope['user']
        Message.objects.create(author=author, content=message)

    @database_sync_to_async
    def save_file_to_message(self, file_data, message):
        author = self.scope['user']
        Message.objects.create(author=author, content=message, file=file_data)
