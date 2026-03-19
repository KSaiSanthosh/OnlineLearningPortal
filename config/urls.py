from django.contrib import admin
from django.urls import path, include

# 🔥 ADD THESE IMPORTS
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Django authentication
    path('accounts/', include('django.contrib.auth.urls')),

    # Your app
    path('', include('portal.urls')),
]

# 🔥 VERY IMPORTANT (this fixes your admin CSS)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)