from django.urls import path

from apps.chat.views import MessageView


urlpatterns = [
    path('messages/', MessageView.as_view())
]
