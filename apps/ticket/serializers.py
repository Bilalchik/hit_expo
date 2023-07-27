from rest_framework import serializers

from apps.ticket.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'title', 'description', 'payment_rekvizit', 'icon', 'chek_photo')

    def create(self, validated_data):
        return super().create(validated_data)
