from rest_framework import serializers
from apps.profile_visit.models import Visit
from apps.users.models import User


class UserNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class VistListSerializer(serializers.ModelSerializer):
    who = UserNameSerializer()
    to_whom = UserNameSerializer()

    class Meta:
        model = Visit
        fields = '__all__'


class VisitCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit
        fields = ('who', 'to_whom')

    def create(self, validated_data):
        who_id = validated_data['who']
        to_whom_id = validated_data['to_whom']

        existing_visit = Visit.objects.filter(who=who_id, to_whom=to_whom_id).exists()

        if existing_visit:
            return None

        visit = Visit.objects.create(who=who_id, to_whom=to_whom_id)
        return visit
