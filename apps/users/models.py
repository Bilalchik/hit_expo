import uuid, os

from django.contrib.auth.models import AbstractUser
from apps.users.managers import CustomManager
from django.db import models

from .choices import Organization


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


class UserType(models.IntegerChoices):
    MASS_MEDIA = 1, "СМИ"
    VISITOR = 2, "ПОСЕТИТЕЛЬ"
    EXPERT = 3, "ЭКСПЕРТ"
    GOV_USER = 4, "ГОС-ОРГАНЫ"


class User(AbstractUser):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользовати"

    def __str__(self):
        return self.email.__str__()

    username = None
    date_joined = None
    first_name = None
    last_name = None
    last_login = None

    ####################################.       PASSWORD    #################################
    user_type = models.PositiveSmallIntegerField(choices=UserType.choices, default=UserType.VISITOR, verbose_name="Тип пользователя")
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





class UserSMI(User):

    class Meta:
        verbose_name = "Пользователь СМИ"
        verbose_name_plural = "Пользователи СМИ"

    def __str__(self):
        return self.email.__str__()

    image_certificate = models.ImageField(verbose_name="Загрузите вашего журналистского удостоверения в  png или jpg", upload_to='images/certificate-smi', **parametersForNull)
    image_logo = models.ImageField(verbose_name="Загрузите логотип компании в png или jpg", upload_to='images/logo-smi', **parametersForNull)
    quantity_person = models.CharField(max_length=300, verbose_name="Сколько у вас человек в команде ?", **parametersForNull)
    name_organization = models.CharField(max_length=300, verbose_name="Полное юридическое наименование организации", **parametersForNull)
    address = models.CharField(max_length=300, verbose_name="Юридический адрес", **parametersForNull)
    web_site = models.CharField(verbose_name="Веб-сайт", max_length=300, **parametersForNull)
    email_company = models.EmailField(verbose_name="Email компании", max_length=300, **parametersForNull)
    phone = models.BigIntegerField(verbose_name="Телефон", **parametersForNull)

    #_____________________SOCIAL SITE____________________________________________________________________________
    instagram = models.CharField(verbose_name="Instagram", max_length=300, **parametersForNull)
    facebook = models.CharField(verbose_name="Facebook", max_length=300, **parametersForNull)
    twitter = models.CharField(verbose_name="Twitter", max_length=300, **parametersForNull)

    ########  Как вы узнали о мероприятие?   #########
    whatsapp_bool = models.BooleanField(verbose_name="WhatsApp", default=False)
    telegram_bool = models.BooleanField(verbose_name="Telegram", default=False)
    radio_bool = models.BooleanField(verbose_name="Радио реклама", default=False)
    tv_bool = models.BooleanField(verbose_name="ТВ", default=False)
    instagram_bool = models.BooleanField(verbose_name="Инстаграм", default=False)
    invite_mail = models.BooleanField(verbose_name="Приглашение от организаторов по почте", default=False)
    invite_fair = models.BooleanField(verbose_name="Приглашение от экспонента выставки", default=False)
    invite_minister = models.BooleanField(verbose_name="Приглашение от Министерства / ведомства", default=False)
    message = models.BooleanField(verbose_name="Сообщение по тел/факсу от организаторов", default=False)
    ad_city = models.BooleanField(verbose_name="Наружная реклама в городе", default=False)

    ##########################      Ваши цели посещение HIT Expo?      SMI      ###############################
    smi_bool_one = models.BooleanField(verbose_name="Стать частью информационной поддержки", default=False)
    smi_bool_two = models.BooleanField(verbose_name="Знакомство с новыми компаниями", default=False)
    smi_bool_three = models.BooleanField(verbose_name="Освещение и полезная информация", default=False)
    smi_bool_four = models.BooleanField(verbose_name="Участие на пресс-конференции", default=False)


class Expert(User):

    class Meta:
        verbose_name = "Пользователь ЭКСПЕРТ"
        verbose_name_plural = "Пользователи ЭКСПЕРТ"

    def __str__(self):
        return self.full_name.__str__()

    full_name = models.CharField(verbose_name="Ф.И.О", max_length=300)
    phone = models.BigIntegerField(verbose_name="Телефон", **parametersForNull)

    ########  Как вы узнали о мероприятие?   #########
    whatsapp_bool = models.BooleanField(verbose_name="WhatsApp", default=False)
    telegram_bool = models.BooleanField(verbose_name="Telegram", default=False)
    radio_bool = models.BooleanField(verbose_name="Радио реклама", default=False)
    tv_bool = models.BooleanField(verbose_name="ТВ", default=False)
    instagram_bool = models.BooleanField(verbose_name="Инстаграм", default=False)
    invite_mail = models.BooleanField(verbose_name="Приглашение от организаторов по почте", default=False)
    invite_fair = models.BooleanField(verbose_name="Приглашение от экспонента выставки", default=False)
    invite_minister = models.BooleanField(verbose_name="Приглашение от Министерства / ведомства", default=False)
    message = models.BooleanField(verbose_name="Сообщение по тел/факсу от организаторов", default=False)
    ad_city = models.BooleanField(verbose_name="Наружная реклама в городе", default=False)


class Visitor(User):

    class Meta:
        verbose_name = "Пользователь ПОСЕТИТЕЛЬ"
        verbose_name_plural = "Пользователи ПОСЕТИТЕЛЬ"

    def __str__(self):
        return self.full_name.__str__()

    full_name = models.CharField(verbose_name="Ф.И.О", max_length=300)
    phone = models.BigIntegerField(verbose_name="Телефон", **parametersForNull)


class GosUser(User):

    class Meta:
        verbose_name = "Пользователь ГОС-ОРГАНЫ"
        verbose_name_plural = "Пользователи ГОС-ОРГАНЫ"

    def __str__(self):
        return self.full_name.__str__()

    full_name = models.CharField(verbose_name="Ф.И.О", max_length=300)
    phone = models.BigIntegerField(verbose_name="Телефон", **parametersForNull)
    oganization = models.CharField(verbose_name="Организация", max_length=300, choices=Organization, default=None, **parametersForNull)
    branch = models.CharField(verbose_name="Отделение", max_length=300, **parametersForNull)
    position = models.CharField(verbose_name="Должность", max_length=300, **parametersForNull)

    ########  Как вы узнали о мероприятие?   #########
    whatsapp_bool = models.BooleanField(verbose_name="WhatsApp", default=False)
    telegram_bool = models.BooleanField(verbose_name="Telegram", default=False)
    radio_bool = models.BooleanField(verbose_name="Радио реклама", default=False)
    tv_bool = models.BooleanField(verbose_name="ТВ", default=False)
    instagram_bool = models.BooleanField(verbose_name="Инстаграм", default=False)
    invite_mail = models.BooleanField(verbose_name="Приглашение от организаторов по почте", default=False)
    invite_fair = models.BooleanField(verbose_name="Приглашение от экспонента выставки", default=False)
    invite_minister = models.BooleanField(verbose_name="Приглашение от Министерства / ведомства", default=False)
    message = models.BooleanField(verbose_name="Сообщение по тел/факсу от организаторов", default=False)
    ad_city = models.BooleanField(verbose_name="Наружная реклама в городе", default=False)

    ##########################      Что вас заинтересовала в нашей выставке?:    GOS     ###############################
    gos_bool_one = models.BooleanField(verbose_name="Присутствие инвесторов", default=False)
    gos_bool_two = models.BooleanField(verbose_name="Потенциал выставки", default=False)
    gos_bool_three = models.BooleanField(verbose_name="Развитие экономики Кыргызстана", default=False)
    gos_bool_four = models.BooleanField(verbose_name="Инвестиционные проекты", default=False)