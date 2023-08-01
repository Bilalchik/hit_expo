from django.urls import path
from . import views


urlpatterns = [
    path('food_zone_list/', views.FoodZoneDeleteView.as_view())
]
