from django.db import models

from apps.users.models import User


class Meeting(models.Model):
    inviter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inviter', verbose_name='Пригласитель')
    invited = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invited', verbose_name='Приглашённый')
    start = models.DateTimeField(verbose_name='Начало встречи')
    end = models.DateTimeField(verbose_name='Конец встречи')
    status = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Отказано'),
            (2, 'В ожидании'),
            (3, 'Ждут ответа'),
            (4, 'Активно'),
        ),
        default=2,
        verbose_name='Статус'
    )
    answer = models.BooleanField(default=False, verbose_name='Ответ')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f"{self.inviter} --> {self.invited}"

    class Meta:
        verbose_name = 'B2B Встреча'
        verbose_name_plural = 'B2B Встречи'
