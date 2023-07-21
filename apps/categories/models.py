from django.db import models

from apps.categories.services import get_upload_path, validate_file_extension


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.PROTECT,
                               related_name='children', blank=True, null=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
    icon = models.FileField(upload_to=get_upload_path, validators=[validate_file_extension], null=True, blank=True)
    is_main = models.BooleanField(default=False)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return f'{self.name_en}'