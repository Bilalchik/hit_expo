from django.db import models

from apps.other.services import get_upload_path


class Expectation(models.Model):
    title = models.CharField(verbose_name='Название', max_length=300)
    description = models.TextField(verbose_name='Описание')

    class Meta:
        db_table = 'other.expectation'
        verbose_name = 'Что вас Ожидает'
        verbose_name_plural = 'Что вас Ожидает'
    
    def __str__(self) -> str:
        return self.title


class Partner(models.Model):
    title = models.CharField(verbose_name='Название', max_length=300)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Логотип', upload_to=get_upload_path, blank=True, null=True)

    class Meta:
        db_table = 'other.partners'
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
    
    def __str__(self) -> str:
        return self.title


class SMI(models.Model):
    text = models.TextField(verbose_name='Текст')

    class Meta:
        db_table = 'other.smi'
        verbose_name = 'СМИ'
        verbose_name_plural = 'СМИ'
    
    def __str__(self) -> str:
        return self.text


class B2B(models.Model):
    title = models.CharField(verbose_name='Название', max_length=300)
    description = models.TextField(verbose_name='Описание')

    class Meta:
        db_table = 'other.b2b'
        verbose_name = 'B2B'
        verbose_name_plural = 'B2B'
    
    def __str__(self) -> str:
        return self.title


class News(models.Model):
    title = models.CharField(verbose_name='Название', max_length=300)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Фото', upload_to=get_upload_path, blank=True, null=True)
    date = models.DateField(verbose_name='Дата', auto_now_add=True)

    class Meta:
        db_table = 'other.news'
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self) -> str:
        return f'{self.title} - {self.date}'
