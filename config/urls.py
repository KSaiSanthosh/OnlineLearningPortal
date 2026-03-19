from django.contrib import admin
from django.urls import path, include

# Static files support
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Django authentication (login, logout, etc.)
    path('accounts/', include('django.contrib.auth.urls')),

    # Your app
    path('', include('portal.urls')),
]

# Serve static files (IMPORTANT FIX)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)