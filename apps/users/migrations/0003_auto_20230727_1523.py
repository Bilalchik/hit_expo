# Generated by Django 3.2.9 on 2023-07-27 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_joined',
            field=models.CharField(default=1, max_length=300, verbose_name='дата_присоединения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=1, max_length=300, verbose_name='имя_фамилия'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.CharField(default=1, max_length=300, verbose_name='последний_логин'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=1, max_length=300, verbose_name='фамилия'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=1, max_length=300, verbose_name='имя пользователя'),
            preserve_default=False,
        ),
    ]
