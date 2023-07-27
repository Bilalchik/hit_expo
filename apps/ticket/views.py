from rest_framework import generics

from apps.ticket.models import Ticket
from apps.ticket.serializers import TicketSerializer
from apps.ticket.permissions import TicketPermission


class TicketView(generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (TicketPermission,)
