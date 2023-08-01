from modeltranslation.translator import register, TranslationOptions
from apps.invest_zone.models import (Advantage, InvestZone, StandZone, Terms, Stand, GeneralAdvantages, Conditions,
                                     ParticipationSteps)


@register(Advantage)
class AdvantageTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(InvestZone)
class InvestZoneTranslationOptions(TranslationOptions):
    fields = ('block_title', 'header_photo')


@register(StandZone)
class StandZoneTranslationOptions(TranslationOptions):
    fields = ('subtext', )


@register(Terms)
class TermsTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Stand)
class StandTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(GeneralAdvantages)
class GeneralAdvantagesTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Conditions)
class ConditionsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'signing')


@register(ParticipationSteps)
class ParticipationStepsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


