from rest_framework import serializers

from apps.ticket.models import Ticket, Check


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'title', 'description', 'payment_rekvizit', 'icon')

    def create(self, validated_data):
        return super().create(validated_data)



class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Check
        fields = ('id', 'chek_photo')

    def create(self, validated_data):
        return super().create(validated_data)
