# Generated by Django 4.2.3 on 2023-07-21 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный?')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Админ?')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='СуперАдмин?')),
                ('type_register', models.CharField(blank=True, max_length=300, null=True, verbose_name='В качестве кого вы хотите посетить HIT EXPO?')),
                ('company_one', models.CharField(blank=True, max_length=300, null=True, verbose_name='Название компании')),
                ('company_two', models.CharField(blank=True, max_length=300, null=True, verbose_name='Юридическое название компании')),
                ('branch', models.CharField(blank=True, max_length=300, null=True, verbose_name='Отделение')),
                ('number_of_employees', models.CharField(blank=True, max_length=300, null=True, verbose_name='Количество сотрудников')),
                ('trade', models.CharField(blank=True, max_length=300, null=True, verbose_name="Отрасль (Выберите одну из представленных 'Строительство и недвижимость')")),
                ('other_trade', models.CharField(blank=True, max_length=300, null=True, verbose_name='Другое(Введите свою отрасль если не нашли среди предложенных)')),
                ('direction', models.CharField(blank=True, max_length=300, null=True, verbose_name='Направление (Напишите свой вид деятельности “Производство кирпичей”)')),
                ('describe_company', models.CharField(blank=True, max_length=300, null=True, verbose_name='Опишите свою деятельность (товар или услугу)')),
                ('photo_company', models.ImageField(blank=True, null=True, upload_to='images/company', verbose_name='Загрузите устав компании в  png или jpg')),
                ('birth_manager', models.CharField(blank=True, max_length=300, null=True, verbose_name='Дата рождения (manager)')),
                ('inn_manager', models.CharField(blank=True, max_length=300, null=True, verbose_name='ИНН/ИИН руководителя')),
                ('position_manager', models.CharField(blank=True, max_length=300, null=True, verbose_name='ИНН/ИИН руководителя')),
                ('active_manager', models.CharField(blank=True, max_length=300, null=True, verbose_name='Действующий на основании')),
                ('selection_face', models.CharField(blank=True, max_length=300, null=True, verbose_name='Вы являетесь контактным лицом ?')),
                ('name_face', models.CharField(blank=True, max_length=300, null=True, verbose_name='Ф.И.О (Контактное лицо)')),
                ('phone_face', models.CharField(blank=True, max_length=300, null=True, verbose_name='Номер телефона: (Контактное лицо)')),
                ('name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Ф.И.О')),
                ('workEmail', models.EmailField(blank=True, default=None, max_length=254, null=True, unique=True, verbose_name='Work Email')),
                ('country', models.CharField(blank=True, max_length=300, null=True, verbose_name='Страна')),
                ('city', models.CharField(blank=True, max_length=300, null=True, verbose_name='Город')),
                ('birth', models.CharField(blank=True, max_length=300, null=True, verbose_name='Дата рождения')),
                ('workPhone', models.CharField(blank=True, max_length=300, null=True, verbose_name='Телефон')),
                ('personalPhone', models.CharField(blank=True, max_length=300, null=True, verbose_name='WhatsApp')),
                ('gos_organization', models.CharField(blank=True, max_length=300, null=True, verbose_name='Организация')),
                ('visit', models.BooleanField(default=False, verbose_name='Посещение на HIT EXPO')),
                ('participation', models.BooleanField(default=False, verbose_name='Участие на HIT EXPO')),
                ('projects', models.BooleanField(default=False, verbose_name='Поиске проектов')),
                ('other_one', models.BooleanField(default=False, verbose_name='Другое')),
                ('smi_bool_one', models.BooleanField(default=False, verbose_name='Стать частью информационной поддержки')),
                ('smi_bool_two', models.BooleanField(default=False, verbose_name='Знакомство с новыми компаниями')),
                ('smi_bool_three', models.BooleanField(default=False, verbose_name='Освещение и полезная информация')),
                ('smi_bool_four', models.BooleanField(default=False, verbose_name='Участие на пресс-конференции')),
                ('gos_bool_one', models.BooleanField(default=False, verbose_name='Присутствие инвесторов')),
                ('gos_bool_two', models.BooleanField(default=False, verbose_name='Потенциал выставки')),
                ('gos_bool_three', models.BooleanField(default=False, verbose_name='Развитие экономики Кыргызстана')),
                ('gos_bool_four', models.BooleanField(default=False, verbose_name='Инвестиционные проекты')),
                ('whatsapp_bool', models.BooleanField(default=False, verbose_name='Whats App')),
                ('telegram_bool', models.BooleanField(default=False, verbose_name='Telegram')),
                ('radio_bool', models.BooleanField(default=False, verbose_name='Радио')),
                ('tv_bool', models.BooleanField(default=False, verbose_name='ТВ')),
                ('instagram_bool', models.BooleanField(default=False, verbose_name='Инстаграм')),
                ('invite_mail', models.BooleanField(default=False, verbose_name='Приглашение от организаторов по почте')),
                ('invite_fair', models.BooleanField(default=False, verbose_name='Приглашение от экспонента выставки')),
                ('invite_minister', models.BooleanField(default=False, verbose_name='Приглашение от Министерства / ведомства')),
                ('message', models.BooleanField(default=False, verbose_name='Сообщение по тел/факсу от организаторов')),
                ('ad_city', models.BooleanField(default=False, verbose_name='Наружная реклама в городе')),
                ('other_two', models.BooleanField(default=False, verbose_name='Другое')),
                ('benefits_one', models.BooleanField(default=False, verbose_name='Присутствие инвесторов')),
                ('benefits_two', models.BooleanField(default=False, verbose_name='Присутствие государственных органов')),
                ('benefits_three', models.BooleanField(default=False, verbose_name='Выход на мировой рынок')),
                ('benefits_for', models.BooleanField(default=False, verbose_name='Реализация продукции')),
                ('benefits_five', models.BooleanField(default=False, verbose_name='Возможность получения инвестиции')),
                ('benefits_six', models.BooleanField(default=False, verbose_name='Расширение бизнеса')),
                ('benefits_seven', models.BooleanField(default=False, verbose_name='Коммуникация с другми участниками')),
                ('benefits_eight', models.BooleanField(default=False, verbose_name='Программа')),
                ('benefits_nine', models.BooleanField(default=False, verbose_name='Место и формат проведения')),
                ('benefits_ten', models.BooleanField(default=False, verbose_name='Возможность получения номинации')),
                ('participant_sector', models.CharField(blank=True, max_length=300, null=True, verbose_name='В качестве кого вы хотите посетить HIT EXPO ?')),
                ('position_main', models.CharField(blank=True, max_length=300, null=True, verbose_name='Должность')),
                ('image_certificate_smi', models.ImageField(blank=True, null=True, upload_to='images/certificate-smi', verbose_name='Загрузите вашего журналистского удостоверения в  png или jpg')),
                ('image_logo', models.ImageField(blank=True, null=True, upload_to='images/logo-smi', verbose_name='Загрузите логотип компании в png или jpg')),
                ('quantity_person_smi', models.CharField(blank=True, max_length=300, null=True, verbose_name='Сколько у вас человек в команде ?')),
                ('organization_smi', models.CharField(blank=True, max_length=300, null=True, verbose_name='Полное юридическое наименование организации')),
                ('address_one', models.CharField(blank=True, max_length=300, null=True, verbose_name='Юридический адрес')),
                ('address_two', models.CharField(blank=True, max_length=300, null=True, verbose_name='Фактический адрес')),
                ('web_site', models.CharField(blank=True, max_length=300, null=True, verbose_name='Укажите url Веб-сайта')),
                ('work_phone', models.CharField(blank=True, max_length=300, null=True, verbose_name='Рабочий телефон')),
                ('email_smi', models.EmailField(blank=True, default=None, max_length=300, null=True, unique=True, verbose_name='Email SMI')),
                ('smi_team', models.CharField(blank=True, max_length=300, null=True, verbose_name='Сколько у вас человек в команде?')),
                ('participation_sector', models.CharField(blank=True, max_length=300, null=True, verbose_name='Выберите сектор участия (с условиями участия каждого сектора можно ознакомится)')),
                ('brand', models.CharField(blank=True, max_length=300, null=True, verbose_name='Наименование бренда')),
                ('organization_participant', models.CharField(blank=True, max_length=300, null=True, verbose_name='Полное юридическое наименование организации')),
                ('name_bank', models.CharField(blank=True, max_length=300, null=True, verbose_name='Наименование банка')),
                ('inn', models.CharField(blank=True, max_length=300, null=True, verbose_name='ИИН/ИНН(Серия патента компании)')),
                ('orgn', models.CharField(blank=True, max_length=300, null=True, verbose_name='ОГРН(Номер патента)')),
                ('p_c', models.CharField(blank=True, max_length=300, null=True, verbose_name='Р/С')),
                ('bik', models.CharField(blank=True, max_length=300, null=True, verbose_name='БИК')),
                ('okpo', models.CharField(blank=True, max_length=300, null=True, verbose_name='ОКПО')),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='file/register', verbose_name='Загрузите свидетельство регистрации в pdf')),
                ('name_manager', models.CharField(blank=True, max_length=300, null=True, verbose_name='Ф.И.О руководителя')),
                ('position_participant', models.CharField(blank=True, max_length=300, null=True, verbose_name='Должность (Участник)')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('email_participant', models.EmailField(blank=True, default=None, max_length=300, null=True, unique=True, verbose_name='Email Participant')),
                ('name_contact_person', models.CharField(blank=True, max_length=300, null=True, verbose_name='Ф.И.О (контактным лицом)')),
                ('position_contact_person', models.CharField(blank=True, max_length=300, null=True, verbose_name='Должность (контактным лицом)')),
                ('phone_contact_person', models.CharField(blank=True, max_length=300, null=True, verbose_name='Телефон (контактным лицом)')),
                ('whatsapp_contact_person', models.CharField(blank=True, max_length=300, null=True, verbose_name='WhatsApp (контактным лицом)')),
                ('instagram', models.CharField(blank=True, max_length=300, null=True, verbose_name='Укажите url Instagram')),
                ('facebook', models.CharField(blank=True, max_length=300, null=True, verbose_name='Укажите url Facebook')),
                ('twitter', models.CharField(blank=True, max_length=300, null=True, verbose_name='Укажите url Twitter')),
                ('agricultural_production', models.BooleanField(default=False, verbose_name='Производство + сельхоз')),
                ('construction', models.BooleanField(default=False, verbose_name='Строительство')),
                ('technique', models.BooleanField(default=False, verbose_name='Строительство + техника')),
                ('textiles', models.BooleanField(default=False, verbose_name='Текстиль, обувь и аксессуары')),
                ('education', models.BooleanField(default=False, verbose_name='Образование')),
                ('medicine', models.BooleanField(default=False, verbose_name='Медицина')),
                ('tourism', models.BooleanField(default=False, verbose_name='Туризм')),
                ('echo', models.BooleanField(default=False, verbose_name='Эко')),
                ('it', models.BooleanField(default=False, verbose_name='IT')),
                ('banks', models.BooleanField(default=False, verbose_name='Банки')),
                ('kfx', models.BooleanField(default=False, verbose_name='КФХ')),
                ('krc', models.BooleanField(default=False, verbose_name='КРС')),
                ('machinery', models.BooleanField(default=False, verbose_name='Машиностроение')),
                ('industry', models.BooleanField(default=False, verbose_name='Текстильное промышленность')),
                ('choose_direction_fashion', models.CharField(blank=True, max_length=300, null=True, verbose_name='Выберите направление (Fashion)')),
                ('choose_direction_food', models.CharField(blank=True, max_length=300, null=True, verbose_name='Выберите направление (Food)')),
                ('choose_direction_expert', models.CharField(blank=True, max_length=300, null=True, verbose_name='Эксперт')),
                ('status', models.CharField(blank=True, max_length=300, null=True, verbose_name='Статус')),
                ('manager', models.CharField(blank=True, max_length=300, null=True, verbose_name='Менеджер')),
                ('referal', models.CharField(blank=True, max_length=300, null=True, verbose_name='Реферал')),
                ('uniqueId', models.UUIDField(blank=True, null=True, unique=True, verbose_name='Уникальный id')),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='Email')),
                ('resetPasswordUUID', models.UUIDField(blank=True, null=True, verbose_name='Ссылка для восстановления пароля')),
                ('resetPasswordDate', models.BigIntegerField(blank=True, null=True, verbose_name='Время восстановления пароля')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]