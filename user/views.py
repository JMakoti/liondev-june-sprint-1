from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def perform_create(self, serializer):
    serializer.save(owner=self.request.user)