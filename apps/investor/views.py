from rest_framework.generics import  ListCreateAPIView

from apps.investor.models import Investor, Country, Text , Organizer , Sponsors
from apps.investor.serializers import InvestorSerializer, CountrySerializer, TextSerializer, OrganizerSerializer, SponsorsSerializer


class InvestorView(ListCreateAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer


class CountryView(ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class TextView(ListCreateAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    
    
class OrganizerView(ListCreateAPIView):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer
    
    
class SponsorsView(ListCreateAPIView):
    queryset = Sponsors.objects.all()
    serializer_class = SponsorsSerializer
