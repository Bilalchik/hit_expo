from django.db import models


user_status = [
  [
    "Партнер",
    "Партнер"
  ],
  [
    "Участник",
    "Участник"
  ],
  [
    "Сми",
    "Сми"
  ],
  [
    "Спонсор",
    "Спонсор"
  ]
]


class Application(models.Model):
    
    class Meta:
        db_table = 'application'
        verbose_name = 'ПРЕДВАРИТЕЛЬНАЯ ЗАЯВКА'
        verbose_name_plural = 'ПРЕДВАРИТЕЛЬНАЯ ЗАЯВКА'
        
    name_organic = models.CharField(verbose_name="Название организации", max_length=128)
    surname = models.CharField(verbose_name="Фамилия", max_length=16)
    name = models.CharField(verbose_name="Имя", max_length=16)
    email = models.EmailField(verbose_name="E-mail", max_length=32)
    number = models.CharField(verbose_name="Телефон", max_length=16)
    user_status = models.CharField(verbose_name="Выберите направление", max_length=100, default=None, choices=user_status, blank=True, null=True)
    data = models.BooleanField(verbose_name="Я согласен на обработку моих персональных данных", default=False)
    
    def __str__(self):
        return self.name


class Feedback(models.Model):

    class Meta:
        db_table = 'feedback'
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    name = models.CharField(verbose_name="Ф.И.О", max_length=300)
    mail = models.EmailField(verbose_name="Почта", max_length=300)
    phone = models.CharField(verbose_name='Номер телефона', max_length=300)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return self.name