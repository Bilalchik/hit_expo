from rest_framework import serializers
from apps.ticket.models import Industry, Stand, Ticket
from apps.trade_zone.serializers import AdditionallyListSerializer, DecorListSerializer


class StandListSerializer(serializers.ModelSerializer):
    additionally = AdditionallyListSerializer(many=True)
    decor = DecorListSerializer(many=True)

    class Meta:
        model = Stand
        fields = '__all__'


class IndustryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'


class TicketCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Ticket
        fields = '__all__'

    def validate(self, data):
        existing_tickets = Ticket.objects.filter(
            zone=data['zone'],
            zone_numbering=data['zone_numbering'],
            row=data['row'],
            line=data['line'],
            place=data['place']
        )

        if self.instance:  # Если это обновление объекта, исключаем текущий объект из проверки
            existing_tickets = existing_tickets.exclude(pk=self.instance.pk)

        if existing_tickets.exists():
            raise serializers.ValidationError("Это место уже занято.")

        return data
