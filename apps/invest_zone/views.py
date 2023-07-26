from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import InvestZoneListSerializer, StandZoneListSerializer, StandListSerializer,\
    GeneralAdvantagesListSerializer, ConditionsListSerializer, ParticipationStepsListSerializer
from .models import Advantage, InvestZone, StandZone, Terms, Stand, GeneralAdvantages, Conditions, ParticipationSteps


class InvestZoneListView(APIView):

    def get(self, request, format=None):
        invest_zone = InvestZone.objects.all()
        stand_zone = StandZone.objects.all()
        stand = Stand.objects.all()
        general_advantages = GeneralAdvantages.objects.all()
        conditions = Conditions.objects.all()
        participation_steps = ParticipationSteps.objects.all()

        invest_zone_serializer = InvestZoneListSerializer(invest_zone, many=True)
        stand_zone_serializer = StandZoneListSerializer(stand_zone, many=True)
        stand_serializer = StandListSerializer(stand, many=True)
        general_advantages_serializer = GeneralAdvantagesListSerializer(general_advantages, many=True)
        conditions_serializer = ConditionsListSerializer(conditions, many=True)
        participation_steps_serializer = ParticipationStepsListSerializer(participation_steps, many=True)

        all_data = {
            'invest_zones': invest_zone_serializer.data,
            'stand_zones': stand_zone_serializer.data,
            'stands': stand_serializer.data,
            'general_advantages': general_advantages_serializer.data,
            'conditions': conditions_serializer.data,
            'participation_steps': participation_steps_serializer.data,
        }

        return Response(all_data)
