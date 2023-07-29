from django.urls import path
from . import views


urlpatterns = [
    path('incoming_list/', views.IncomingListView.as_view()),
    path('meeting_create/<int:pk>', views.MeetingCreateView.as_view()),
    path('sent_list/', views.SentListView.as_view()),
    path('appointed_list/', views.AppointedListView.as_view()),
]
