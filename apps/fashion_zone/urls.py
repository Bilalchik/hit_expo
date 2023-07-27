from django.urls import path
from . import views


urlpatterns = [
    path('fashion_zone_list/', views.FashionZoneListView.as_view())
]
