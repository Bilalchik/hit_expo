from django.db import models

from apps.investor.services import get_upload_path


class Investor(models.Model):
    fio = models.CharField(verbose_name='ФИО', max_length=300)
    title = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Фото представителя', upload_to=get_upload_path, null=True, blank=True)

    class Meta:
        db_table = 'investor'
        verbose_name = 'Инвестор'
        verbose_name_plural = 'Инвесторы'

    def __str__(self) -> str:
        return self.fio


class Country(models.Model):
    title = models.CharField(verbose_name='Название страны', max_length=300)
    image = models.ImageField(verbose_name='Фото флага', upload_to=get_upload_path)
    description = models.TextField(verbose_name='Описание')

    class Meta:
        db_table = 'investor_country'
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
