from django.urls import path
from .views import UserCreateAPIView, CustomAuthToken

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='user-register'),
    path('login/', CustomAuthToken.as_view(), name='user-login'),
]