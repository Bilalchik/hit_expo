from rest_framework import serializers

from apps.chat.models import Message


class MessageSerilaziers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'author', 'content', 'timestamp', 'file')
