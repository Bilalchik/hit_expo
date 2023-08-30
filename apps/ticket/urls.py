from django.urls import path
from . import views


urlpatterns = [
    path('ticket_create/', views.TicketCreateView.as_view())
]
