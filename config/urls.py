from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("attendances/", include("attendances.urls")),
    path('api/user/', include('user.urls')),
    path('admin/', admin.site.urls),
]
