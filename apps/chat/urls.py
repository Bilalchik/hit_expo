from django.urls import path
from . import views


urlpatterns = [
    path('chats/', views.MessageListView.as_view()),
    path('chat/<int:pk>', views.MessageCreateDetailView.as_view())
]
