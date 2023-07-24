from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.state import token_backend
from rest_framework.exceptions import PermissionDenied

from apps.users.models import User, UserSMI


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
        print("priver doni")
        for field, value in validated_data.items():
            if field == 'password':
                instance.set_password(value)
            else:
                setattr(instance, field, value)
        instance.save()
        return instance


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


class UserSMISerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=400, required=False)

    class Meta:
        model = UserSMI
        fields = '__all__'

    def create(self, validated_data):
        user_smi = UserSMI(**validated_data)
        user_smi.set_password(validated_data['password'])
        user_smi.save()
        return user_smi

    def update(self, instance, validated_data):
        print("priver doni")
        for field, value in validated_data.items():
            if field == 'password':
                instance.set_password(value)
            else:
                setattr(instance, field, value)
        instance.save()
        return instance


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


