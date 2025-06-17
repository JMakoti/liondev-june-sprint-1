from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'check_in', 'check_out')
    list_filter = ('date', 'user__user_type')
    search_fields = ('user__username', 'user__email')