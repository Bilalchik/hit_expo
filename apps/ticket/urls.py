from django.urls import path

from apps.ticket.views import TicketView, TicketCreateView


urlpatterns = [
    path('ticket/', TicketView.as_view()),
    path('ticket/<int:pk>/', TicketView.as_view()),
    path('ticket/add/', TicketCreateView.as_view()),
]
