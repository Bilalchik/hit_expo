from django.db import models

from apps.users.models import User


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_message_user')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='chat_files/', blank=True, null=True)

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'chat'
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
