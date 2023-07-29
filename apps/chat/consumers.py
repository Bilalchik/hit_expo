import json

from channels.generic.websocket import AsyncWebsocketConsumer

from apps.chat.models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        content = data['content']
        author_id = data['author_id']  # Предполагается, что вы отправляете идентификатор автора из фронтенда

        message = await self.create_message(author_id, content)

        await self.send(
            text_data=json.dumps({
                'author_id': message.author_id,
                'content': message.content,
                'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                'file_url': message.file.url if message.file else None,
            })
        )

    async def create_message(self, author_id, content):
        # Создаем и сохраняем сообщение в базе данных
        return Message.objects.create(author_id=author_id, content=content)
