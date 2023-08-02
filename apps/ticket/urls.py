from django.urls import path

from apps.ticket.views import TicketView, CheckView


urlpatterns = [
    path('ticket/', TicketView.as_view()),
    path('ticket/add/', TicketView.as_view()),
    path('ticket/<int:pk>/', TicketView.as_view()),

    path('check/', CheckView.as_view()),
    path('check/add/', CheckView.as_view()),
    path('check/<int:pk>/', CheckView.as_view()),
]
