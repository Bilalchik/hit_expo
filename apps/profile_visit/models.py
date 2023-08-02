from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Visit(models.Model):
    who = models.ForeignKey(User, on_delete=models.CASCADE, related_name='who', verbose_name='Кто')
    to_whom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_whom', verbose_name='Кому')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.who} --> {self.to_whom}"

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'
