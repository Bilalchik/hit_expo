from rest_framework import generics

from apps.chat.models import Message
from apps.chat.serialzers import MessageSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type="object",
            properties={
                "author": openapi.Schema(type="integer", example=1),
                "content": openapi.Schema(type="string", example="Я люблю тебя!"),
                "file": openapi.Schema(type="file", example="'Типо файл'"),
            }
        )
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
