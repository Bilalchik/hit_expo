from rest_framework import serializers as s

from apps.main_page.models import (PageOne, Place, PlaceOffice,
                                    Partners, Members, Forum, 
                                    Ellipse, Video, Organizers,
                                    Target, Tasks, Sectors,
                                    Sponsors, Speakers, Socials)


class PageOneSerializer(s.ModelSerializer):
    
    class Meta:
        model = PageOne
        fields = ('id', 'image', 'year', 'title', 'description')


class PlaceSerializer(s.ModelSerializer):
    
    class Meta:
        model = Place
        fields = ('id', 'address', 'location')


class PlaceOfficeSerializer(s.ModelSerializer):
    
    class Meta:
        model = PlaceOffice
        fields = ('id', 'phone', 'mail', 'address', 'location')


class PartnersSerializer(s.ModelSerializer):
    
    class Meta:
        model = Partners
        fields = ('id', 'name', 'loga')


class MembersSerializer(s.ModelSerializer):

    class Meta:
        model = Members
        fields = ('id', 'name', 'image')


class ForumSerializer(s.ModelSerializer):
    
    class Meta:
        model = Forum
        fields = ('id', 'title', 'description')


class EllipseSerializer(s.ModelSerializer):
    
    class Meta:
        model = Ellipse
        fields = ('id', 'company', 'countries', 'meetings', 'exhibitors')


class VideoSerializer(s.ModelSerializer):

    class Meta:
        model = Video
        fields = ('id', 'title', 'urel_video')


class OrganizersSerializer(s.ModelSerializer):
    
    class Meta:
        model = Organizers
        fields = ('id', 'name', 'loga')


class TargetSerializer(s.ModelSerializer):

    class Meta:
        model = Target
        fields = ('id', 'title', 'description') 


class TasksSerializer(s.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'number', 'description')


class SectorsSerializer(s.ModelSerializer):
    
    class Meta:
        model = Sectors
        fields = ('id', 'image', 'icon', 'title', 'description')


class SponsorsSerializer(s.ModelSerializer):

    class Meta:
        model = Sponsors
        fields = ('id', 'name', 'loga')


class SpeakersSerializer(s.ModelSerializer):
    
    class Meta:
        model =Speakers
        fields = ('id', 'image', 'name', 'description')


class SocialsSerializer(s.ModelSerializer):
    
    class Meta:
        model = Socials
        fields = ('id', 'whatsapp', 'instagram', 'facebook', 'telegram', 
                    'snapchat', 'tiktok', 'twitter', 'youtube', 'wechat')
