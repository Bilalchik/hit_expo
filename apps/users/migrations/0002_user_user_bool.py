# Generated by Django 3.2.9 on 2023-08-02 10:33
# Generated by Django 3.2.9 on 2023-08-02 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_bool',
            field=models.BooleanField(default=False, verbose_name='Разрешение на редактирование'),
        ),
    ]