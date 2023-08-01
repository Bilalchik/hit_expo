from modeltranslation.translator import register, TranslationOptions
from apps.trade_zone.models import (Members, Opportunity, TradeZone, StandPhoto, Additionally, Decor, Stand, StandZone,
                                    AdditionalText, Conditions, PurchaseStage)


@register(Members)
class MembersTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Opportunity)
class OpportunityTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(TradeZone)
class TradeZoneTranslationOptions(TranslationOptions):
    fields = ('block_title', 'header_photo')


@register(Additionally)
class AdditionallyTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Decor)
class DecorTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Stand)
class StandTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(StandZone)
class StandZoneTranslationOptions(TranslationOptions):
    fields = ('block_title', 'block_description', 'photo', 'subtext')


@register(AdditionalText)
class AdditionalTextTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Conditions)
class ConditionsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(PurchaseStage)
class PurchaseStageTranslationOptions(TranslationOptions):
    fields = ('title', )

