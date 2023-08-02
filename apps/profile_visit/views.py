from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView

from apps.profile_visit.models import Visit
from apps.profile_visit.serializers import VistListSerializer, VisitCreateSerializer


class VisitListView(ListAPIView):
    serializer_class = VistListSerializer

    def get_queryset(self):
        return Visit.objects.filter(to_whom=self.request.user.id)


class VisitCreateView(CreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitCreateSerializer


