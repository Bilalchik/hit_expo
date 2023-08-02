from django.db import models

from apps.users.models import User


class Message(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='message_user')
    content = models.TextField()
    file = models.FileField(upload_to='chat_files/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}: {self.content}'
