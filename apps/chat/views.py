from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .models import Message, ChatRoom
from .serializers import ChatRoomListSerializer, MessageCreateSerializer, MessageListSerializer


User = get_user_model()


class MessagePagination(PageNumberPagination):
    page_size = 20  # Количество сообщений на одной странице
    page_size_query_param = 'page_size'
    max_page_size = 100


class ChatRoomListView(ListAPIView):
    serializer_class = ChatRoomListSerializer

    def get_queryset(self):
        return ChatRoom.objects.filter(Q(receiver__id=self.request.user.id) | Q(sender__id=self.request.user.id))


class IncomingListView(APIView):

    def get(self, request):
        queryset = ChatRoom.objects.filter(receiver__id=self.request.user.id)

        serializer = ChatRoomListSerializer(queryset, many=True)
        return Response(serializer.data)


class SentListView(ListAPIView):

    serializer_class = ChatRoomListSerializer

    def get_queryset(self):
        return ChatRoom.objects.filter(sender__id=self.request.user.id)


class ChatRoomDetailView(APIView):
    pagination_class = MessagePagination

    def get_chatroom(self, sender, receiver):
        try:
            # Пытаемся найти существующую чат комнату между отправителем и получателем
            chatroom = ChatRoom.objects.get(sender=sender, receiver=receiver)
        except ChatRoom.DoesNotExist:
            try:
                # Пытаемся найти обратную чат комнату (получатель -> отправитель)
                chatroom = ChatRoom.objects.get(sender=receiver, receiver=sender)
            except ChatRoom.DoesNotExist:
                # Если чат комнаты нет, создаем новую
                chatroom = ChatRoom.objects.create(sender=sender, receiver=receiver)
        return chatroom

    # def get(self, request, pk):
    #     queryset = Message.objects.filter(chat__id=pk)
    #     serializer = MessageListSerializer(queryset, many=True)
    #     return Response(serializer.data)

    def get(self, request, pk):
        chatroom = get_object_or_404(ChatRoom, pk=pk)
        messages = chatroom.messages.all().order_by('-timestamp')

        # Применяем пагинацию к результату запроса
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(messages, request)

        serializer = MessageListSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, pk):
        receiver = get_object_or_404(User, pk=pk)
        serializer = MessageCreateSerializer(data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            sender = serializer.validated_data['sender']
            chatroom, created = ChatRoom.objects.get_or_create(sender=sender, receiver=receiver)

            # Обновляем last_messages в чат комнате
            chatroom.last_messages = serializer.validated_data['content']
            chatroom.save()

            serializer.save(chat=chatroom)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


