from django.urls import path
from .views import ApplicationCreateListView, ApplicationDeleteView, FeedbackCreateListView, FeedbackDeleteView


urlpatterns = [
    ############   Заявка
    path('application/', ApplicationCreateListView.as_view()),
    path('application/<int:pk>', ApplicationDeleteView.as_view()),
    ############   Feedback
    path('feedback/', FeedbackCreateListView.as_view()),
    path('feedback/<int:pk>', FeedbackDeleteView.as_view()),
]