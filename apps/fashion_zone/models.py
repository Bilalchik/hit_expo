from django.db import models


class Opportunity(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Возможность'
        verbose_name_plural = 'Возможности'


class FashionZone(models.Model):
    block_title = models.CharField(max_length=300, verbose_name='Заглавный текст')
    header_photo = models.ImageField(upload_to='media/invest_zone', verbose_name='Заглавное фото')
    number_of_members = models.PositiveIntegerField(verbose_name='Кол-во участников')
    opportunity = models.ManyToManyField(Opportunity, verbose_name='Возможности')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.block_title

    class Meta:
        verbose_name = 'Начало'
        verbose_name_plural = 'Начало'


class BracketsZone(models.Model):
    title = models.CharField(max_length=300, verbose_name='Заголовок')
    subtext = models.TextField(verbose_name='Подописание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Зона Кронштейна'
        verbose_name_plural = 'Зона Кронштейна'


class Possibility(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Возможность'
        verbose_name_plural = 'Возможности'


class Brackets(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    number_of_places = models.PositiveIntegerField(verbose_name='Кол-во мест')
    possibility = models.ManyToManyField(Possibility, verbose_name='Возможности')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=12, default=0.00)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Возможность'
        verbose_name_plural = 'Возможности'


class AdditionalInformation(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Дополнительная информация'
        verbose_name_plural = 'Дополнительная информация'


class AdvantagesZone(models.Model):
    block_title = models.CharField(max_length=300, verbose_name='Заголовок')

    def __str__(self):
        return self.block_title

    class Meta:
        verbose_name = 'Зона Преимущества'
        verbose_name_plural = 'Зона Преимущества'


class Advantages(models.Model):
    title = models.CharField(max_length=300, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='media/invest_zone', verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Преимущества'
        verbose_name_plural = 'Преимущества'


class Stage(models.Model):
    title = models.CharField(max_length=300, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Этап'
        verbose_name_plural = 'Этапы'
