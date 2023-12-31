from django.db.models import Q
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.users.models import User
from apps.b2b_meeting.models import Meeting
from apps.b2b_meeting.serializers import (MeetingListSerializer, MeetingAnswerCreateSerializer, 
                                            UserNameSerializer, MeetingCreateSerializer)


class IncomingListView(APIView):

    def get(self, request):
        meetings = Meeting.objects.filter(invited=request.user.id)
        serializer = MeetingListSerializer(meetings, many=True)

        return Response(serializer.data)

    @swagger_auto_schema(request_body=openapi.Schema(
        type="object",
        properties={
            "id": openapi.Schema(type="integer", example="1"),
            "answer": openapi.Schema(type="boolean", example=False),
        }
    ))
    def put(self, request):
        meeting_id = request.data.get('id')
        meeting = get_object_or_404(Meeting, id=meeting_id, invited=request.user)
        serializer = MeetingAnswerCreateSerializer(meeting, data=request.data)
        if serializer.is_valid():
            if 'answer' in request.data:
                answer = request.data['answer']
                meeting.answer = answer

                if answer:
                    meeting.status = 4
                else:
                    meeting.status = 1

                meeting.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeetingCreateView(APIView):

    def get(self, request, pk):
        user = User.objects.filter(id=pk)
        meetings = Meeting.objects.filter(Q(invited=pk) | Q(inviter=pk), status=4)
        meeting_serializer = MeetingListSerializer(meetings, many=True)
        user_serializer = UserNameSerializer(user, many=True)

        all_data = {
            'user': user_serializer.data,
            'meetings': meeting_serializer.data,
        }

        return Response(all_data)

    @swagger_auto_schema(request_body=openapi.Schema(
        type="object",
        properties={
            "inviter": openapi.Schema(type="integer", example="1"),
            "invited": openapi.Schema(type="integer", example="2"),
            "start": openapi.Schema(type="string", example='2023-09-12T16:00:00.142783+06:00'),
            "end": openapi.Schema(type="string", example='2023-09-12T18:00:00.142783+06:00'),
            "description": openapi.Schema(type="string", example="Я вызываю тебя на B2B встречу"),
        }
    ))
    def post(self, request, pk):
        # Получаем объект пользователя на основе pk из URL
        invited_user = get_object_or_404(User, id=pk)

        # Добавляем значение invited в request.data равным invited_user.id
        request.data['invited'] = invited_user.id

        serializer = MeetingCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SentListView(APIView):

    def get(self, request):
        meetings = Meeting.objects.filter(inviter=request.user.id).exclude(status=4)
        serializer = MeetingListSerializer(meetings, many=True)

        return Response(serializer.data)

    @swagger_auto_schema(request_body=openapi.Schema(
        type="object",
        properties={
            "id": openapi.Schema(type="integer", example="1"),
        }
    ))
    def put(self, request):
        meeting_id = request.data.get('id')
        meeting = get_object_or_404(Meeting, id=meeting_id)
        meeting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AppointedListView(APIView):

    def get(self, request):
        meetings = Meeting.objects.filter(Q(invited=request.user.id) | Q(inviter=request.user.id), status=4)
        serializer = MeetingListSerializer(meetings, many=True)

        return Response(serializer.data)

    @swagger_auto_schema(request_body=openapi.Schema(
        type="object",
        properties={
            "id": openapi.Schema(type="integer", example="1"),
            "answer": openapi.Schema(type="boolean", example=False),
        }
    ))
    def put(self, request):
        meeting_id = request.data.get('id')
        meeting = get_object_or_404(Meeting, Q(invited=request.user.id) | Q(inviter=request.user.id), status=4, id=meeting_id)
        serializer = MeetingAnswerCreateSerializer(meeting, data=request.data)
        if serializer.is_valid():
            if 'answer' in request.data:
                answer = request.data['answer']
                meeting.answer = answer

                if answer:
                    meeting.status = 4
                else:
                    meeting.status = 1

                meeting.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


