from rest_framework.generics import ListAPIView

from apps.investor.models import Investor, Country, Text
from apps.investor.serializers import InvestorSerializer, CountrySerialzier, TextSerializer


class InvestorView(ListAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer


class CountryView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerialzier


class TextView(ListAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
