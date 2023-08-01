from django.db import models


class Advantage(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'


class FoodZone(models.Model):
    block_title = models.CharField(max_length=300, verbose_name='Заглавный текст')
    header_photo = models.ImageField(upload_to='media/food_zone', verbose_name='Заглавное фото')
    advantage = models.ManyToManyField(to=Advantage, related_name='food_zone_advantage')
    
    def __str__(self):
        return self.block_title
    

class Terms(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')

    class Meta:
        db_table = 'terms'
        verbose_name = 'Название'
        verbose_name_plural = 'Название'
        
    def __str__(self):
        return self.title

class Meta:
    verbose_name = 'Название'
    verbose_name_plural = 'Название '


class ParticipationSteps(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='media/food_zone', verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'participation_steps'
        verbose_name = 'Этап участия'
        verbose_name_plural = 'Этапы участия'