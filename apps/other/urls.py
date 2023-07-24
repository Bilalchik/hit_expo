from django.urls import path

from apps.other.views import ExpectationView, PartnerView, SMIView, B2BView, NewsView


urlpatterns = [
    path('expectation/', ExpectationView.as_view()),
    path('partners/', PartnerView.as_view()),
    path('smi/', SMIView.as_view()),
    path('b2b/', B2BView.as_view()),
    path('news/', NewsView.as_view())
]
