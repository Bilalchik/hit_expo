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

    class Meta:
        db_table = 'investor_country'
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self) -> str:
        return self.title


class Text(models.Model):
    description = models.TextField(verbose_name='Описание сайта')

    class Meta:
        db_table = 'investor_text'
        verbose_name = 'Описание'
        verbose_name_plural = 'Описание'


class Organizer(models.Model):
    
    class Meta: 
        verbose_name = 'Об организаторах'
        verbose_name_plural = 'Об организаторах'
    
    title = models.CharField(verbose_name='Название  предпринимателей', max_length=999)
    icon = models.ImageField(verbose_name='Фото иконки' , blank=True , null=True)
    link = models.URLField(verbose_name='Инстаграм', blank=True , null=True)
    url = models.URLField(verbose_name = 'Сайт', max_length=300 ,blank=True , null=True)
    text = models.TextField(verbose_name='Описание сайта')
    galary = models.ImageField(verbose_name='Фото Галерея ')


class Sponsors(models.Model):
    
    class Meta:
        verbose_name = 'Спонсоры'
        verbose_name_plural = 'Спонсоры'
    
    text_one = models.TextField(verbose_name='текст описание', max_length=300)
    icon_one = models.ImageField(verbose_name='Иконка')
    description = models.TextField(verbose_name='Описание сайта' , max_length=300)
    