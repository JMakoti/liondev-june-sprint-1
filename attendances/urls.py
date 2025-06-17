from django.urls import path
from .views import (
    AttendanceCheckInAPIView,
    AttendanceCheckOutAPIView,
    AttendanceListAPIView
)

urlpatterns = [
    path('checkin/', AttendanceCheckInAPIView.as_view(), name='attendance-checkin'),
    path('checkout/', AttendanceCheckOutAPIView.as_view(), name='attendance-checkout'),
    path('list/', AttendanceListAPIView.as_view(), name='attendance-list'),
]