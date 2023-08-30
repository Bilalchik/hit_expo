from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.ticket.models import Industry, Stand, Ticket
from apps.ticket.serializers import IndustryListSerializer, TicketCreateSerializer, StandListSerializer


class TicketCreateView(APIView):

    def get(self, request):

        industry = Industry.objects.all()
        stands = Stand.objects.all()

        industry_serializer = IndustryListSerializer(industry, many=True)
        stands_serializer = StandListSerializer(stands, many=True)

        all_data = {
            'stands': stands_serializer.data,
            'industry': industry_serializer.data
        }

        return Response(all_data)

    def post(self, request, format=None):
        serializer = TicketCreateSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





