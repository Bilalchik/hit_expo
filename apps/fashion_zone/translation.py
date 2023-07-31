from modeltranslation.translator import register, TranslationOptions
from apps.fashion_zone.models import (Opportunity, FashionZone, BracketsZone, Possibility, Brackets,
                                      AdditionalInformation, AdvantagesZone, Advantages, Stage)


@register(Opportunity)
class OpportunityTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(FashionZone)
class FashionZoneTranslationOptions(TranslationOptions):
    fields = ('block_title', 'header_photo', 'description')


@register(BracketsZone)
class BracketsZoneTranslationOptions(TranslationOptions):
    fields = ('title', 'subtext')


@register(Possibility)
class PossibilityTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Brackets)
class BracketsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(AdditionalInformation)
class AdditionalInformationTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(AdvantagesZone)
class AdvantagesZoneTranslationOptions(TranslationOptions):
    fields = ('block_title', )


@register(Advantages)
class AdvantagesTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Stage)
class StageTranslationOptions(TranslationOptions):
    fields = ('title', 'description')



