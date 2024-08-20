from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from main import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('picvits.urls')),
    path('users/', include('users.urls')),
    path('login/', user_views.login_view, name='login'),
    path('register/', user_views.register_view, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_DOOR)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)