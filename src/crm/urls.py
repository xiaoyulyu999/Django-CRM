from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("dashboard.urls")),
    path("admin/", admin.site.urls),
    path("auth/", include("django_googler.urls.default")),
    # path('accounts/', include('allauth.urls')),
]
