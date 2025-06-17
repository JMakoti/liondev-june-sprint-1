from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.staff_user = User.objects.create_user(
            username='staff',
            password='password123',
            user_type='staff'
        )
        self.community_user = User.objects.create_user(
            username='community',
            password='password123',
            user_type='community'
        )

    def test_user_registration(self):
        url = reverse('user-register')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123',
            'user_type': 'community'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 3)

    def test_user_login(self):
        url = reverse('user-login')
        data = {
            'username': 'community',
            'password': 'password123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)