from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.utils import timezone
from .models import Attendance
from .serializers import AttendanceSerializer
from user.models import User

class AttendanceCheckInAPIView(generics.CreateAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        attendance, created = Attendance.objects.get_or_create(
            user=self.request.user,
            date=timezone.now().date(),
            defaults={'check_in': timezone.now()}
        )
        if not created and not attendance.check_in:
            attendance.check_in = timezone.now()
            attendance.save()

class AttendanceCheckOutAPIView(generics.UpdateAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = None

    def get_object(self):
        today = timezone.now().date()
        return Attendance.objects.get(user=self.request.user, date=today)

    def update(self, request, *args, **kwargs):
        attendance = self.get_object()
        if not attendance.check_out:
            attendance.check_out = timezone.now()
            attendance.save()
            return Response({'status': 'checked out'})
        return Response({'status': 'already checked out'}, status=status.HTTP_400_BAD_REQUEST)

class AttendanceListAPIView(generics.ListAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff():
            return Attendance.objects.all()
        return Attendance.objects.filter(user=self.request.user)