from rest_framework import serializers

from .models import Message, ChatRoom
from apps.users.models import User


class UserNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class ChatRoomListSerializer(serializers.ModelSerializer):
    sender = UserNameSerializer()
    receiver = UserNameSerializer()

    class Meta:
        model = ChatRoom
        fields = '__all__'


class MessageCreateSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Message
        fields = ('sender', 'content', 'file')


class MessageListSerializer(serializers.ModelSerializer):
    sender = UserNameSerializer()
    chat = ChatRoomListSerializer()

    class Meta:
        model = Message
        fields = ('id', 'sender', 'content', 'file', 'timestamp', 'chat')







