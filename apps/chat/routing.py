from django.urls import path

from apps.chat import consumers

websocket_urlpatterns = [
    path('ws/some_path/', consumers.ChatConsumer.as_asgi()),
]
