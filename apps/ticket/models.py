from django.db import models
from apps.users.models import User


class Industry(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отрасль'
        verbose_name_plural = 'Отрасли'


class Stand(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    number_of_places = models.PositiveIntegerField(verbose_name='Кол-во мест')
    size = models.CharField(max_length=300, verbose_name='Размер')
    additionally = models.ManyToManyField(
        'trade_zone.Additionally',
        verbose_name='Дополнительно',
        related_name='additionallys')
    decor = models.ManyToManyField('trade_zone.Decor', verbose_name='Оформление', related_name='decors')
    image = models.ImageField(upload_to='media/stands', verbose_name='Фото')
    price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=12, default=0.00)
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Стенд'
        verbose_name_plural = 'Стенды'

    def __str__(self):
        return self.title


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    zone = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Trade'),
            (2, 'Invest'),
            (3, 'Fashion'),
            (4, 'Food'),
            (5, 'National'),
        ),
        verbose_name='Зона'
    )
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, verbose_name='Отрасль')
    activities = models.CharField(max_length=500, verbose_name='Деятельность')
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE, verbose_name='Стенд')
    zone_numbering = models.PositiveSmallIntegerField(verbose_name='Номер зоны')
    row = models.PositiveSmallIntegerField(verbose_name='Ряд')
    line = models.PositiveSmallIntegerField(verbose_name='Линия')
    place = models.PositiveSmallIntegerField(
        choices=(
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 'Все 4'),
        ),
        verbose_name='Место'
    )
    place_status = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Gold'),
            (2, 'Silver'),
            (3, 'Standart'),
            (4, 'Шатер Invest zone'),
            (5, 'Шатер Trade zone'),
        ),
        verbose_name='Статус места'
    )
    photo = models.ImageField(upload_to='media/ticket/check', blank=True, null=True, verbose_name='Чек')
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    status = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Не оплачено'),
            (2, 'В обработке'),
            (3, 'Успешно'),
        ),
        default=1,
        verbose_name='Статус'
    )

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты на покупку стендов'
