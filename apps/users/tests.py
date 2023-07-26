# from django.test import TestCase
#
# # Create your tests here.
#
# class User(AbstractUser):
#     class Meta:
#         verbose_name = "Пользователь"
#         verbose_name_plural = "Пользовати"
#
#     def __str__(self):
#         return self.email.__str__()
#
#     username = None
#     date_joined = None
#     first_name = None
#     last_name = None
#     last_login = None
#     is_active = models.BooleanField(default=True, verbose_name="Активный?")
#     is_staff = models.BooleanField(default=False, verbose_name="Админ?")
#     is_superuser = models.BooleanField(default=False, verbose_name="СуперАдмин?")
#
#     #############################################       Участник           ##########################################
#
#     participation_sector = models.CharField(max_length=300,
#                                             verbose_name="Выберите сектор участия (с условиями участия каждого сектора можно ознакомится)",
#                                             **parametersForNull)
#
#     brand = models.CharField(max_length=300, verbose_name="Наименование бренда", **parametersForNull)
#     organization_participant = models.CharField(max_length=300,
#                                                 verbose_name="Полное юридическое наименование организации",
#                                                 **parametersForNull)
#     name_bank = models.CharField(max_length=300, verbose_name="Наименование банка", **parametersForNull)
#
#     inn = models.CharField(max_length=300, verbose_name="ИИН/ИНН(Серия патента компании)", **parametersForNull)
#     orgn = models.CharField(max_length=300, verbose_name="ОГРН(Номер патента)", **parametersForNull)
#     p_c = models.CharField(max_length=300, verbose_name="Р/С", **parametersForNull)
#     bik = models.CharField(max_length=300, verbose_name="БИК", **parametersForNull)
#     okpo = models.CharField(max_length=300, verbose_name="ОКПО", **parametersForNull)
#
#     pdf_file = models.FileField(verbose_name="Загрузите свидетельство регистрации в pdf", upload_to='file/register',
#                                 **parametersForNull)
#     name_manager = models.CharField(max_length=300, verbose_name="Ф.И.О руководителя", **parametersForNull)
#     position_participant = models.CharField(max_length=300, verbose_name="Должность (Участник)", **parametersForNull)
#     description = models.TextField(verbose_name="Описание", **parametersForNull)
#
#     email_participant = models.EmailField(max_length=300, verbose_name="Email Participant", default=None, unique=True,
#                                           **parametersForNull)
#
#     ###############################################         Контактные лица          #########################################
#
#     name_contact_person = models.CharField(max_length=300, verbose_name="Ф.И.О (контактным лицом)", **parametersForNull)
#     position_contact_person = models.CharField(max_length=300, verbose_name="Должность (контактным лицом)",
#                                                **parametersForNull)
#     phone_contact_person = models.CharField(max_length=300, verbose_name="Телефон (контактным лицом)",
#                                             **parametersForNull)
#     whatsapp_contact_person = models.CharField(max_length=300, verbose_name="WhatsApp (контактным лицом)",
#                                                **parametersForNull)
#
#     # socials
#     instagram = models.CharField(verbose_name="Укажите url Instagram", max_length=300, **parametersForNull)
#     facebook = models.CharField(verbose_name="Укажите url Facebook", max_length=300, **parametersForNull)
#     twitter = models.CharField(verbose_name="Укажите url Twitter", max_length=300, **parametersForNull)
#
#     #####################################   Investment    #################################
#
#     agricultural_production = models.BooleanField(verbose_name="Производство + сельхоз", default=False)
#     construction = models.BooleanField(verbose_name="Строительство", default=False)
#     technique = models.BooleanField(verbose_name="Строительство + техника", default=False)
#     textiles = models.BooleanField(verbose_name="Текстиль, обувь и аксессуары", default=False)
#     education = models.BooleanField(verbose_name="Образование", default=False)
#     medicine = models.BooleanField(verbose_name="Медицина", default=False)
#     tourism = models.BooleanField(verbose_name="Туризм", default=False)
#     echo = models.BooleanField(verbose_name="Эко", default=False)
#     it = models.BooleanField(verbose_name="IT", default=False)
#     banks = models.BooleanField(verbose_name="Банки", default=False)
#     kfx = models.BooleanField(verbose_name="КФХ", default=False)
#     krc = models.BooleanField(verbose_name="КРС", default=False)
#     machinery = models.BooleanField(verbose_name="Машиностроение", default=False)
#     industry = models.BooleanField(verbose_name="Текстильное промышленность", default=False)
#
#     #####################################################################
#
#     choose_direction_fashion = models.CharField(max_length=300, verbose_name="Выберите направление (Fashion)",
#                                                 **parametersForNull)
#     choose_direction_food = models.CharField(max_length=300, verbose_name="Выберите направление (Food)",
#                                              **parametersForNull)
#     choose_direction_expert = models.CharField(max_length=300, verbose_name="Эксперт", **parametersForNull)
#
#     status = models.CharField(max_length=300, verbose_name="Статус", **parametersForNull)
#     manager = models.CharField(max_length=300, verbose_name="Менеджер", **parametersForNull)
#     referal = models.CharField(max_length=300, verbose_name="Реферал", **parametersForNull)
#
#     ####################################.       PASSWORD    #################################
#     uniqueId = models.UUIDField(unique=True, verbose_name="Уникальный id", **parametersForNull)
#     email = models.EmailField(max_length=200, verbose_name="Email", unique=True)
#
#     resetPasswordUUID = models.UUIDField(verbose_name="Ссылка для восстановления пароля", **parametersForNull)
#     resetPasswordDate = models.BigIntegerField(verbose_name="Время восстановления пароля", **parametersForNull)
#
#     USERNAME_FIELD = 'email'
#
#     REQUIRED_FIELDS = []
#
#     objects = CustomManager()
#
#     def save(self, force_insert=False, force_update=False, using=None,
#              update_fields=None):
#         if not self.id:
#             self.uniqueId = uuid.uuid4()
#         super(User, self).save(force_insert=False, force_update=False, using=None, update_fields=None)