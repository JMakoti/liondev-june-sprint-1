from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    STAFF = 'staff'
    COMMUNITY = 'community'
    
    USER_TYPE_CHOICES = [
        (STAFF, 'Staff'),
        (COMMUNITY, 'Community Member'),
    ]
    
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default=COMMUNITY,
    )
    
    # Add these to properly handle staff/superuser permissions
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    def is_staff_member(self):
        return self.user_type == self.STAFF or self.is_staff
    
    def is_community(self):
        return self.user_type == self.COMMUNITY

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'