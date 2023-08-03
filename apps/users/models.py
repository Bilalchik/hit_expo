import uuid, os

from django.db import models
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.models import AbstractUser

from apps.users.managers import CustomManager
from apps.users.choices import Organization, Industry


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
    PARTICIPANT = 5, "УЧАСТНИК"


class User(AbstractUser):
    class Meta:
        verbose_name = "Все пользователи"
        verbose_name_plural = "Пользователь"

    def __str__(self):
        return self.email.__str__()

    username = None
    first_name = None
    last_name = None
    last_login = None

    ####################################.       PASSWORD    #################################
    user_type = models.PositiveSmallIntegerField(choices=UserType.choices, default=UserType.VISITOR, verbose_name="Тип пользователя")
    uniqueId = models.UUIDField(unique=True, verbose_name="Уникальный id", **parametersForNull)
    email = models.EmailField(max_length=200, verbose_name="Email", unique=True)

    user_bool = models.BooleanField(verbose_name="Разрешение на редактирование", default=False)

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


class Participant(User):

    class Meta:
        verbose_name = "Пользователь УЧАСТНИК"
        verbose_name_plural = "Пользователи УЧАСТНИКОВ"

    def __str__(self):
        return self.company_one.__str__()

    company_one = models.CharField(verbose_name="Название компании", max_length=300, **parametersForNull)
    company_two = models.CharField(verbose_name="Юридическое название компании", max_length=300, **parametersForNull)
    personnel = models.CharField(verbose_name="Количество сотрудников", max_length=300, **parametersForNull)
    industry = models.CharField(verbose_name="Отрасль (Выберите одну из представленных “Строительство и недвижимость”)", max_length=300, choices=Industry, default=None, **parametersForNull)
    industry_name = models.CharField(verbose_name="Другое(Введите свою отрасль если не нашли среди предложенных)", max_length=300, **parametersForNull)
    direction = models.CharField(verbose_name="Направление (Напишите свой вид деятельности “Производство кирпичей”)", max_length=300, **parametersForNull)
    description = models.TextField(verbose_name="Опишите свою деятельность (товар или услугу)", **parametersForNull)

    country = models.CharField(verbose_name="Страна", max_length=128, **parametersForNull)
    city = models.CharField(verbose_name="Город", max_length=128, **parametersForNull)
    address_one = models.CharField(verbose_name="Юридический адрес", max_length=128, **parametersForNull)
    address_two = models.CharField(verbose_name="Фактический адрес", max_length=128, **parametersForNull)

    email_company = models.EmailField(verbose_name="Адрес электронной почты компании", max_length=128, **parametersForNull)
    site_company = models.CharField(verbose_name="Сайт", max_length=300, **parametersForNull)
    instagram = models.CharField(verbose_name="Instagram", max_length=300, **parametersForNull)
    facebook = models.CharField(verbose_name="Facebook", max_length=300, **parametersForNull)

    iin_inn = models.CharField(verbose_name="ИИН/ИНН(Серия патента компании)", max_length=128, **parametersForNull)
    ogrn = models.CharField(verbose_name="ОГРН(Номер патента)", max_length=128, **parametersForNull)
    okpo = models.CharField(verbose_name="ОКПО", max_length=128, **parametersForNull)
    charter_company = models.FileField(verbose_name="Загрузите устав компании в  pdf или jpg", upload_to='company/% Y/% m/% d/', **parametersForNull)

    bank = models.CharField(verbose_name="Наименование банка", max_length=128, **parametersForNull)
    p_c = models.CharField(verbose_name="P/C", max_length=128, **parametersForNull)
    bik = models.CharField(verbose_name="БИК", max_length=128, **parametersForNull)
    image_logo = models.ImageField(verbose_name="Загрузите логотип компании в png или jpg", upload_to='images/logo-participant', **parametersForNull)

    name_manager = models.CharField(verbose_name="Ф.И.О (Данные о руководителе)", max_length=128, **parametersForNull)
    date_of_birth = models.CharField(verbose_name="Дата рождения", max_length=64, **parametersForNull)
    iin_inn_manage = models.CharField(verbose_name="ИНН/ИИН руководителя", max_length=128, **parametersForNull)
    position = models.CharField(verbose_name="Должность", max_length=64, **parametersForNull)
    effective = models.CharField(verbose_name="Действующий на основании", max_length=128, **parametersForNull)

    contact_person = models.BooleanField(verbose_name="Контактное лицо", default=False)
    name_cont_person = models.CharField(verbose_name="Ф.И.О (Контактное лицо)", max_length=128, **parametersForNull)
    number_cont_person = models.BigIntegerField(verbose_name="Номер телефона", **parametersForNull)

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

    bool_company_one = models.BooleanField(verbose_name="Присутствие инвесторов", default=False)
    bool_company_two = models.BooleanField(verbose_name="Присутствие государственных органов", default=False)
    bool_company_three = models.BooleanField(verbose_name="Выход на мировой рынок", default=False)
    bool_company_four = models.BooleanField(verbose_name="Реализация продукции", default=False)
    bool_company_five = models.BooleanField(verbose_name="Возможность получения инвестиции", default=False)
    bool_company_six = models.BooleanField(verbose_name="Расширение бизнеса", default=False)
    bool_company_seven = models.BooleanField(verbose_name="Коммуникация с другми участниками", default=False)
    bool_company_eight = models.BooleanField(verbose_name="Программа", default=False)
    bool_company_nine = models.BooleanField(verbose_name="Место и формат проведения", default=False)
    bool_company_ten = models.BooleanField(verbose_name="Возможность получения номинации", default=False)


class UserSMI(User):

    class Meta:
        verbose_name = "Пользователь СМИ"
        verbose_name_plural = "Пользователи СМИ"

    def __str__(self):
        return self.name_organization.__str__()

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
        verbose_name_plural = "Пользователи ЭКСПЕРТОВ"

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
        verbose_name_plural = "Пользователи ПОСЕТИТЕЛЕЙ"

    def __str__(self):
        return self.full_name.__str__()

    full_name = models.CharField(verbose_name="Ф.И.О", max_length=300)
    phone = models.BigIntegerField(verbose_name="Телефон", **parametersForNull)


class GosUser(User):

    class Meta:
        verbose_name = "Пользователь ГОС-ОРГАНЫ"
        verbose_name_plural = "Пользователи ГОС-ОРГАНОВ"

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
    
##############################     Global Search #############################    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    
def global_search(request):
    search_query = request.GET.get('q', '')  # Получаем запрос поиска из параметра 'q' в URL

    # Ищем пользователей, удовлетворяющих поисковому запросу (username или email)
    users = User.objects.filter(Q(username__icontains=search_query) | Q(email__icontains=search_query))

    context = {
        'users': users,
        'search_query': search_query,
    }
    return render(request, 'search_results.html', context)
