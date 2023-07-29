from rest_framework import serializers
from apps.b2b_meeting.models import Meeting
from apps.users.models import User


class UserNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class MeetingListSerializer(serializers.ModelSerializer):
    inviter = UserNameSerializer()
    invited = UserNameSerializer()

    class Meta:
        model = Meeting
        fields = ('id', 'inviter', 'invited', 'start', 'end', 'get_status_display', 'answer', 'description')


class MeetingCreateSerializer(serializers.ModelSerializer):
    inviter = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Meeting
        fields = ('inviter', 'invited', 'start', 'end', 'description')
        extra_kwargs = {
            'description': {'required': False},
            'invited': {'required': False},
        }

    def validate(self, data):
        current_user = self.context['request'].user
        invited = data['invited']
        start = data['start']
        end = data['end']

        # Проверяем, существует ли уже встреча с таким же временем
        existing_meeting = Meeting.objects.filter(invited=invited, start=start, end=end, status=4).exists()
        meeting_existing = Meeting.objects.filter(inviter=current_user, start=start, end=end, status=4).exists()
        if existing_meeting:
            raise serializers.ValidationError("Уданного пользователя уже назначена встреча на это время.")
        elif meeting_existing:
            raise serializers.ValidationError("У вас уже есть встреча на это время.")

        return data


class MeetingAnswerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting
        fields = ('id', 'answer')


