import uuid
import os

from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from apps.users.managers import CustomManager
from django.db import models



parametersForNull = {
    'null': True,
    'blank': True,
}


class Rename:
    def __init__(self, path):
        self.path = path
        
    def rename(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (uuid.uuid4(), ext)
        return os.path.join(self.path, filename)


class User(AbstractUser):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email.__str__()

    username = None
    date_joined = None
    first_name = None
    last_name = None
    last_login = None
    is_active = models.BooleanField(default=True, verbose_name="Активный?")
    is_staff = models.BooleanField(default=False, verbose_name="Админ?")
    is_superuser = models.BooleanField(default=False, verbose_name="СуперАдмин?")

    type_register = models.CharField(verbose_name="В качестве кого вы хотите посетить HIT EXPO?", max_length=300, **parametersForNull)

    company_one = models.CharField(max_length=300, verbose_name="Название компании", **parametersForNull)
    company_two = models.CharField(max_length=300, verbose_name="Юридическое название компании", **parametersForNull)

    branch = models.CharField(max_length=300, verbose_name="Отделение", **parametersForNull)
    number_of_employees = models.CharField(max_length=300, verbose_name="Количество сотрудников", **parametersForNull)
    trade = models.CharField(max_length=300, verbose_name="Отрасль (Выберите одну из представленных 'Строительство и недвижимость')", **parametersForNull)
    other_trade = models.CharField(max_length=300, verbose_name="Другое(Введите свою отрасль если не нашли среди предложенных)", **parametersForNull)
    direction = models.CharField(max_length=300, verbose_name="Направление (Напишите свой вид деятельности “Производство кирпичей”)", **parametersForNull)
    describe_company  = models.CharField(max_length=300, verbose_name="Опишите свою деятельность (товар или услугу)", **parametersForNull)

    photo_company = models.ImageField(verbose_name="Загрузите устав компании в  png или jpg", upload_to='images/company', **parametersForNull)

    ######################################            Данные о руководителе            #################################################

    name_manager = models.CharField(max_length=300, verbose_name="Ф.И.О (manager)", **parametersForNull)
    birth_manager = models.CharField(max_length=300, verbose_name="Дата рождения (manager)", **parametersForNull)
    inn_manager = models.CharField(max_length=300, verbose_name="ИНН/ИИН руководителя", **parametersForNull)
    position_manager = models.CharField(max_length=300, verbose_name="ИНН/ИИН руководителя", **parametersForNull)
    active_manager = models.CharField(max_length=300, verbose_name="Действующий на основании", **parametersForNull)

    ######################################          Контактное лицо          ##################################
    
    selection_face = models.CharField(max_length=300, verbose_name="Вы являетесь контактным лицом ?", **parametersForNull)
    name_face = models.CharField(max_length=300, verbose_name="Ф.И.О (Контактное лицо)", **parametersForNull)
    phone_face = models.CharField(max_length=300, verbose_name="Номер телефона: (Контактное лицо)", **parametersForNull)

    ################################################################################################################
    name = models.CharField(max_length=300, verbose_name="Ф.И.О", **parametersForNull)
    workEmail = models.EmailField(verbose_name="Work Email", default=None, unique=True, **parametersForNull)
    country = models.CharField(max_length=300, verbose_name="Страна", **parametersForNull)
    city = models.CharField(max_length=300, verbose_name="Город", **parametersForNull)
    birth = models.CharField(max_length=300, verbose_name="Дата рождения", **parametersForNull)
    
    workPhone = models.CharField(max_length=300, verbose_name="Телефон", **parametersForNull)
    personalPhone = models.CharField(max_length=300, verbose_name="WhatsApp", **parametersForNull)

    gos_organization = models.CharField(max_length=300, verbose_name="Организация", **parametersForNull)
    
    ####### Я заинтересован в #########

    visit = models.BooleanField(verbose_name="Посещение на HIT EXPO", default=False)
    participation = models.BooleanField(verbose_name="Участие на HIT EXPO", default=False)
    projects = models.BooleanField(verbose_name="Поиске проектов", default=False)
    other_one = models.BooleanField(verbose_name="Другое", default=False)


    ##########################      Ваши цели посещение HIT Expo?      SMI      ###############################

    smi_bool_one = models.BooleanField(verbose_name="Стать частью информационной поддержки", default=False)
    smi_bool_two = models.BooleanField(verbose_name="Знакомство с новыми компаниями", default=False)
    smi_bool_three = models.BooleanField(verbose_name="Освещение и полезная информация", default=False)
    smi_bool_four = models.BooleanField(verbose_name="Участие на пресс-конференции", default=False)


    ##########################      Что вас заинтересовала в нашей выставке?:    GOS     ###############################

    gos_bool_one = models.BooleanField(verbose_name="Присутствие инвесторов", default=False)
    gos_bool_two = models.BooleanField(verbose_name="Потенциал выставки", default=False)
    gos_bool_three = models.BooleanField(verbose_name="Развитие экономики Кыргызстана", default=False)
    gos_bool_four = models.BooleanField(verbose_name="Инвестиционные проекты", default=False)

    ########  Как вы узнали о мероприятие?   #########

    whatsapp_bool = models.BooleanField(verbose_name="Whats App", default=False)
    telegram_bool = models.BooleanField(verbose_name="Telegram", default=False)
    radio_bool = models.BooleanField(verbose_name="Радио", default=False)
    tv_bool = models.BooleanField(verbose_name="ТВ", default=False)
    instagram_bool = models.BooleanField(verbose_name="Инстаграм", default=False)
    invite_mail = models.BooleanField(verbose_name="Приглашение от организаторов по почте", default=False)
    invite_fair = models.BooleanField(verbose_name="Приглашение от экспонента выставки", default=False)
    invite_minister = models.BooleanField(verbose_name="Приглашение от Министерства / ведомства", default=False)
    message = models.BooleanField(verbose_name="Сообщение по тел/факсу от организаторов", default=False)
    ad_city = models.BooleanField(verbose_name="Наружная реклама в городе", default=False)
    other_two = models.BooleanField(verbose_name="Другое", default=False)

    ################  Какие преимущества и возможности предоставляете?     ###################

    benefits_one = models.BooleanField(verbose_name="Присутствие инвесторов", default=False)
    benefits_two = models.BooleanField(verbose_name="Присутствие государственных органов", default=False)
    benefits_three = models.BooleanField(verbose_name="Выход на мировой рынок", default=False)
    benefits_for = models.BooleanField(verbose_name="Реализация продукции", default=False)
    benefits_five = models.BooleanField(verbose_name="Возможность получения инвестиции", default=False)
    benefits_six = models.BooleanField(verbose_name="Расширение бизнеса", default=False)
    benefits_seven = models.BooleanField(verbose_name="Коммуникация с другми участниками", default=False)
    benefits_eight = models.BooleanField(verbose_name="Программа", default=False)
    benefits_nine = models.BooleanField(verbose_name="Место и формат проведения", default=False)
    benefits_ten = models.BooleanField(verbose_name="Возможность получения номинации", default=False)

    ##############################################       USER           ############################################
    
    participant_sector = models.CharField(max_length=300, verbose_name="В качестве кого вы хотите посетить HIT EXPO ?", **parametersForNull)
    
    position_main = models.CharField(max_length=300, verbose_name="Должность", **parametersForNull)

    #########################################        СМИ       #########################################
        
    image_certificate_smi = models.ImageField(verbose_name="Загрузите вашего журналистского удостоверения в  png или jpg", upload_to='images/certificate-smi', **parametersForNull)
    image_logo = models.ImageField(verbose_name="Загрузите логотип компании в png или jpg", upload_to='images/logo-smi', **parametersForNull)
    
    quantity_person_smi = models.CharField(max_length=300, verbose_name="Сколько у вас человек в команде ?", **parametersForNull)
    organization_smi = models.CharField(max_length=300, verbose_name="Полное юридическое наименование организации", **parametersForNull)
    address_one = models.CharField(max_length=300, verbose_name="Юридический адрес", **parametersForNull)
    address_two = models.CharField(max_length=300, verbose_name="Фактический адрес", **parametersForNull)
    web_site = models.CharField(verbose_name="Укажите url Веб-сайта", max_length=300, **parametersForNull)
    work_phone = models.CharField(max_length=300, verbose_name="Рабочий телефон", **parametersForNull)
    email_smi = models.EmailField(max_length=300, verbose_name="Email SMI", default=None, unique=True, **parametersForNull)
    
    smi_team = models.CharField(max_length=300, verbose_name="Сколько у вас человек в команде?", **parametersForNull)
    
    
    #############################################       Участник           ##########################################

    participation_sector = models.CharField(max_length=300, verbose_name="Выберите сектор участия (с условиями участия каждого сектора можно ознакомится)", **parametersForNull)
        
    brand = models.CharField(max_length=300, verbose_name="Наименование бренда", **parametersForNull)
    organization_participant = models.CharField(max_length=300, verbose_name="Полное юридическое наименование организации", **parametersForNull)
    name_bank = models.CharField(max_length=300, verbose_name="Наименование банка", **parametersForNull)
    
    inn = models.CharField(max_length=300, verbose_name="ИИН/ИНН(Серия патента компании)", **parametersForNull)
    orgn = models.CharField(max_length=300, verbose_name="ОГРН(Номер патента)", **parametersForNull)
    p_c = models.CharField(max_length=300, verbose_name="Р/С", **parametersForNull)
    bik = models.CharField(max_length=300, verbose_name="БИК", **parametersForNull)
    okpo = models.CharField(max_length=300, verbose_name="ОКПО", **parametersForNull)
    
    pdf_file = models.FileField(verbose_name="Загрузите свидетельство регистрации в pdf", upload_to='file/register', **parametersForNull)
    name_manager = models.CharField(max_length=300, verbose_name="Ф.И.О руководителя", **parametersForNull)
    position_participant = models.CharField(max_length=300, verbose_name="Должность (Участник)", **parametersForNull)
    description = models.TextField(verbose_name="Описание", **parametersForNull)


    email_participant = models.EmailField(max_length=300, verbose_name="Email Participant", default=None, unique=True, **parametersForNull)
    
    
    ###############################################         Контактные лица          #########################################

    name_contact_person = models.CharField(max_length=300, verbose_name="Ф.И.О (контактным лицом)", **parametersForNull)
    position_contact_person = models.CharField(max_length=300, verbose_name="Должность (контактным лицом)", **parametersForNull)
    phone_contact_person = models.CharField(max_length=300, verbose_name="Телефон (контактным лицом)", **parametersForNull)
    whatsapp_contact_person = models.CharField(max_length=300, verbose_name="WhatsApp (контактным лицом)", **parametersForNull)

    # socials
    instagram = models.CharField(verbose_name="Укажите url Instagram", max_length=300, **parametersForNull)
    facebook = models.CharField(verbose_name="Укажите url Facebook", max_length=300, **parametersForNull)
    twitter = models.CharField(verbose_name="Укажите url Twitter", max_length=300, **parametersForNull)
    
    #####################################   Investment    #################################
    
    agricultural_production = models.BooleanField(verbose_name="Производство + сельхоз", default=False)
    construction = models.BooleanField(verbose_name="Строительство", default=False)
    technique = models.BooleanField(verbose_name="Строительство + техника", default=False)
    textiles = models.BooleanField(verbose_name="Текстиль, обувь и аксессуары", default=False)
    education = models.BooleanField(verbose_name="Образование", default=False)
    medicine = models.BooleanField(verbose_name="Медицина", default=False)
    tourism = models.BooleanField(verbose_name="Туризм", default=False)
    echo = models.BooleanField(verbose_name="Эко", default=False)
    it = models.BooleanField(verbose_name="IT", default=False)
    banks = models.BooleanField(verbose_name="Банки", default=False)
    kfx = models.BooleanField(verbose_name="КФХ", default=False)
    krc = models.BooleanField(verbose_name="КРС", default=False)
    machinery = models.BooleanField(verbose_name="Машиностроение", default=False)
    industry = models.BooleanField(verbose_name="Текстильное промышленность", default=False)
    
    
    #####################################################################
    
    choose_direction_fashion = models.CharField(max_length=300, verbose_name="Выберите направление (Fashion)", **parametersForNull)
    choose_direction_food = models.CharField(max_length=300, verbose_name="Выберите направление (Food)", **parametersForNull)
    choose_direction_expert = models.CharField(max_length=300, verbose_name="Эксперт", **parametersForNull)
    
    status = models.CharField(max_length=300, verbose_name="Статус", **parametersForNull)
    manager = models.CharField(max_length=300, verbose_name="Менеджер", **parametersForNull)
    referal = models.CharField(max_length=300, verbose_name="Реферал", **parametersForNull)
    
    ####################################.       PASSWORD    #################################
    uniqueId = models.UUIDField(unique=True, verbose_name="Уникальный id", **parametersForNull)
    email = models.EmailField(max_length=200, verbose_name="Email", unique=True)

    resetPasswordUUID = models.UUIDField(verbose_name="Ссылка для восстановления пароля", **parametersForNull)
    resetPasswordDate = models.BigIntegerField(verbose_name="Время восстановления пароля", **parametersForNull)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = CustomManager()

    def save(self, force_insert=False, force_update=False, using=None,
            update_fields=None):
        if not self.id:
            self.uniqueId = uuid.uuid4()
        super(User, self).save(force_insert=False, force_update=False, using=None, update_fields=None)
