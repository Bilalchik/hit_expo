from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from apps.ticket.models import Industry, Stand, Ticket
from apps.ticket.serializers import (IndustryListSerializer, TicketCreateSerializer, StandListSerializer,
                                     TicketListSerializer)


class TicketCreateView(APIView):

    def get(self, request):

        industry = Industry.objects.all()
        stands = Stand.objects.all()
        tickets = Ticket.objects.all()

        industry_serializer = IndustryListSerializer(industry, many=True)
        stands_serializer = StandListSerializer(stands, many=True)
        tickets_serializer = TicketListSerializer(tickets, many=True)

        all_data = {
            'stands': stands_serializer.data,
            'industry': industry_serializer.data,
            'tickets': tickets_serializer.data,
        }

        return Response(all_data)

    @swagger_auto_schema(
        operation_description="Создание билета",
        request_body=openapi.Schema(
            type="object",
            properties={
                "user": openapi.Schema(type="integer", example=1),
                "zone": openapi.Schema(type="integer", example=1),
                "industry": openapi.Schema(type="integer", example=1),
                "activities": openapi.Schema(type="string", example="Some activity"),
                "stand": openapi.Schema(type="integer", example=1),
                "zone_numbering": openapi.Schema(type="integer", example=1),
                "row": openapi.Schema(type="integer", example=1),
                "line": openapi.Schema(type="integer", example=1),
                "place": openapi.Schema(type="integer", example=1),
                "place_status": openapi.Schema(type="integer", example=1),
                "photo": openapi.Schema(type="string", format="binary"),
            }
        ),
        responses={
            201: openapi.Response("Successful creation", TicketCreateSerializer),
            400: "Bad Request",
        },
    )
    def post(self, request, format=None):
        serializer = TicketCreateSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





