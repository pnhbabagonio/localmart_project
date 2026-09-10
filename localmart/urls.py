from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse


def api_home(request):
    """Simple API root view to confirm the server is running."""
    return JsonResponse({
        'message': 'Welcome to LocalMart API',
        'version': '1.0',
        'endpoints': {
            'admin': '/admin/',
            'token': '/api/v1/token/',
            'token_refresh': '/api/v1/token/refresh/',
            'register': '/api/v1/register/',
            'profile': '/api/v1/profile/',
            'logout': '/api/v1/logout/',
        }
    })


urlpatterns = [
    path('', api_home, name='api-home'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.accounts.urls')),
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)