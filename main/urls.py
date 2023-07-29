from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static

from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import (
    TokenVerifyView,
    TokenObtainPairView,
    TokenRefreshView,
)

from main import settings
from main.yasg import urlpatterns as doc_urls


schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restframework/', include('rest_framework.urls')),
    path('api/token/access/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # APPS
    path('user/', include('apps.users.urls')),
    path('chat/', include('apps.chat.urls')),
    path('main_page/', include('apps.main_page.urls')),
    path('investor/', include('apps.investor.urls')),
    path('feedback/', include('apps.feedback.urls')),
    path('other/', include('apps.other.urls')),
    path('trade_zone/', include('apps.trade_zone.urls')),
    path('invest_zone/', include('apps.invest_zone.urls')),
    path('fashion_zone/', include('apps.fashion_zone.urls')),
    path('b2b_meeting/', include('apps.b2b_meeting.urls')),
]

urlpatterns += doc_urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
