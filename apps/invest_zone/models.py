from django.db import models


class Advantage(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'


class InvestZone(models.Model):
    block_title = models.CharField(max_length=300, verbose_name='Заглавный текст')
    header_photo = models.ImageField(upload_to='media/invest_zone', verbose_name='Заглавное фото')
    number_of_members = models.PositiveIntegerField(verbose_name='Кол-во участников')
    advantage = models.ManyToManyField(Advantage, verbose_name='Преимущества')

    def __str__(self):
        return self.block_title

    class Meta:
        verbose_name = 'Начало'
        verbose_name_plural = 'Начало'


class StandZone(models.Model):
    subtext = models.CharField(max_length=300, verbose_name='Текст об окончании бронирования')

    def __str__(self):
        return self.subtext

    class Meta:
        verbose_name = 'Зона Стенда'
        verbose_name_plural = 'Зона Стенда'


class Terms(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Условия у Стенда'
        verbose_name_plural = 'Условия у Стендов'


class Stand(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    number_of_places = models.PositiveIntegerField(verbose_name='Кол-во мест')
    terms = models.ManyToManyField(Terms, verbose_name='Условия у Стенда')
    price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=12, default=0.00)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стенд'
        verbose_name_plural = 'Стенды'


class GeneralAdvantages(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='media/invest_zone', verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Общие Преимущества'
        verbose_name_plural = 'Общие Преимущества'


class Conditions(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    signing = models.CharField(max_length=300, verbose_name='Подописание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Условия участия'
        verbose_name_plural = 'Условия участия'


class ParticipationSteps(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='media/invest_zone', verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Этап участия'
        verbose_name_plural = 'Этапы участия'
