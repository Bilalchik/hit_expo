from django.urls import path

from apps.investor.views import InvestorView, CountryView, TextView


urlpatterns = [
    path('investors/', InvestorView.as_view()),
    path('country/', CountryView.as_view()),
    path('text/', TextView.as_view())
]
