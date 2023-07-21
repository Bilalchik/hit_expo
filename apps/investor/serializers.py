from rest_framework import serializers

from apps.investor.models import Investor, Country


class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = ('fio', 'title', 'image')


class CountrySerialzier(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('title', 'image', 'description')
