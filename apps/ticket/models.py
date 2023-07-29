from django.db import models

from apps.ticket.services import get_upload_path, validate_file_extension


class Ticket(models.Model):
    title = models.CharField('Название', max_length=300)
    description = models.TextField('Описание')
    payment_rekvizit = models.CharField('Реквизиты', max_length=300)
    icon = models.ImageField('Иконка', upload_to=get_upload_path)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'ticket'
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'

class Check(models.Model):
    chek_photo = models.ImageField('Фото чека', upload_to=get_upload_path, validators=[validate_file_extension], blank=True, null=True)

    class Meta:
        db_table = 'ticket.check'
        verbose_name = 'Чек'
        verbose_name_plural = 'Чеки'
