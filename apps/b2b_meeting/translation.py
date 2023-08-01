from modeltranslation.translator import register, TranslationOptions
from apps.b2b_meeting.models import Meeting


@register(Meeting)
class MeetingTranslationOptions(TranslationOptions):
    fields = ('answer', 'description')






