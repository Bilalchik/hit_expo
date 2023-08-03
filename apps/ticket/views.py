from rest_framework import generics

from apps.ticket.models import Ticket, Check
from apps.ticket.serializers import TicketSerializer, CheckSerializer
from apps.ticket.permissions import TicketPermission


class TicketView(generics.ListAPIView, generics.RetrieveAPIView, generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (TicketPermission,)


class CheckView(generics.ListAPIView, generics.RetrieveAPIView, generics.CreateAPIView):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer
    permission_classes = (TicketPermission,)
