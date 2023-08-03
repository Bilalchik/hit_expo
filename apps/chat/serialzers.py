from rest_framework import serializers

from apps.chat.models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = 'id', 'author', 'content', 'timestamp', 'file'

    def create(self, validated_data):
        return super().create(validated_data)
