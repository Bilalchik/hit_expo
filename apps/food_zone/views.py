from rest_framework import generics

from apps.food_zone.models import Advantage, FoodZone, Terms, ParticipationSteps
from apps.food_zone.serializers import AdvantageListSerializer,FoodZoneListSerializer, TermsListSerializer, ParticipationStepsListSerializer


#######   Преимущества для участников
class AdvantageCreateListView(generics.ListCreateAPIView):
    queryset = Advantage.objects.all()
    serializer_class = AdvantageListSerializer
    
    
class AdvantageDeleteView(generics.DestroyAPIView):
    queryset = Advantage.objects.all()
    serializer_class = AdvantageListSerializer
########################################################################

class FoodZoneCreateListView(generics.ListCreateAPIView):
    queryset = FoodZone.objects.all()
    serializer_class = FoodZoneListSerializer
    
    
class FoodZoneDeleteView(generics.DestroyAPIView):
    queryset = FoodZone.objects.all()
    serializer_class = FoodZoneListSerializer
    
#######################################################################

class TermsCreateListView(generics.ListCreateAPIView):
    queryset = Terms.objects.all()
    serializer_class = TermsListSerializer
    
    
class TermsDeleteView(generics.DestroyAPIView):
    queryset = Terms.objects.all()
    serializer_class = TermsListSerializer


##########################################################################

class ParticipationStepsCreateListView(generics.ListCreateAPIView):
    queryset = ParticipationSteps.objects.all()
    serializer_class = ParticipationStepsListSerializer
    
    
class ParticipationStepsDeleteView(generics.DestroyAPIView):
    queryset = ParticipationSteps.objects.all()
    serializer_class = ParticipationStepsListSerializer




























# class FoodZoneListView(APIView):

#     def get(self, request, format=None):

#         participation_steps = ParticipationSteps.objects.all()
#         food_zone_serializer = FoodZoneListSerializer(food_zone, many=True)
#         advantaged_zone_serializer = AdvantageListSerializer.objects.all()
#         terms_zone_serializer = TermsListSerializer.objects.all()


#         all_data = {
#             'food_zone_serializer': food_zone_serializer.data,
#             'participation_steps': FoodZoneListSerializer.data,
#             'advantaged_zone_serializer': AdvantageListSerializer.data,
#             'terms_zone_serializer': TermsListSerializer.data,
#         }
        
#         return Response(all_data)
