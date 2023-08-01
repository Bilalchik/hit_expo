from django.urls import path
from . import views

urlpatterns = [
    path('visit_list/', views.VisitListView.as_view()),
    path('visit_create/', views.VisitCreateView.as_view()),
]
