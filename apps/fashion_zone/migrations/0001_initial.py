# Generated by Django 4.2.3 on 2023-07-26 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Дополнительная информация',
                'verbose_name_plural': 'Дополнительная информация',
            },
        ),
        migrations.CreateModel(
            name='Advantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='media/invest_zone', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Преимущества',
                'verbose_name_plural': 'Преимущества',
            },
        ),
        migrations.CreateModel(
            name='AdvantagesZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_title', models.CharField(max_length=300, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Зона Преимущества',
                'verbose_name_plural': 'Зона Преимущества',
            },
        ),
        migrations.CreateModel(
            name='BracketsZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Заголовок')),
                ('subtext', models.TextField(verbose_name='Подописание')),
            ],
            options={
                'verbose_name': 'Зона Кронштейна',
                'verbose_name_plural': 'Зона Кронштейна',
            },
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Возможность',
                'verbose_name_plural': 'Возможности',
            },
        ),
        migrations.CreateModel(
            name='Possibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Возможность',
                'verbose_name_plural': 'Возможности',
            },
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Этап',
                'verbose_name_plural': 'Этапы',
            },
        ),
        migrations.CreateModel(
            name='FashionZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_title', models.CharField(max_length=300, verbose_name='Заглавный текст')),
                ('header_photo', models.ImageField(upload_to='media/invest_zone', verbose_name='Заглавное фото')),
                ('number_of_members', models.PositiveIntegerField(verbose_name='Кол-во участников')),
                ('description', models.TextField(verbose_name='Описание')),
                ('opportunity', models.ManyToManyField(to='fashion_zone.opportunity', verbose_name='Возможности')),
            ],
            options={
                'verbose_name': 'Начало',
                'verbose_name_plural': 'Начало',
            },
        ),
        migrations.CreateModel(
            name='Brackets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('number_of_places', models.PositiveIntegerField(verbose_name='Кол-во мест')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Цена')),
                ('possibility', models.ManyToManyField(to='fashion_zone.possibility', verbose_name='Возможности')),
            ],
            options={
                'verbose_name': 'Возможность',
                'verbose_name_plural': 'Возможности',
            },
        ),
    ]
