from rest_framework import serializers

from apps.other.models import Expectation, Partner, SMI, B2B, News


class ExpectationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expectation
        fields = ('id', 'title', 'description')


class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = ('id', 'title', 'description', 'image')


class SMISerializer(serializers.ModelSerializer):

    class Meta:
        model = SMI
        fields = ('id', 'text')


class B2BSerializer(serializers.ModelSerializer):
    class Meta:
        model = B2B
        fields = ('id', 'title', 'description')


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'description', 'image', 'date')
