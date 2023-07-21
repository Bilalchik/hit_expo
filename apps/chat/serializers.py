from rest_framework import serializers
from .models import Message
from apps.users.models import User


class UserNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class MessageListSerializer(serializers.ModelSerializer):
    sender = UserNameSerializer()
    receiver = UserNameSerializer()

    class Meta:
        model = Message
        fields = '__all__'


class MessageCreateSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Message
        fields = ('sender', 'receiver', 'content', 'file')


