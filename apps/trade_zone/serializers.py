from rest_framework import serializers
from .models import Members, Opportunity, TradeZone, StandPhoto, Additionally, Decor, Stand, StandZone, AdditionalText, \
    Conditions, PurchaseStage


class MembersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'


class OpportunityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = '__all__'


class TradeZoneListSerializer(serializers.ModelSerializer):
    members = MembersListSerializer(many=True)
    opportunity = OpportunityListSerializer(many=True)

    class Meta:
        model = TradeZone
        fields = '__all__'


class StandPhotoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StandPhoto
        fields = '__all__'


class AdditionallyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Additionally
        fields = '__all__'


class DecorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decor
        fields = '__all__'


class StandListSerializer(serializers.ModelSerializer):
    additionally = AdditionallyListSerializer(many=True)
    decor = DecorListSerializer(many=True)

    class Meta:
        model = Stand
        fields = '__all__'


class StandZoneListSerializer(serializers.ModelSerializer):
    photo = StandPhotoListSerializer(many=True)

    class Meta:
        model = StandZone
        fields = '__all__'


class AdditionalTextListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalText
        fields = '__all__'


class ConditionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conditions
        fields = '__all__'


class PurchaseStageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseStage
        fields = '__all__'





