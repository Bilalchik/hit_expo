from rest_framework import generics

from apps.chat.models import Message
from apps.chat.serializers import MessageSerilaziers
from apps.chat.permissions import MessagePermission


class MessageView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerilaziers
    permission_classes = (MessagePermission,)
