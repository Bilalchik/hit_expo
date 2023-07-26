from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TradeZoneListSerializer, StandListSerializer, StandZoneListSerializer, \
    AdditionalTextListSerializer, ConditionsListSerializer, PurchaseStageListSerializer
from .models import Members, Opportunity, TradeZone, StandPhoto, Additionally, Decor, Stand, StandZone, AdditionalText, \
    Conditions, PurchaseStage


class TradeZoneListView(APIView):

    def get(self, request, format=None):
        trade_zones = TradeZone.objects.all()
        stands = Stand.objects.all()
        stand_zones = StandZone.objects.all()
        additionally_texts = Additionally.objects.all()
        conditions = Conditions.objects.all()
        purchase_stages = PurchaseStage.objects.all()

        trade_zones_serializer = TradeZoneListSerializer(trade_zones, many=True)
        stands_serializer = StandListSerializer(stands, many=True)
        stand_zones_serializer = StandZoneListSerializer(stand_zones, many=True)
        additionally_texts_serializer = AdditionalTextListSerializer(additionally_texts, many=True)
        conditions_serializer = ConditionsListSerializer(conditions, many=True)
        purchase_stages_serializer = PurchaseStageListSerializer(purchase_stages, many=True)

        all_data = {
            'trade_zones': trade_zones_serializer.data,
            'stands': stands_serializer.data,
            'stand_zones': stand_zones_serializer.data,
            'additional_texts': additionally_texts_serializer.data,
            'conditions': conditions_serializer.data,
            'purchase_stages': purchase_stages_serializer.data,
        }

        return Response(all_data)



