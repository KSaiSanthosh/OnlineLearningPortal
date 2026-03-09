from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Django authentication (login, logout, password change)
    path('accounts/', include('django.contrib.auth.urls')),

    # Portal app URLs
    path('', include('portal.urls')),
]