from rest_framework.generics import ListAPIView

from apps.main_page.models import (PageOne, Place, PlaceOffice,
                                    Partners, Members, Forum, 
                                    Ellipse, Video, Organizers,
                                    Target, Tasks, Sectors,
                                    Sponsors, Speakers, Socials)

from apps.main_page.serializers import (PageOneSerializer, PlaceSerializer, PlaceOfficeSerializer,
                                        PartnersSerializer, MembersSerializer, ForumSerializer,
                                        EllipseSerializer, VideoSerializer, OrganizersSerializer,
                                        TargetSerializer, TasksSerializer, SectorsSerializer,
                                        SponsorsSerializer, SpeakersSerializer, SocialsSerializer)


class PageOneView(ListAPIView):
    queryset = PageOne.objects.all()
    serializer_class = PageOneSerializer


class PlaceView(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceOfficeView(ListAPIView):
    queryset = PlaceOffice.objects.all()
    serializer_class = PlaceOfficeSerializer


class PartnersView(ListAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer


class MembersView(ListAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer


class ForumView(ListAPIView):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer


class TargetView(ListAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer


class TasksView(ListAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer


class EllipseView(ListAPIView):
    queryset = Ellipse.objects.all()
    serializer_class = EllipseSerializer


class OrganizersView(ListAPIView):
    queryset = Organizers.objects.all()
    serializer_class = OrganizersSerializer


class VideoView(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class SectorsView(ListAPIView):
    queryset = Sectors.objects.all()
    serializer_class = SectorsSerializer


class SpeakersView(ListAPIView):
    queryset = Speakers.objects.all()
    serializer_class = SpeakersSerializer


class SponsorsView(ListAPIView):
    queryset = Sponsors.objects.all()
    serializer_class = SponsorsSerializer


class SocialsView(ListAPIView):
    queryset = Socials.objects.all()
    serializer_class = SocialsSerializer
