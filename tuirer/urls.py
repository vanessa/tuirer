from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    # Django
    path('admin/', admin.site.urls),
    
    # Tuirer
    path('', include('core.urls')),
    path('', include('tuites.urls')),

    # Auth
    path('', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)