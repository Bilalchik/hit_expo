from django.urls import path
from . import views

urlpatterns = [
    path('trade_zone_list/', views.TradeZoneListView.as_view())
]
