from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('contacts/', include('contacts.urls')),
    path("", include("dashboard.urls")),
    path("admin/", admin.site.urls),
    path("auth/", include("django_googler.urls.default")),
]

# 🔥 THIS is what makes /static/ work
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
