from rest_framework import serializers

from apps.investor.models import Investor, Country, Text


class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = ('id', 'fio', 'title', 'image')


class CountrySerialzier(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'title', 'image')


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ('id', 'description')
