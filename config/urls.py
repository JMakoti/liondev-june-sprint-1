from django.contrib import admin #Add commentMore actions
from django.urls import path, include
from django.views.generic import RedirectView  # Add this import
from rest_framework.routers import DefaultRouter
from user.views import UserViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='attendances:dashboard'), name='home'),  # Redirect to the dashboard
    path('', RedirectView.as_view(url='accounts/login/')),
    path('admin/', admin.site.urls),
    path('attendances/', include(('attendances.urls', 'attendances'), namespace='attendances')),
    path('accounts/', include('django.contrib.auth.urls')),   # Changed from empty path
    path('users/', include('user.urls')),  # Changed from empty path,
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
    