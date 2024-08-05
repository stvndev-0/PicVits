from django.contrib import admin
from django.urls import path, include
from main import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('picvits.urls')),
    path('', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_DOOR)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)