from rest_framework import generics

from apps.chat.models import Message
from apps.chat.serialzers import MessageSerializer

class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
