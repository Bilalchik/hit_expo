from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework import viewsets, permissions, status, generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView

from apps.users.models import User
from apps.users.serializers import (
    UserCRUDSerializer, CustomTokenRefreshSerializer, LoginUserSerializer
)


class MVSDynamicPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'update':
            if request.user.is_authenticated:
                return True
            else:
                return False
        else:
            return True


class UserMVS(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # permission_classes = [MVSDynamicPermission]
    lookup_field = 'uniqueId'
    serializer_class = UserCRUDSerializer
    # filter_backends = [DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ['email', 'type_register']
    filterset_fields = ('email', 'type_register')

    def create(self, request, *args, **kwargs):
        # secretAdminKey = request.data.get('secretAdminKey')
        # if secretAdminKey == settings.SECRET_ADMIN_KEY:
        #     serializer = UserCRUDSerializer(data={'password': settings.DEFAULT_PASSWORD}, context={'request': request})
        #     serializer.is_valid(raise_exception=True)
        #     serializer.save()
        #     return Response(data=f"{settings.CLIENT_URL}/user/{serializer.data['uniqueId']}")
        # return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = self.serializer_class(
            data=request.data, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        user = request.user
        data = request.data.dict()
        serializer = UserCRUDSerializer(user, data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer


class UserLoginView(APIView):
    queryset = User.objects.all()
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            user = User.objects.get(email=serializer.validated_data['email'])
            if user.check_password(serializer.validated_data['password']):
                show_serializer = UserCRUDSerializer(user)
                return Response(show_serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            pass
        
        return Response(status=status.HTTP_403_FORBIDDEN)
