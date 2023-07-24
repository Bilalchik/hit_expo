from django.urls import path
from . import views


urlpatterns = [
    path('chats/', views.ChatRoomListView.as_view()),
    path('incoming/', views.IncomingListView.as_view()),
    path('sent/', views.SentListView.as_view()),
    path('chat_room_detail/<int:pk>/', views.ChatRoomDetailView.as_view()),
]
