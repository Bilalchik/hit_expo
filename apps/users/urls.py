from django.urls import path

from apps.users.views import UserMVS, UserSMI, CustomTokenRefreshView, UserLoginView, CurrentUserView

userPlural = {
    'get': 'list',
    'post': 'create'
}

useSingle = {
    'get': 'retrieve',
    'patch': 'update'
}

useSingle2 = {
    'get': 'retrieve',
    'post': 'create',
}

useSingle3 = {
    'get': 'retrieve',
    'patch': 'update',
    'post': 'create',
    'delete': 'destroy'
}

urlpatterns = [
    path('user/', UserMVS.as_view(userPlural)),
    path('user/<uuid:uniqueId>/', UserMVS.as_view(useSingle)),

    path('user-smi/', UserSMI.as_view(userPlural)),
    path('user-smi/<uuid:uniqueId>/', UserSMI.as_view(useSingle)),

    path('profile/', CurrentUserView.as_view()),

    path('check/', CustomTokenRefreshView.as_view()),

    path('login/', UserLoginView.as_view()),
]
