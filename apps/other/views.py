from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.other.models import Expectation, Partner, SMI, B2B, News
from apps.other.serializers import ExpectationSerializer, PartnerSerializer, SMISerializer, B2BSerializer, NewsSerializer


class ExpectationView(ListAPIView):
    queryset = Expectation.objects.all()
    serializer_class = ExpectationSerializer


class PartnerView(ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class SMIView(ListAPIView):
    queryset = SMI.objects.all()
    serializer_class = SMISerializer


class B2BView(ListAPIView):
    queryset = B2B.objects.all()
    serializer_class = B2BSerializer


class NewsView(ListAPIView, RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
