from modeltranslation.translator import register, TranslationOptions
from apps.categories.models import Category


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )






