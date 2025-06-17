from rest_framework import serializers
from .models import Attendance
from user.models import User

class AttendanceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Attendance
        fields = ('id', 'user', 'date', 'check_in', 'check_out', 'notes')
        read_only_fields = ('date', 'check_in', 'check_out')