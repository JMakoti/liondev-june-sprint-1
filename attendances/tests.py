from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework import status
from user.models import User
from .models import Attendance

class AttendanceTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            user_type='community'
        )
        self.staff = User.objects.create_user(
            username='staffuser',
            password='staffpass123',
            user_type='staff'
        )
        self.client.force_authenticate(user=self.user)

    def test_check_in(self):
        url = reverse('attendance-checkin')
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Attendance.objects.filter(user=self.user).exists())

    def test_check_out(self):
        # First check in
        Attendance.objects.create(user=self.user, date=timezone.now().date(), check_in=timezone.now())
        
        url = reverse('attendance-checkout')
        response = self.client.put(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        attendance = Attendance.objects.get(user=self.user)
        self.assertIsNotNone(attendance.check_out)

    def test_attendance_list(self):
        Attendance.objects.create(user=self.user, date=timezone.now().date(), check_in=timezone.now())
        
        # Test community user can see only their own records
        url = reverse('attendance-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
        # Test staff can see all records
        self.client.force_authenticate(user=self.staff)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)