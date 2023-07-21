from rest_framework import serializers as s

from apps.main_page.models import (PageOne, Place, PlaceOffice,
                                    Partners, Members, Forum, 
                                    Ellipse, Video, Organizers,
                                    Target, Tasks, Sectors,
                                    Sponsors, Speakers, Socials)


class PageOneSerializer(s.ModelSerializer):
    
    class Meta:
        model = PageOne
        fields = ('image', 'year', 'title', 'description')


class PlaceSerializer(s.ModelSerializer):
    
    class Meta:
        model = Place
        fields = ('address', 'location')


class PlaceOfficeSerializer(s.ModelSerializer):
    
    class Meta:
        model = PlaceOffice
        fields = ('phone', 'mail', 'address', 'location')


class PartnersSerializer(s.ModelSerializer):
    
    class Meta:
        model = Partners
        fields = ('name', 'loga')


class MembersSerializer(s.ModelSerializer):

    class Meta:
        model = Members
        fields = ('name', 'image')


class ForumSerializer(s.ModelSerializer):
    
    class Meta:
        model = Forum
        fields = ('title', 'description')


class EllipseSerializer(s.ModelSerializer):
    
    class Meta:
        model = Ellipse
        fields = ('company', 'countries', 'meetings', 'exhibitors')


class VideoSerializer(s.ModelSerializer):

    class Meta:
        model = Video
        fields = ('title', 'urel_video')


class OrganizersSerializer(s.ModelSerializer):
    
    class Meta:
        model = Organizers
        fields = ('name', 'loga')


class TargetSerializer(s.ModelSerializer):

    class Meta:
        model = Target
        fields = ('title', 'description') 


class TasksSerializer(s.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('number', 'description')


class SectorsSerializer(s.ModelSerializer):
    
    class Meta:
        model = Sectors
        fields = ('image', 'icon', 'title', 'description')


class SponsorsSerializer(s.ModelSerializer):

    class Meta:
        model = Sponsors
        fields = ('name', 'loga')


class SpeakersSerializer(s.ModelSerializer):
    
    class Meta:
        model =Speakers
        fields = ('image', 'name', 'description')


class SocialsSerializer(s.ModelSerializer):
    
    class Meta:
        model = Socials
        fields = ('whatsapp', 'instagram', 'facebook', 'telegram', 
                    'snapchat', 'tiktok', 'twitter', 'youtube', 'wechat')
