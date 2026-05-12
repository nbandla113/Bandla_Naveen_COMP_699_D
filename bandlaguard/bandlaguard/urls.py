from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # User Accounts
    path('', include('apps.accounts.urls')),

    # Content Processing
    path('content/', include('apps.content.urls')),

    # Shared Safety Spaces
    path('shared/', include('apps.shared_space.urls')),

    # Reports
    path('reports/', include('apps.reports.urls')),

    # Admin Panel
    path('adminpanel/', include('apps.adminpanel.urls')),
]

# ✅ SERVE STATIC + MEDIA FILES (DEV ONLY)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)