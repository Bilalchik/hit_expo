from rest_framework import serializers

from apps.investor.models import Investor, Country, Text , Organizer , Sponsors


class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = ('id', 'fio', 'title', 'image')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'title', 'image')


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ('id', 'description')


class OrganizerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Organizer
        fields = ('id', 'title', 'icon', 'link', 'url', 'text', 'galary')


class SponsorsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sponsors
        fields = ('id', 'text_one day', 'icon_one','description')
        