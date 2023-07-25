from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class ChatRoom(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_messages',
        verbose_name='Отправитель'
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='received_messages',
        verbose_name='Получатель'
    )
    last_messages = models.TextField(verbose_name='Последнее сообщение')

    def __str__(self):
        return f"{self.sender} -> {self.receiver}"

    class Meta:
        verbose_name = 'Комната для чата'
        verbose_name_plural = 'Комнаты для чата'


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='send_messages', verbose_name='Отправитель')
    chat = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages', verbose_name='Чат')
    content = models.TextField(verbose_name='Сообщение')
    file = models.FileField(upload_to='files/user_files', blank=True, null=True, verbose_name='Файл')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')

    def __str__(self):
        return f'{self.sender} --> {self.chat.receiver}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
