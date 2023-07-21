from django.urls import path

from apps.main_page.views import (PlaceView, PlaceOfficeView, PartnersView,
                                    MembersView, ForumView, TargetView,
                                    TasksView, EllipseView, OrganizersView,
                                    VideoView, SectorsView, SpeakersView,
                                    SponsorsView, SocialsView, PageOneView)

urlpatterns = [
    path('main-page/',PageOneView.as_view()),
    path('members/',MembersView.as_view()),
    path('forum/',ForumView.as_view()),    
    path('target/',TargetView.as_view()),  
    path('tasks/',TasksView.as_view()),   
    path('ellipse/',EllipseView.as_view()),
    path('video/',VideoView.as_view()),   
    path('sectors/',SectorsView.as_view()),
    path('place/',PlaceView.as_view()),
    path('speakers/',SpeakersView.as_view()),
    path('organizers/',OrganizersView.as_view()),
    path('sponsors/',SponsorsView.as_view()),
    path('partners/',PartnersView.as_view()),
    path('place-office/',PlaceOfficeView.as_view()),
    path('socials/',SocialsView.as_view()),
]