from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.state import token_backend
from rest_framework.exceptions import PermissionDenied
from .models import Book

from apps.users.models import User, Participant, UserSMI, Expert, Visitor, GosUser, UserType


class UserCRUDSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=400, required=False)

    class Meta:
        model = User
        exclude = ['groups', 'user_permissions', 'resetPasswordUUID', 'resetPasswordDate']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            if field == 'password':
                instance.set_password(value)
            else:
                setattr(instance, field, value)
        instance.save()
        return instance


class UserSMISerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=400, required=False)

    class Meta:
        model = UserSMI
        exclude = ['groups', 'user_permissions', 'resetPasswordUUID', 'resetPasswordDate']

    def create(self, validated_data):
        user_smi = UserSMI(**validated_data)
        user_smi.set_password(validated_data['password'])
        user_smi.user_type = UserType.MASS_MEDIA
        user_smi.save()
        return user_smi

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            if field == 'password':
                instance.set_password(value)
            else:
                setattr(instance, field, value)
        instance.save()
        return instance


class ExpertSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=400, required=False)

    class Meta:
        model = Expert
        exclude = ['groups', 'user_permissions', 'resetPasswordUUID', 'resetPasswordDate']

    def create(self, validated_data):
        expert = Expert(**validated_data)
        expert.set_password(validated_data['password'])
        expert.save()
        return expert


class VisitorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=400, required=False)

    class Meta:
        model = Visitor
        exclude = ['groups', 'user_permissions', 'resetPasswordUUID', 'resetPasswordDate']

    def create(self, validated_data):
        visitor = Visitor(**validated_data)
        visitor.set_password(validated_data['password'])
        visitor.save()
        return visitor


class GosUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=400, required=False)

    class Meta:
        model = GosUser
        exclude = ['groups', 'user_permissions', 'resetPasswordUUID', 'resetPasswordDate']

    def create(self, validated_data):
        gos_user = GosUser(**validated_data)
        gos_user.set_password(validated_data['password'])
        gos_user.save()
        return gos_user


class ParticipantSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=400, required=False)

    class Meta:
        model = Participant
        exclude = ['groups', 'user_permissions', 'resetPasswordUUID', 'resetPasswordDate']

    def create(self, validated_data):
        participant = Participant(**validated_data)
        participant.set_password(validated_data['password'])
        participant.save()
        return participant


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSMIListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSMI
        fields = '__all__'


class CombinedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        user = self.context['request'].user
        if isinstance(instance, User) and instance == user:
            return UserListSerializer(instance).to_representation(instance)
        elif isinstance(instance, UserSMI) and instance == user:
            return UserSMIListSerializer(instance).to_representation(instance)
        else:
            raise PermissionDenied("You do not have permission to view this data.")


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super(CustomTokenRefreshSerializer, self).validate(attrs)
        decoded_payload = token_backend.decode(data['access'], verify=True)
        user_id = decoded_payload['user_id']
        user = User.objects.get(id=user_id)
        data.update({
            'profile':
                UserSerializer(user, context={'request': self.context['request']}).data
        })
        return data