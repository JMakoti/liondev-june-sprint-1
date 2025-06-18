from django.urls import path ,include
from . import views
from .views import UserCreateAPIView


urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='user-register'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    # Adding login to the Browsable API
    path('api-auth/', include('rest_framework.urls')),
    path('login/', include('django.contrib.auth.urls')),

]