from rest_framework import serializers
from .models import Advantage, InvestZone, StandZone, Terms, Stand, GeneralAdvantages, Conditions, ParticipationSteps


class AdvantageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advantage
        fields = '__all__'


class InvestZoneListSerializer(serializers.ModelSerializer):
    advantage = AdvantageListSerializer(many=True)

    class Meta:
        model = InvestZone
        fields = '__all__'


class TermsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terms
        fields = '__all__'


class StandZoneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StandZone
        fields = '__all__'


class StandListSerializer(serializers.ModelSerializer):
    terms = TermsListSerializer(many=True)

    class Meta:
        model = Stand
        fields = '__all__'


class GeneralAdvantagesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralAdvantages
        fields = '__all__'


class ConditionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conditions
        fields = '__all__'


class ParticipationStepsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParticipationSteps
        fields = '__all__'

