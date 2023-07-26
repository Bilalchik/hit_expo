from django.urls import path
from . import views


urlpatterns = [
    path('invest_zone_list/', views.InvestZoneListView.as_view())
]
