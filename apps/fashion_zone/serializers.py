from rest_framework import serializers
from .models import Opportunity, FashionZone, BracketsZone, Possibility, Brackets, AdditionalInformation, \
    AdvantagesZone, Advantages, Stage


class OpportunityListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Opportunity
        fields = '__all__'


class FashionZoneListSerializer(serializers.ModelSerializer):
    opportunity = OpportunityListSerializer(many=True)

    class Meta:
        model = FashionZone
        fields = '__all__'


class BracketsZoneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BracketsZone
        fields = '__all__'


class PossibilityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Possibility
        fields = '__all__'


class BracketsListSerializer(serializers.ModelSerializer):
    possibility = PossibilityListSerializer(many=True)

    class Meta:
        model = Brackets
        fields = '__all__'


class AdditionalInformationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInformation
        fields = '__all__'


class AdvantagesZoneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvantagesZone
        fields = '__all__'


class AdvantagesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = '__all__'


class StageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = '__all__'

