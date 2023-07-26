from django.db import models


class Members(models.Model):
    logo = models.ImageField(upload_to='media/trade_zone', verbose_name='Логотип')
    title = models.CharField(max_length=300, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'


class Opportunity(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Возможность'
        verbose_name_plural = 'Возможности'


class TradeZone(models.Model):
    block_title = models.CharField(max_length=300, verbose_name='Заглавный текст')
    header_photo = models.ImageField(upload_to='media/trade_zone', verbose_name='Заглавное фото')
    number_of_members = models.PositiveIntegerField(verbose_name='Кол-во участников')
    members = models.ManyToManyField(Members, verbose_name='Участники')
    opportunity = models.ManyToManyField(Opportunity, verbose_name='Возможности')

    def __str__(self):
        return self.block_title

    class Meta:
        verbose_name = 'Начало'
        verbose_name_plural = 'Начало'


class StandPhoto(models.Model):
    image = models.ImageField(upload_to='media/trade_zone')

    class Meta:
        verbose_name = 'Фото Стенда'
        verbose_name_plural = 'Фото Стендов'


class Additionally(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Дополнительная информация Стенда'
        verbose_name_plural = 'Дополнительная информация Стенда'


class Decor(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информация оформление Стенда'
        verbose_name_plural = 'Информация оформление Стенда'


class Stand(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    number_of_places = models.PositiveIntegerField(verbose_name='Кол-во мест')
    size = models.CharField(max_length=300, verbose_name='Размер')
    additionally = models.ManyToManyField(Additionally, verbose_name='Дополнительно')
    decor = models.ManyToManyField(Decor, verbose_name='Оформление')
    price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=12, default=0.00)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стенд'
        verbose_name_plural = 'Стенды'


class StandZone(models.Model):
    block_title = models.CharField(max_length=300, verbose_name='Заглавный текст')
    block_description = models.TextField(verbose_name='Описание')
    photo = models.ManyToManyField(StandPhoto, verbose_name='Фото Стендов')
    subtext = models.CharField(max_length=300, verbose_name='Текст об окончании бронирования')

    def __str__(self):
        return self.block_title

    class Meta:
        verbose_name = 'Зона Стенда'
        verbose_name_plural = 'Зона Стенда'


class AdditionalText(models.Model):
    title = models.CharField(max_length=300, verbose_name='Заглавный текст')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Дополнительная информация'
        verbose_name_plural = 'Дополнительные информации'


class Conditions(models.Model):
    title = models.CharField(max_length=300, verbose_name='Заглавный текст')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Условия участия'
        verbose_name_plural = 'Условия участия'


class PurchaseStage(models.Model):
    title = models.CharField(max_length=300, verbose_name='Заглавный текст')
    image = models.ImageField(upload_to='media/trade_zone', verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Этап покупки'
        verbose_name_plural = 'Этапы покупки'









