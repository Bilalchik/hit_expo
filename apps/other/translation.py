from modeltranslation.translator import register, TranslationOptions
from apps.other.models import Expectation, Partner, SMI, B2B, News


@register(Expectation)
class ExpectationTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Partner)
class PartnerTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(SMI)
class SMITranslationOptions(TranslationOptions):
    fields = ('text', )


@register(B2B)
class B2BTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('description', )
