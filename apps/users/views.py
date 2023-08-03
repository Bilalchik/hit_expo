from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView

from django.db.models import Q
from .models import Book, Participant
from rest_framework import generics

from apps.users.models import User, UserSMI, Expert, Visitor, GosUser, UserType
from apps.users.serializers import (
    UserCRUDSerializer, CustomTokenRefreshSerializer, LoginUserSerializer, UserSMISerializer, CombinedUserSerializer,
    ExpertSerializer, VisitorSerializer, GosUserSerializer, ParticipantSerializer, BookSerializer
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
    lookup_field = 'uniqueId'
    serializer_class = UserCRUDSerializer
    filter_backends = [filters.SearchFilter]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserSMIViewSet(viewsets.ModelViewSet):
    queryset = UserSMI.objects.all()
    lookup_field = 'uniqueId'
    serializer_class = UserSMISerializer
    filter_backends = [filters.SearchFilter]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        unique_id = kwargs['uniqueId']
        user_smi = UserSMI.objects.get(uniqueId=unique_id)
        serializer = UserSMISerializer(user_smi, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class ExpertViewSet(viewsets.ModelViewSet):
    queryset = Expert.objects.all()
    lookup_field = 'uniqueId'
    serializer_class = ExpertSerializer
    filter_backends = [filters.SearchFilter]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        unique_id = kwargs['uniqueId']
        expert = Expert.objects.get(uniqueId=unique_id)
        serializer = ExpertSerializer(expert, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    lookup_field = 'uniqueId'
    serializer_class = VisitorSerializer
    filter_backends = [filters.SearchFilter]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        unique_id = kwargs['uniqueId']
        visitor = Visitor.objects.get(uniqueId=unique_id)
        serializer = VisitorSerializer(visitor, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class GosUserViewSet(viewsets.ModelViewSet):
    queryset = GosUser.objects.all()
    lookup_field = 'uniqueId'
    serializer_class = GosUserSerializer
    filter_backends = [filters.SearchFilter]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        unique_id = kwargs['uniqueId']
        gos_user = GosUser.objects.get(uniqueId=unique_id)
        serializer = GosUserSerializer(gos_user, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    lookup_field = 'uniqueId'
    serializer_class = ParticipantSerializer
    filter_backends = [filters.SearchFilter]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        unique_id = kwargs['uniqueId']
        participant = Participant.objects.get(uniqueId=unique_id)
        serializer = ParticipantSerializer(participant, data=request.data, context={'request': request})
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
                user = self._get_user(user.user_type, user.id)
                show_serializer = self._get_serializer(user)
                return Response(show_serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            pass
        
        return Response(status=status.HTTP_403_FORBIDDEN)

    def _get_serializer(self, *args, **kwargs):
        user = args[0]

        if user.user_type == UserType.MASS_MEDIA:
            return UserSMISerializer(user)
        elif user.user_type == UserType.VISITOR:
            return VisitorSerializer(user)
        elif user.user_type == UserType.GOV_USER:
            return GosUserSerializer(user)
        elif user.user_type == UserType.EXPERT:
            return ExpertSerializer(user)
        elif user.user_type == UserType.PARTICIPANT:
            return ParticipantSerializer(user)

    def _get_user(self, user_type, user_id):

        if user_type == UserType.MASS_MEDIA:
            return UserSMI.objects.get(id=user_id)
        elif user_type == UserType.VISITOR:
            return Visitor.objects.get(id=user_id)
        elif user_type == UserType.GOV_USER:
            return GosUser.objects.get(id=user_id)
        elif user_type == UserType.EXPERT:
            return Expert.objects.get(id=user_id)
        elif user_type == UserType.PARTICIPANT:
            return Participant.objects.get(id=user_id)


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = CombinedUserSerializer(user, context={'request': request})
        return Response(serializer.data)


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
class BookSearchView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get('q', '')
        return Book.objects.filter(Q(title__icontains=search_query) | Q(author__icontains=search_query) | Q(genre__icontains=search_query))