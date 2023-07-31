from modeltranslation.translator import register, TranslationOptions
from apps.main_page.models import (PageOne, Place, PlaceOffice,
                                    Partners, Members, Forum,
                                    Ellipse, Video, Organizers,
                                    Target, Tasks, Sectors,
                                    Sponsors, Speakers, Socials)


@register(PageOne)
class PageOneTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Forum)
class ForumTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Target)
class TargetTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Tasks)
class TasksTranslationOptions(TranslationOptions):
    fields = ('description', )


@register(Sectors)
class SectorsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'image')


