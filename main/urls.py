from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls.static import static

from .yasg import urlpatterns as doc_urls
from . import settings
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenVerifyView,
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # APPS
    path('', include('apps.users.urls')),
    path('chat/', include('apps.chat.urls')),
    path('main_page/', include('apps.main_page.urls')),
    path('investor/', include('apps.investor.urls')),
    path('other/', include('apps.other.urls')),
    path('trade_zone/', include('apps.trade_zone.urls')),
]

urlpatterns += doc_urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

