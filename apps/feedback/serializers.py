from rest_framework import serializers as s
from .models import Application, Feedback


class ApplicationSerializer(s.ModelSerializer):
    
    class Meta:
        model = Application
        fields = 'name_organic', 'surname', 'name', 'email', 'number', 'user_status', 'data', 'id'


class FeedbackSerializer(s.ModelSerializer):

    class Meta:
        model = Feedback    
        fields = 'name', 'mail', 'phone', 'description', 'id'
