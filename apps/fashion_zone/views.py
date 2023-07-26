from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import FashionZoneListSerializer, BracketsZoneListSerializer, BracketsListSerializer,\
    AdditionalInformationListSerializer, AdvantagesZoneListSerializer, AdvantagesListSerializer, StageListSerializer
from .models import Opportunity, FashionZone, BracketsZone, Possibility, Brackets, AdditionalInformation, \
    AdvantagesZone, Advantages, Stage


class FashionZoneListView(APIView):

    def get(self, request, format=None):
        fashion_zone = FashionZone.objects.all()
        brackets_zone = BracketsZone.objects.all()
        brackets = Brackets.objects.all()
        additional_information = AdditionalInformation.objects.all()
        advantages_zone = AdvantagesZone.objects.all()
        advantages = Advantages.objects.all()
        stages = Stage.objects.all()

        fashion_zone_serializer = FashionZoneListSerializer(fashion_zone, many=True)
        brackets_zone_serializer = BracketsZoneListSerializer(brackets_zone, many=True)
        brackets_serializer = BracketsListSerializer(brackets, many=True)
        additional_information_serializer = AdditionalInformationListSerializer(additional_information, many=True)
        advantages_zone_serializer = AdvantagesZoneListSerializer(advantages_zone, many=True)
        advantages_serializer = AdvantagesListSerializer(advantages, many=True)
        stages_serializer = StageListSerializer(stages, many=True)

        all_data = {
            'fashion_zone': fashion_zone_serializer.data,
            'brackets_zone': brackets_zone_serializer.data,
            'brackets': brackets_serializer.data,
            'additional_information': additional_information_serializer.data,
            'advantages_zone': advantages_zone_serializer.data,
            'advantages': advantages_serializer.data,
            'stages': stages_serializer.data,
        }

        return Response(all_data)
