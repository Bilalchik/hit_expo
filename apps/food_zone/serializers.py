from rest_framework import serializers
from .models import Advantage, FoodZone, Terms, ParticipationSteps


class AdvantageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advantage
        fields = '__all__'


class FoodZoneListSerializer(serializers.ModelSerializer):
    advantage = AdvantageListSerializer(many=True)

    class Meta:
        model = FoodZone
        fields = '__all__'


class TermsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terms
        fields = '__all__'


class ParticipationStepsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParticipationSteps
        fields = '__all__'

