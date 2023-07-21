from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Message
from .serializers import MessageListSerializer, MessageCreateSerializer


class MessageListView(ListAPIView):
    serializer_class = MessageListSerializer

    def get_queryset(self):
        return Message.objects.filter(sender=self.request.user)


class MessageCreateDetailView(APIView):

    def get(self, request, pk):
        queryset = Message.objects.filter(receiver__id=pk)

        serializer = MessageListSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, pk):

        serializer = MessageCreateSerializer(data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


